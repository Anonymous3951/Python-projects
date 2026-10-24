import json     #text format that looks like python lists & dictionaries, so we can save tickets & read them back later
import os       #interact with folders and file paths

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))     #finds folder where code is saved
SAVE_FILE = os.path.join(SCRIPT_DIR, "tickets.json")           #saves tickets to same folder


#below is some sample ticket data storted in a list, within the list is 4 dictionaries storing data in key:value pairs
default_tickets = [
    {"id": "TICK-101", "user": "Warehouse Team", "issue": "Barcode scanner software crashing", "priority": "High"},
    {"id": "TICK-102", "user": "Finance Dept", "issue": "Excel report export timing out", "priority": "Medium"},
    {"id": "TICK-103", "user": "Supply Chain", "issue": "Database query failing to update delivery", "priority": "High"},
    {"id": "TICK-104", "user": "HR", "issue": "Password reset request", "priority": "Low"}
]


def save_tickets(tickets):  
    with open(SAVE_FILE, "w") as file:  #opens file in write mode
        json.dump(tickets, file, indent=4) #dumps list into text file


def load_tickets():
    if os.path.exists(SAVE_FILE):   #does file already exist?
        with open(SAVE_FILE, "r") as file:  #opens in read mode
            return json.load(file)                  #reads text and turns back into python list
    else:
        save_tickets(default_tickets)  #if 1st time we call save_tickets function save deafult tickets
        return default_tickets             #and return values 


def display_all_tickets(tickets):
    print("\n--- ALL SUPPORT TICKETS ---")
    if len(tickets) == 0:
        print("No tickets in the system.")
        return

    for ticket in tickets:
        print(f"[{ticket['id']}] {ticket['priority']} | {ticket['user']}")
        print(f"     Issue: {ticket['issue']}")         #on separate line as may be much longer, more presentable


def add_new_ticket(tickets):
    print("\n--- CREATE NEW TICKET ---")
    user = input("Enter department (e.g., Sales, IT): ").strip().title()
    if user in ["It", "Hr", "Pr", "Qa", "Ops"]:
        user = user.upper()
        
    issue = input("Enter the issue description: ").strip()
    priority = input("Enter priority (High / Medium / Low): ").strip().title()

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Defaulting to 'Medium'.")
        priority = "Medium"

    if len(tickets) == 0:
        new_id = "TICK-101"
    else:
        last_id = tickets[-1]["id"]                         #identify the last ticket made
        last_number = int(last_id.split("-")[1])    #cut it at the dash, take second item (the number) and make it an integer 
        new_id = f"TICK-{last_number + 1}"     #then we add 1 to it, getting the next number along 

    new_ticket = {"id": new_id, "user": user, "issue": issue, "priority": priority}
    tickets.append(new_ticket) #adds the new dictionary for the ticket to the list
    save_tickets(tickets)
    print(f"Ticket {new_id} created and saved successfully.")


def delete_ticket(tickets):
    print("\n--- DELETE A TICKET ---")
    ticket_id = input("Enter the Ticket ID to delete (e.g., TICK-101): ").strip().upper()

    found_ticket = None
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            found_ticket = ticket
            break

    if found_ticket:    #as in if not none
        confirmation = input(f"Are you sure you want to delete {ticket_id}? (yes/no)").strip().lower()
        if confirmation == "yes":
            tickets.remove(found_ticket)
            save_tickets(tickets)
            print(f"\nSuccess! Ticket {ticket_id} has been permanently deleted.")
        else:
            print(f"\nTicket {ticket_id} has not been deleted")            
    else:
        print(f"Error: Ticket {ticket_id} not found. Please check the ID and try again.")


def analyse_tickets(tickets):
    print("\n==========================================")
    print("       IT SUPPORT & ERROR LOG ANALYSIS")
    print("==========================================")

    high_count = 0
    med_count = 0
    low_count = 0
    escalated_issues = []

    for ticket in tickets:
        if ticket["priority"] == "High":
            high_count += 1
            escalated_issues.append(ticket)
        elif ticket["priority"] == "Medium":
            med_count += 1
        elif ticket["priority"] == "Low":
            low_count += 1

    print(f"\nTotal Tickets Processed: {len(tickets)}")
    print(f"High Priority:   {high_count}")
    print(f"Medium Priority: {med_count}")
    print(f"Low Priority:    {low_count}\n")

    if high_count == 0:
        print("No high-priority issues. Systems are stable.")
    else:
        print("--- ACTION REQUIRED: ESCALATED TICKETS ---")
        for item in escalated_issues:
            print(f"- [ID: {item['id']}] Dept: {item['user']}")
            print(f"  Issue: {item['issue']}")
            print("  Status: Flagged for immediate developer investigation.\n")


def main():
    tickets = load_tickets()

    while True: 
        print("\n==========================================")
        print("       IT SUPPORT TICKET MANAGER")
        print("==========================================")
        print("1. View All Tickets")
        print("2. Add New Ticket")
        print("3. Delete Existing Ticket")
        print("4. Run Priority Analysis")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            display_all_tickets(tickets)
        elif choice == "2":
            add_new_ticket(tickets)
        elif choice == "3":
            delete_ticket(tickets)
        elif choice == "4":
            analyse_tickets(tickets)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


main()
