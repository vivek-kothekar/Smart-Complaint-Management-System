# 📌 Smart Complaint Management System (Expert System)

## 🚀 Overview

The **Smart Complaint Management System** is a web-based application built using **Flask (Python)** that acts as a **Rule-Based Expert System**.

It automatically evaluates customer complaints and assigns **priority levels (High, Medium, Low)** using predefined logical rules, helping organizations handle issues faster and more efficiently.

---

## 🎯 Problem Statement

In systems like IT helpdesks and customer support:

* Complaints are manually reviewed
* Priority assignment is slow and inconsistent
* Critical issues may get delayed

This project solves the problem using an **automated rule-based decision system**.

---

## 🧠 AI Concept Used

### 🔹 Expert System (Symbolic AI)

This project is based on **classical AI (Symbolic AI)**

It mimics the decision-making of a human expert using rules.

### Core Components:

* **Knowledge Base** → IF-THEN rules inside `determine_priority()`
* **Working Memory** → User inputs (complaint_type, severity, customer_type)
* **Inference Engine** → Python logic that applies rules

---

## ⚙️ Logic Method

### Forward Chaining

The system uses a **data-driven approach**:

1. Takes user input (facts)
2. Applies rules step-by-step
3. Produces final decision (priority)

---

## 🏗️ Features

### 👤 User

* Submit complaints
* Automatic priority assignment
* Receive complaint ID

### 🔍 Tracking

* Track complaint using ID
* View status (**Open / In Progress / Resolved**)

### 🛠️ Admin Dashboard

* View all complaints
* Update complaint status
* View analytics:

  * Total complaints
  * High priority cases
  * Resolved cases

---

## ⚙️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, Jinja2
* **Database:** SQLite

---

## 🗂️ Project Structure

```id="final1"
Smart-Complaint-Management-System/
│
├── app.py                  # Backend + Expert System logic
├── README.md
│
├── database/
│   └── complaints.db       # SQLite database
│
├── static/
│   └── style.css           # UI styling
│
└── templates/
    ├── index.html          # Complaint form
    ├── result.html         # Priority result
    ├── track.html          # Track complaint
    └── admin.html          # Admin dashboard
```

---

## 🧩 System Workflow

1. User submits complaint form
2. Data is sent to Flask backend
3. `determine_priority()` evaluates inputs
4. Priority is assigned using rules
5. Data is stored in SQLite database
6. Admin manages complaints
7. User tracks status using ID

---

## 🧮 Rule Engine Logic

**Function:**

```id="final2"
determine_priority(complaint_type, severity, customer_type)
```

### Example Rules:

* Server Down → High
* Payment Issue + Premium → High
* Payment Issue + Critical → High
* Login Issue + Critical → High
* Login Issue → Medium
* General Inquiry → Low

---

## ▶️ How to Run

```bash
git clone https://github.com/vivek-kothekar/Smart-Complaint-Management-System.git
cd Smart-Complaint-Management-System
pip install flask
python app.py
```

Open in browser:
http://127.0.0.1:5000/

---

## 📊 Database Schema

| Field          | Description       |
| -------------- | ----------------- |
| id             | Complaint ID      |
| complaint_type | Type of complaint |
| severity       | Severity level    |
| customer_type  | Customer type     |
| priority       | Assigned priority |
| date           | Submission time   |
| status         | Complaint status  |

---

## 📌 Sample

**Input:**

* Complaint Type: Server Down
* Severity: Critical
* Customer: Premium

**Output:**
👉 Priority = **HIGH**

---

## 📈 Advantages

* Fast complaint processing
* Automated prioritization
* Reduces manual effort
* Consistent decision-making
* Easy to implement and scalable

---

## 🌍 Applications

* IT Helpdesk Systems
* Customer Support Platforms
* Banking & Financial Services
* E-commerce Systems
* Government Complaint Portals

---

## 🔮 Future Enhancements

* User authentication system
* Email/SMS notifications
* Advanced analytics dashboard
* Cloud deployment

---

## 🎓 Academic Note

This project demonstrates a **Rule-Based Expert System using Symbolic AI**.

Unlike Machine Learning, it provides:

* Deterministic results
* No training data requirement
* High reliability for critical systems
