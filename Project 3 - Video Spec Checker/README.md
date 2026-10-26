# Multi-Platform Video Spec Checker

A tool that reads video files and checks their dimensions, aspect ratio, and duration against the specific technical requirements of social media platforms (TikTok, Instagram Reels, YouTube Shorts, etc.).

## Features
- *External Library Integration:* Uses the hachoir library to extract video metadata (width, height, duration) without needing external tools like FFmpeg.
- *Dynamic Rule Engine:* Uses a scalable dictionary to store platform rules, making it easy to add new platforms or formats.
- *Graceful Error Handling:* Features a try/except block to guide users on how to install the missing hachoir library, and prevents crashes if a folder is selected instead of a file.
- *Interactive UI:* Includes a while True menu loop and a summary counter at the end of the report.

## Technologies Used
- Python 3
- hachoir (Video metadata extraction)
- os (File system navigation)

## How to Run
1. Ensure you have the required library: pip install hachoir
2. Run the script: python "Multi-Platform Video Spec Checker.py"
3. Enter the name of a video file on your system to generate a compliance report.
