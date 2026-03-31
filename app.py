from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import datetime
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'complaints.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS complaints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                complaint_type TEXT NOT NULL,
                severity TEXT NOT NULL,
                customer_type TEXT NOT NULL,
                priority TEXT NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Open'
            )
        ''')
        
        # Ensure status column exists for older database versions
        cursor.execute("PRAGMA table_info(complaints)")
        columns = [column[1] for column in cursor.fetchall()]
        if 'status' not in columns:
            cursor.execute("ALTER TABLE complaints ADD COLUMN status TEXT NOT NULL DEFAULT 'Open'")
        db.commit()

# --- RULE ENGINE (EXPERT SYSTEM) ---
def determine_priority(complaint_type, severity, customer_type):
    # Rule 1
    if complaint_type == "Server Down":
        return "High"
    
    # Rule 2
    elif complaint_type == "Payment Issue" and customer_type == "Premium":
        return "High"
    
    # Extension logic
    elif complaint_type == "Payment Issue" and customer_type == "Standard" and severity == "Critical":
        return "High"
    
    # Rule 3
    elif complaint_type == "Login Issue":
        if severity == "Critical":
            return "High"
        else:
            return "Medium"
    
    # Rule 4
    elif complaint_type == "General Inquiry":
        return "Low"
    
    # Default Inference Base
    else:
        if severity == "Critical":
            return "Medium"
        return "Low"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_complaint():
    complaint_type = request.form.get("complaint_type")
    severity = request.form.get("severity")
    customer_type = request.form.get("customer_type")
    
    # Process through Rule-Based Inference Engine
    priority = determine_priority(complaint_type, severity, customer_type)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO complaints (complaint_type, severity, customer_type, priority, date, status)
        VALUES (?, ?, ?, ?, ?, 'Open')
    """, (complaint_type, severity, customer_type, priority, date_str))
    db.commit()
    complaint_id = cursor.lastrowid
    
    return redirect(url_for("result", complaint_id=complaint_id))

@app.route("/result/<int:complaint_id>", methods=["GET"])
def result(complaint_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM complaints WHERE id = ?", (complaint_id,))
    complaint = cursor.fetchone()
    
    if not complaint:
        return "Complaint not found", 404
        
    return render_template("result.html", complaint=complaint)

@app.route("/admin", methods=["GET"])
def admin():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM complaints ORDER BY id DESC")
    complaints = cursor.fetchall()
    
    # Calculate simple analytics
    total = len(complaints)
    open_cases = sum(1 for c in complaints if c['status'] in ['Open', 'In Progress'])
    high_priority = sum(1 for c in complaints if c['priority'] == 'High')
    resolved_cases = sum(1 for c in complaints if c['status'] == 'Resolved')

    return render_template("admin.html", 
                           complaints=complaints, 
                           total=total, 
                           open_cases=open_cases, 
                           high_priority=high_priority,
                           resolved_cases=resolved_cases)

@app.route("/track", methods=["GET", "POST"])
def track():
    complaint = None
    error = None
    if request.method == "POST":
        complaint_id = request.form.get("complaint_id")
        if complaint_id and complaint_id.isdigit():
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM complaints WHERE id = ?", (complaint_id,))
            complaint = cursor.fetchone()
            if not complaint:
                error = "No complaint found with this ID."
        else:
            error = "Please enter a valid numeric Complaint ID."
    return render_template("track.html", complaint=complaint, error=error)

@app.route("/update_status/<int:complaint_id>", methods=["POST"])
def update_status(complaint_id):
    new_status = request.form.get("status")
    if new_status in ["Open", "In Progress", "Resolved"]:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE complaints SET status = ? WHERE id = ?", (new_status, complaint_id))
        db.commit()
    return redirect(url_for("admin"))

if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH))
    init_db()
    app.run(debug=True, port=5000)
