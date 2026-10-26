# GUI Weather Application

A desktop application built with Python that fetches live weather data from the OpenWeatherMap API and displays it in a graphical interface.

## Features
- *Graphical User Interface (GUI):* Built entirely with tkinter, featuring text inputs, buttons, and dynamic label updates.
- *Live API Integration:* Uses the requests library to make HTTP GET requests to a REST API.
- *JSON Parsing:* Extracts specific weather details (temperature, condition) from deeply nested JSON dictionaries.
- *Robust Error Handling:* Uses try/except blocks to catch network errors and handles invalid city inputs gracefully without crashing the app.

## Technologies Used
- Python 3
- tkinter (GUI framework)
- requests (API requests)
- OpenWeatherMap API

## Files Included
- Weather App.py: The main graphical application.
- Weather Test.py: A CLI script used to test API connectivity before building the GUI.

## How to Run
1. Install the requests library: pip install requests
2. Sign up at OpenWeatherMap.org to get a free API key.
3. Open both .py files and replace "PASTE_YOUR_API_KEY_HERE" with your actual key.
4. Run the GUI: python "Weather App.py"
