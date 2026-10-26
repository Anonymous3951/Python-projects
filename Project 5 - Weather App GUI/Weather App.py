import tkinter as tk    #library for creating GUIs
import requests     ##allows python to reach out to internet and grab info at a certain URL

API_KEY = "PASTE_YOUR_API_KEY_HERE"    #API key stored as constant

def get_weather():
    city = city_entry.get()     #extract what the user typed
    
    if city == "":  #guard clause
        result_label.config(text="Please enter a city name!")
        return
        
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"  #the URL the request is sent to
    
    try:
        response = requests.get(url)    #download servers response 
        data = response.json()              #convert response into python dictionary
        
        if data["cod"] == 200:                  #check if request was successful, cod 200 means "OK"
            temp = data["main"]["temp"]     #grabs main data from dictionary and temp from inside that
            condition = data["weather"][0]["description"].title()   #returns weather list, retrieves 1st item and description inside

            result_label.config(text=f"{temp}°C | {condition}")     #change the text on screen, config is like print
        else:
            result_label.config(text="City not found. Please try again.")   #if not a city
    except:
        result_label.config(text="Network error. Check your internet.")     #if network error

window = tk.Tk()    #creates the actual window box
window.title("My Weather App")  #sets title right at the top
window.geometry("300x250") # sets size of the window in pixels 

title_label = tk.Label(window, text="Weather Checker", font=("Arial", 16, "bold"))  #creates piece of text
title_label.pack(pady=10)   #stacks items vertically, 10 pixels above and below 

city_entry = tk.Entry(window, font=("Arial", 12), justify="center")     #text box where user types, justify=centre make its centred
city_entry.pack(pady=5)

search_button = tk.Button(window, text="Get Weather", font=("Arial", 12), command=get_weather)  #makes clickable button
search_button.pack(pady=10)                                                                                                                                     #runs only when clicked

result_label = tk.Label(window, text="Enter a city above", font=("Arial", 14))  #creates label that is later changed 
result_label.pack(pady=20)

window.mainloop()   #keeps window open
