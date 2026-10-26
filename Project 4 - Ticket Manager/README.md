# IT Support Ticket & Error Log Analyser

A CLI ticketing system designed to simulate an IT helpdesk environment. It manages support requests, tracks priorities, and flags urgent issues.

## Features
- *Auto-Generating IDs:* Automatically parses the last ticket to generate the next sequential ID (e.g., TICK-105).
- *Smart Acronym Formatting:* Automatically fixes department names (e.g., typing "it" becomes "IT").
- *Priority Analysis:* Generates a report that categorizes tickets by urgency and escalates High-priority issues for immediate developer investigation.
- *Safe Deletion:* Requires explicit yes confirmation before permanently deleting a ticket to prevent accidental data loss.
- *JSON Persistence:* Saves tickets locally using absolute file paths so the data persists regardless of where the script is run.

## Technologies Used
- Python 3
- json and os modules.

## How to Run
1. Run the script: python "IT Support Ticket & Error Log Analyser.py"
2. Use the interactive menu to add, view, delete, or analyse tickets.
