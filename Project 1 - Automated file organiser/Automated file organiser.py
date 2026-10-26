import os   #used to interact with files
import shutil   #used to copy or move files around

EXTENSIONS = {
    "Videos": ["mp4", "mov", "avi", "mkv"],
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Audio": ["mp3", "wav", "aac" , "m4a"],
    "Notes": ["txt"],
    "Documents": ["pdf", "docx", "xlsx"],
    "Archives": ["zip"]
}

print ("============================================\n--------------- Automated File Organiser ---------------\n============================================\n")

target_name = input("What folder do you want to organise?").strip().strip('"').strip("'")    #looks for the folder you want to clean up

target_directory = target_name

if not os.path.exists(target_directory):    #checks if folder exists at intial path given
    print(f"Searching your computer for '{target_name}'... Please wait.")
    home_dir = os.path.expanduser("~")      #finds main account folder
    wanted = target_name.lower()
    found = False
    for root, dirs, files in os.walk(home_dir):
        for d in dirs:
            if d.lower() == wanted:
                found = True
                target_directory = os.path.join(root, d)
                break       #used to exit loops
        if found:
            break

def organise_files():   #puts all the cleaning instructions into function "organise_files" 
    if not os.path.exists(target_directory):    #checks to see if folder is found 
        print(f"Error: The folder '{target_directory}' could not be found.") #if not found error message sent 
        return  #ends the function


    items = os.listdir(target_directory)    #folder is searched and list of contents stored in "items" 

    moved_count = 0
    for item in items:  #goes through every item (each item is a file in the original folder)
        full_path = os.path.join(target_directory, item)    #finds exact address of item
        if os.path.isdir(full_path):    #checks if it is a folder
            continue    #skips to next item inside loop
        name, ext = os.path.splitext(item) #splits file name and extension
        ext =ext.lower().replace(".", "")   #replaces the dot in the extension with nothing, eg. ".mp4" becomes "mp4"

        folder_name = "Others"
        for category, ext_list in EXTENSIONS.items():
            if ext in ext_list:
                folder_name = category 
                break

        subfolder_path = os.path.join(target_directory, folder_name)
        if not os.path.exists(subfolder_path):  #checks if folder already exists, if first time it will create
            os.makedirs(subfolder_path)
            

        destination_path = os.path.join(subfolder_path, item)
        if os.path.exists(destination_path): #checks to see if name already exists, so files are not accidentally replaced 
            counter = 1
            while os.path.exists(destination_path):
                new_name = f"{name} ({counter}).{ext}" #automatically makes a new name
                destination_path = os.path.join(subfolder_path, new_name) #and uses it to make the new path
                counter += 1
                
        shutil.move(full_path, destination_path)    #moves file to new destination
        print(f"Moved: {item} ---> {folder_name}/")
        moved_count += 1

    print(f"\nFinished! {moved_count} files have been organised \nAll files have been successfully organised!")


organise_files()
