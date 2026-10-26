import sqlite3  #SQL library for SQL databases, just as JSON is for text files

connection = sqlite3.connect("support_portal.db")   #opens connection to a database file, if non-existent, it will create one
cursor = connection.cursor()    #create a cursor 

#next we give commands using.execute()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        department TEXT,
        issue TEXT,
        priority TEXT,
        status TEXT
    )
""")        #if there isnt one already, it creates a table with columns for ID ( which is an integer and has unique ID 
               #which is automatically assigned), and also columns for department, issue, priority and status (all text)

cursor.execute("SELECT COUNT(*) FROM tickets")
ticket_count = cursor.fetchone()[0]

# Only insert the sample tickets if the table is empty (first time running)
if ticket_count == 0:
    cursor.execute("INSERT INTO tickets (department, issue, priority, status) VALUES (?, ?, ?, ?)",     #insert a new row
                   ("Warehouse", "Barcode scanner offline", "High", "Open"))                                                           #with these values 
    cursor.execute("INSERT INTO tickets (department, issue, priority, status) VALUES (?, ?, ?, ?)",    #tuple fills question marks
                   ("Logistics", "ERP delivery ETA not syncing", "Medium", "Open"))                                             #in the exact same order

connection.commit()             #we basically press save

cursor.execute("SELECT * FROM tickets")     #we retrieve all columns from the table
all_tickets = cursor.fetchall()                               #grabs all results and turns into a python list

print("--- DATA FROM THE SUPPORT PORTAL ---")
for ticket in all_tickets:                  #loop through tuples, so its one at a time
    print(ticket)                                   #print them one at a time, looks neater then printing all at once

connection.close()              #safely close file and connection
