# Enterprise Support Portal

A full-stack web application designed to simulate an Enterprise ERP support ticketing system. This project demonstrates database management, backend routing, and dynamic frontend templating.

## Features
- *SQL Database:* Uses SQLite to create, store, and query support tickets.
- *Create:* Users can submit new tickets via a web form.
- *Read:* Dynamically displays all active tickets in a styled HTML table.
- *Delete:* Users can safely delete tickets with a built-in JavaScript confirmation prompt.
- *Backend Validation:* Uses .strip() to prevent blank submissions and validates dropdown inputs to prevent frontend tampering.
- *Secure Queries:* Uses parameterized queries (?) to prevent SQL Injection attacks.

## Technologies Used
- Python 3
- Flask (Web Framework)
- SQLite3 (Database)
- HTML5 & CSS3
- Jinja2 (Templating Engine)

## How to Run
1. Clone the repository.
2. Run python "Database Setup.py" to create and seed the database.
3. Run python app.py to start the Flask server.
4. Open your browser and go to http://127.0.0.1:5000.
