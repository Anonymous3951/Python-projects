import time
import json
import os

def slow_print(text, delay=0): 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))     #finds folder where code is saved
SAVE_FILE = os.path.join(SCRIPT_DIR, "Studio_Equipment_Inventory.json")           #saves inventory to same folder

equipment_inventory = {
    "Sony 4K Camera": {"quantity": 2, "status": "Available"},
    "Led Light Panel": {"quantity": 1, "status": "In Use"},
    "Wireless Microphone": {"quantity": 3, "status": "Available"},
    "Tripod Stand": {"quantity": 5, "status": "Available"},
}
#creates a dictionary with each piece of information and its value as a mini dictionary with quantity and status 
#this is our sample inventory

def save_inventory(inventory):  
    with open(SAVE_FILE, "w") as file:  #opens file in write mode
        json.dump(inventory, file, indent=4) #dumps list into text file


def load_inventory():
    if os.path.exists(SAVE_FILE):   #does file already exist?
        with open(SAVE_FILE, "r") as file:  #opens in read mode
            return json.load(file)                  #reads text and turns back into python list
    else:
        save_inventory(equipment_inventory)  #if 1st time we call save_inventory function save deafult inventory
        return equipment_inventory             #and return values 

def display_inventory(inventory):
    slow_print("\n--- Current Studio Equipment List ---\n")
    for equipment, details in inventory.items():    # grabs each item and its status from inventory
        qty = details["quantity"]
        status = details["status"]
        slow_print(f"- {equipment} | Quantity: {qty} | Status: {status}")    # f allows us to plug the variables directly into text 


def add_new_item(inventory):
    slow_print("\nEnter the name of the new equipment: ")
    item = input().strip().title()     #.strip() removes accidental spaces at end and beginning 
    if item in inventory:     #checks to see if its already in inventory
        slow_print("That item is already in the inventory!")
        update_qty(inventory, item)
    else:
        slow_print("What is the status of item?")
        item_status = input().strip().title()  #takes status of new item
        try:
            slow_print("What is the quantity?")
            item_qty = int(input())
            if item_qty < 0:
                    slow_print("Quantity cannot be negative!")
            else:
                inventory[item] = {"quantity": item_qty, "status": item_status}     #add it to dictionary
                save_inventory(inventory)
                slow_print(f"Success! Added '{item}' as {item_status} x{item_qty}.")
        except ValueError:
            slow_print("Invalid input. Please enter a whole number.")

def remove_item(inventory):
    slow_print("\nWhich piece of equipment is no longer in inventory?")
    item = input().strip().title()
    if item in inventory:
        del inventory[item]
        slow_print(f"{item} was removed from inventory.")
        save_inventory(inventory)
    else:
        slow_print("That item is not in the inventory!")

def update_qty(inventory, item = None):
    if item is None:
        slow_print("\nEnter the name of the equipment to update quantity: ")
        item = input().strip().title()
    if item not in inventory:
        slow_print("That item is not in the inventory!")
        return
    current_qty = inventory[item]["quantity"]
    slow_print(f"Current quantity for {item}: {current_qty}")
    try:
        slow_print(f"Enter the new total quantity for {item}: ")
        new_qty = int(input())
        if new_qty < 0:
            slow_print("Quantity cannot be negative!")
        else:
            inventory[item]["quantity"] = new_qty
            save_inventory(inventory)
            slow_print(f"Success! Quantity for '{item}' updated to {new_qty}.")
    except ValueError:
        slow_print("Invalid input. Please enter a whole number.")

def update_status(inventory):
    slow_print("\nEnter the name of the equipment to update status: ")
    item = input().strip().title()
    if item in inventory:
        current_status = inventory[item]["status"]
        slow_print(f"Current status for '{item}': {current_status}")
        slow_print("Enter the new status (e.g., Available, In Use, Maintenance): ")
        new_status = input().strip().title()
        inventory[item]["status"] = new_status
        save_inventory(inventory)
        slow_print(f"Status for '{item}' updated to '{new_status}'.")
    else:
        slow_print("That item is not in the inventory!")


def main():

    inventory = load_inventory()
    
    while True:                             #always true so runs indefinitely 
        slow_print("\n==========================================")
        slow_print("STUDIO EQUIPMENT INVENTORY MANAGEMENT")
        slow_print("==========================================\n")
        slow_print("1. View all equipment")
        slow_print("2. Add new equipment to inventory")
        slow_print("3. Remove a piece of equipment from inventory")
        slow_print("4. Update quantity of a piece of equipment")
        slow_print("5. Update status of a piece of equipment")
        slow_print("6. Exit program")

        slow_print("\nPlease choose an option (1-6): ")
        choice = input().strip()

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            add_new_item(inventory)
        elif choice == "3":
            remove_item(inventory)
        elif choice == "4":
            update_qty(inventory)
        elif choice == "5":
            update_status(inventory)
        elif choice == "6":
            slow_print("\nExiting program. Goodbye!")
            break
        else:
            slow_print("\nInvalid choice. Please enter a number 1-6.")


main()
