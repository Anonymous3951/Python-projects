import os   #used to interact with files
import shutil   #used to copy or move files around


target_name = input("What folder do you want to organise?").strip().strip('"').strip("'")      #looks for the folder you want to clean up

target_directory = target_name

if not os.path.exists(target_directory):    #checks folder exist at intial path
    print(f"Searching your computer for '{target_name}'... Please wait.")
    home_dir = os.path.expanduser("~")      #finds main account folder
    for root, dirs, files in os.walk(home_dir):
        if target_name in dirs:
            target_directory = os.path.join(root, target_name)
            break       #used to exit loops

def organise_files():   #puts all the cleaning instructions into function "organise_files" 
    if not os.path.exists(target_directory):    #checks to see if folder is found 
        print(f"Error: The folder '{target_directory}' could not be found.") #if not found error message sent 
        return  #ends the function


    items = os.listdir(target_directory)    #folder is searched and list of contents stored in "items"

    for item in items:  #goes through every item 
        full_path = os.path.join(target_directory, item)    #finds exact address of item
        if os.path.isdir(full_path):    #checks if it is a folder
            continue    #skips to next item inside loop
        if "." in item:     #chops file name wherever there is a dot to separate the file type
            file_extension = item.split(".")[-1].lower()    #isolates last the extension (last segment if more than one dot) and assigns it to "file extension"
        else:
            continue 


        if file_extension in ["mp4", "mov", "avi", "mkv"]:  #checks if video
            folder_name = "Videos"
        elif file_extension in ["jpg", "jpeg", "png", "gif"]:   #checks if image
            folder_name = "Images"
        elif file_extension in ["mp3", "wav", "aac" , "m4a"]:   #checks if audio
            folder_name = "Audio"
        elif file_extension in ["txt"]:
            folder_name = "Notes"
        else:
            folder_name = "Documents_and_Others"


        subfolder_path = os.path.join(target_directory, folder_name)
        if not os.path.exists(subfolder_path):  #checks if folder already exists, if first time it will create
            os.makedirs(subfolder_path) 


        destination_path = os.path.join(subfolder_path, item)
        shutil.move(full_path, destination_path)    #moves file to new destination
        print(f"Moved: {item} ---> {folder_name}/")

    print("All files have been successfully organised!")


organise_files()
