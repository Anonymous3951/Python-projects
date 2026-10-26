# Studio Equipment Inventory Manager

A data-persistent Command Line Interface (CLI) application used to track, update, and manage studio equipment inventory.

## Features
- *JSON Data Persistence:* Saves all equipment data (quantities and statuses) to a local .json file, ensuring no data is lost when the program closes.
- *CRUD Operations:* Allows users to View, Add, Update Quantity, Update Status, and Remove equipment.
- *Modular Architecture:* Refactored into modular functions with a main menu loop for better code maintainability.
- *Input Validation:* Uses try/except blocks to handle invalid user inputs (like typing text instead of a number) and prevents negative stock quantities.

## Technologies Used
- Python 3
- json (Data persistence)
- os (File pathing)
- time (Terminal typing effect)

## How to Run
1. Run the script: python "Studio Equipment Inventory Manager.py"
2. Follow the on-screen menu to manage the inventory.
