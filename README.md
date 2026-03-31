# 📌 Smart Complaint Management System

## 🚀 Overview
The **Smart Complaint Management System** is a web-based application built using **Flask (Python)** that automates complaint handling using a **rule-based expert system**.

It allows users to submit complaints, automatically assigns priority based on predefined rules, and enables admins to manage and track complaints efficiently.

---

## 🎯 Problem Statement
Handling large volumes of complaints in systems like IT helpdesks, customer support, and government portals is challenging due to:

- Slow manual prioritization  
- Inconsistent decision-making  
- Delayed response time  

This project solves these issues using an **AI-based rule system** for automatic complaint prioritization.

---

## 🧠 AI Concept Used

### Expert System (Rule-Based AI)

The system is based on:

- **Knowledge Base** → Complaint rules  
- **Rule Base** → IF-THEN conditions  
- **Inference Engine** → Decision-making logic  

### Example Rules:
- Server Down → **High**  
- Payment Issue + Premium Customer → **High**  
- Login Issue → **Medium**  
- General Inquiry → **Low**

---

## 🏗️ Features

### 👤 User
- Submit complaints  
- Automatic priority assignment  
- View complaint result  

### 🔍 Tracking
- Track complaint using ID  
- View status (Open / In Progress / Resolved)

### 🛠️ Admin
- View all complaints  
- Update complaint status  
- Dashboard insights:
  - Total complaints  
  - Open cases  
  - High priority cases  
  - Resolved cases  

---

## ⚙️ Tech Stack

- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, Jinja Templates  
- **Database:** SQLite  

---

## 🗂️ Project Structure


Smart-Complaint-Management-System/
│
├── app.py
├── database/
│ └── complaints.db
├── templates/
│ ├── index.html
│ ├── result.html
│ ├── admin.html
│ └── track.html
├── static/
│ └── style.css
└── README.md


---

## 🧩 Workflow

1. User submits a complaint  
2. System applies rule-based logic  
3. Priority is assigned (High / Medium / Low)  
4. Complaint is stored in database  
5. Admin updates status  
6. User can track complaint anytime  

---

## 🧮 Rule Engine Logic

Function used:


determine_priority(complaint_type, severity, customer_type)


### Rules:
- Server Down → High  
- Payment Issue + Premium → High  
- Payment Issue + Critical → High  
- Login Issue + Critical → High  
- Login Issue → Medium  
- General Inquiry → Low  
- Default → Based on severity  

---

## ▶️ How to Run

```bash
git clone https://github.com/vivek-kothekar/Smart-Complaint-Management-System.git
cd Smart-Complaint-Management-System
pip install flask
python app.py

Open in browser:

http://127.0.0.1:5000/
---
📊 Database Schema
Field	Description
id	Complaint ID
complaint_type	Type of complaint
severity	Severity
customer_type	Customer category
priority	Assigned priority
date	Submission time
status	Complaint status
---
📌 Sample

Input:

Complaint Type: Server Down
Severity: Critical
Customer: Premium

Output:
👉 Priority = HIGH
---
📈 Advantages
Faster resolution
Automated prioritization
Reduced manual work
Consistent decisions
Improved efficiency
---
🌍 Applications
IT Helpdesk Systems
E-commerce Support
Banking Systems
Telecom Services
Government Portals
---
🔮 Future Enhancements
Authentication system
Email/SMS alerts
ML-based prioritization
Advanced analytics
Cloud deployment
