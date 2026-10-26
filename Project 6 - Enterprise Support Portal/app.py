from flask import Flask, render_template, request, redirect, url_for   
# import Flask class and another tools
# request lets Flask catch the data from the form
#redirect and url_for let us send the user back to the homepage after submitting
import sqlite3

app = Flask(__name__)                       # creates a web app
                                                                  #__name__ tells Flask where the program is running

@app.route('/', methods=['GET', 'POST'])    # we use a decorator to set up a specific address 
                                                                                    # GET is for viewing the page, POST is for submitting the form
def home():                                 # runs the moment someone visits the homepage
    
    connection = sqlite3.connect("support_portal.db")   # connect to database
    cursor = connection.cursor()                        # create a cursor

    # if the form is submitted:
    if request.method == 'POST':
        # grab the data the user typed into the HTML form
        dept = request.form['department'].strip()   #.strip() prevents blank spaces from being accepted
        issue_desc = request.form['issue'].strip()
        priority = request.form['priority']
        
        if priority not in ["High", "Medium", "Low"]:       #this prevents user from using inspect element
            priority = "Medium"                                                #to input a priority not listed

        if dept == "" or issue_desc == "":      #if blank after stripping spaces
            cursor.execute("SELECT * FROM tickets")
            all_tickets = cursor.fetchall()
            connection.close()
            # We pass error_message="..." to the HTML
            return render_template("index.html", tickets=all_tickets, error_message="Error: Department and Issue cannot be blank!")
        
            # Add the new ticket to the SQL database in order
        cursor.execute("INSERT INTO tickets (department, issue, priority, status) VALUES (?, ?, ?, ?)", 
                       (dept, issue_desc, priority, "Open"))
        connection.commit()                             # save changes to the database
        connection.close()                              # close the connection
        
        # refresh webpage so the new ticket appears in the table immediately
        return redirect(url_for('home'))

    #on GET request, when not submitting form:
    cursor.execute("SELECT * FROM tickets")             # we retrieve all columns from the table
    all_tickets = cursor.fetchall()                     # grabs all results, turns it into a Python list, 
                                                                                # and saves it in all_tickets
    connection.close()                  # close the connection
    
    return render_template("index.html", tickets = all_tickets)   
    # return instead of print so it goes to the web page
    # finds index.html, reads the code, and prepares to send
    # we tell it 'tickets' stands for all the data in all_tickets

@app.route('/delete/<int:ticket_id>')
def delete_ticket(ticket_id):
    connection = sqlite3.connect("support_portal.db")
    cursor = connection.cursor()
    
    # The ticket_id comes directly from the URL (e.g., /delete/3)
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    
    connection.commit()
    connection.close()
    
    # Send the user right back to the homepage to see the updated table
    return redirect(url_for('home'))

if __name__== '__main__':                  # if running file directly
    app.run(debug=True, use_reloader=False)                     # run program, debug=True will show what went wrong if there is an error
                                                                                                            #use_reloader=False stops IDLE from freezing making and making
                                                                                                            #browser loading take forever
