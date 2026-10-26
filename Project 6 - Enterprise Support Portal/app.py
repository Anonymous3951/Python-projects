from flask import Flask, render_template    #import Flask class and also another tool
                                                                                   #to connect our code to HTML files 
import sqlite3

app = Flask(__name__)         #creates a web app, __name__ tells Flask where the program is running

@app.route('/')     #we use decorator to set up a specific address 
def home():           #runs the moment someone visits the homepage
    connection = sqlite3.connect("support_portal.db")   #connect to database
    cursor = connection.cursor()                                             #create a cursor
    
    cursor.execute("SELECT * FROM tickets")     #we retrieve all columns from the table
    all_tickets = cursor.fetchall()                               #grabs all results and turns into a python list
                                                                                           #and save in all_tickets
    connection.close()                      #close the connection
    
    return render_template("index.html", tickets = all_tickets)   #return instead of print so it goes to web browser
                                                                                                                     #finds index.html, reads code and prepares to send
                                                                                                                    #we tell it tickets stand for all the data in all_tickets

if __name__ == '__main__':          #if running file directly
    app.run(debug=True)             #run program, debug=true will show what went wrong if error
