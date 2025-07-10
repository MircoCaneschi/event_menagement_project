# Event Management System

A Django-based web application to create, manage, and attend events. This project was developed as part of a university assignment.

---

##  Features

- User authentication with custom roles
- Two user groups:
  - **Attendee**: can view events, register/unregister, and view their registrations
  - **Organizer**: has all attendee permissions, plus can create, edit, delete events and view the list of attendees
- Event creation and registration system
- Dynamic pages using Django Templates
- Permissions and access control
- Pre-populated database included for testing

---

##  Tech Stack

- Python
- Django
- SQLite
- HTML/CSS (Bootstrap or custom)
- Deployment on Render (or any other free hosting)

---

#  Local Setup

## 1. Clone the repository:
    git clone https://github.com/tuo-username/tuo-repo.git
    cd event_menagement_project-recovery-branch

## 2. Create a virtual environment
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

## 3. Install the dependencies
    pip install -r requirements.txt

## 4. Run the development server
    python manage.py runserver

## 5. Access the application at 
http://127.0.0.1:8000

---
# Pre-populated Database
The db.sqlite3 file is included and contains sample data, so you can start testing the app right away.

---
# Live Deployment
https://event-menagement-project.onrender.com/

---
# Demo Credentials
You can use these test accounts to explore the app:

#### Superuser Django:
Username: admin  
Password: Passwordprova123  
Email: admin@example.com  

#### first_organizer:
Username: first_organizer  
Password: Passwordprova123  
Email: firstOrg@example.com  

#### attendee1:
Username: attendee1  
Password: Passwordprova123  
Email: attendee1@example.com  

#### organizer2:
Username: organizer2  
Password: Passwordprova123  
Email: organizer2@example.com  

#### organizer3:
Username: organizer3  
Password: Passwordprova123  
Email: organizer3@example.com  