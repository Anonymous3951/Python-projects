import os   #used to interact with files

try:                                                                                                #if hachoir library is not installed 
    from hachoir.parser import createParser                  #the program will crash
    from hachoir.metadata import extractMetadata      #so we use try/except block
except ImportError:
    print("The 'hachoir' library is missing")
    print("Please run pip install hachoir")
    exit()
    
#dictionary with rules for each platform, with a mini dictionary inside
platform_rules = {
    "TikTok": {"label": "9:16 (Vertical)", "ratio_w": 9, "ratio_h": 16, "max_duration": 180},
    "Instagram Reels": {"label": "9:16 (Vertical)", "ratio_w": 9, "ratio_h": 16, "max_duration": 90},
    "YouTube Shorts":  {"label": "9:16 (Vertical)", "ratio_w": 9, "ratio_h": 16, "max_duration": 180},
    "YouTube Standard": {"label": "16:9 (Horizontal)", "ratio_w": 16, "ratio_h": 9, "max_duration": 3600},
    "Instagram Feed":   {"label": "4:5 (Vertical)",  "ratio_w": 4,  "ratio_h": 5, "max_duration": 60},
}

#first we need to find the file 
def find_video_file(filename):    #we create a function that takes in  the file name 
    path = os.path.expanduser(filename)   #assigns "filename" to "path" variable
    if os.path.exists(path):
        return path                           # if the user typed the full path instead of name

    print(f"Searching for '{filename}'... Please wait.")
    home_dir = os.path.expanduser("~")      #main folder for the users account

    wanted = os.path.basename(filename).lower()   #gets just file name with no folders that may have been included
    found_it = False
    result = None

    for root, dirs, files in os.walk(home_dir):   #goes through every folder in users main account folder
        dirs[:] =  [d for d in dirs if not d.startswith(".") and d not in ["AppData", "Library"]]   #skips system files, saving time
        for file_name in files:
            name_without_ext = os.path.splitext(file_name)[0].lower()   #retrives each file name without extension

            if name_without_ext == wanted or file_name.lower() == wanted:
                result = os.path.join(root, file_name)
                found_it = True
                break     #once found loop ends 

        if found_it:
            break     #used to exit the outer loop

    return result

#now we get video details
def get_video_details(path):
    if not os.path.isfile(path):    #checks if it is a file to prevent crash
        return None    
    parser = createParser(path)   #figures out what kind of video file this is 
    if parser is None:
        return None

    with parser:
        metadata = extractMetadata(parser)  #extracts all data

    if metadata is None:
        return None

    width = metadata.get("width")
    height = metadata.get("height")
    duration = metadata.get("duration")

    if width is None or height is None or duration is None:         #these prevent system from crashing
        return None                                                                                     #if there are no values found

    seconds = duration.total_seconds()  #.total_seconds converts timedelta into a simple decimal
    
    return width, height, seconds


def check_video_specs(filename, width, height, duration):
    print(f"\n--- Compliance Report for: '{filename}' ---")
    print(f"{width}x{height} pixels, {duration:.1f} seconds long\n")

    video_ratio = width / height
    passed_count = 0

    for platform, rules in platform_rules.items():  #.items() retrieves keys and values in a pair, platform refers to key and rules refers to values
        expected_ratio = rules["ratio_w"] / rules["ratio_h"]
        problems = []

        difference = abs(video_ratio - expected_ratio) / expected_ratio   #abs makes sure its positive
        if difference > 0.01:   #we allow 1%, due to rounding
            problems.append(f"Wrong shape (expected {rules['label']})")

        if duration > rules["max_duration"]:
            problems.append(f"Too long (max {rules['max_duration']} seconds)")

        if len(problems) == 0:
            print(f"[{platform}] PASS - ready to upload")
            passed_count += 1
        else:
            print(f"[{platform}] FAIL")
            for problem in problems:
                print(f"    - {problem}")
                
    print(f"\nSummary: This video is ready for {passed_count} out of {len(platform_rules)} platforms.")

def main():
    while True:                   #main interactive menu
        print("\n===================================")
        print("---MULTI-PLATFORM VIDEO CHECKER---")
        print("===================================")
        print("\n1. Check a video")
        print("2. Exit")
        
        choice = input("\nPick an option (1-2): ")

        if choice == "1":
            filename = input("What video file do you want to check? ")
            filename = filename.strip().strip('"').strip("'")
            if filename == "":
                print("You didn't enter a file name!")
                continue

            path = find_video_file(filename)
            if path is None:
                print(f"Error: could not find '{filename}' anywhere.")
                continue

            print(f"Found: {path}")

            details = get_video_details(path)
            if details is None:
                print("Could not read the video details from this file.")
                continue

            width, height, duration = details   #unpack info, width = details[0] and so on
            check_video_specs(filename, width, height, duration)

        elif choice == "2":
            print("Closing Program... Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1 or 2.")
            continue

main()
