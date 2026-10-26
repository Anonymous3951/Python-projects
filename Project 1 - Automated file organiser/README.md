# Automated File Organiser

A Python script designed to automatically sort messy folders by moving files into categorized subfolders (Videos, Images, Audio, Notes, Documents, Archives) based on their file extensions.

## Features
- *Data Loss Prevention:* Automatically detects if a file with the same name already exists in the destination folder and renames it (e.g., file (1).mp4) instead of overwriting it.
- *Smart Searching:* If the target folder isn't in the current directory, the script searches the user's home directory. It uses directory pruning to skip heavy system folders (like AppData or Library) to save time.
- *Case-Insensitive Matching:* Ensures the folder is found regardless of how the user types the capitalisation.
- *Scalable Dictionary:* Uses a dictionary map to easily add new file types and categories.

## Technologies Used
- Python 3
- os and shutil modules for file system interaction.

## How to Run
1. Run the script: python "Automated file organiser.py"
2. Enter the name of the folder you want to organise (e.g., Downloads).
3. The script will safely sort the files.
