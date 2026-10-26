import requests     #allows python to reach out to internet and grab info at a certain URL

API_KEY = "PASTE_YOUR_API_KEY_HERE"    #API key stored as constant

city = "Birmingham, UK"     #store city in variable, UK specifies which birmingham
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"  #the URL the request is sent to

print(f"Connecting to weather server for {city}...")

response = requests.get(url)    #stores weather info in variable

data = response.json()  #raw text is translated into python dictionary

if data["cod"] == 200:  #check if request was successful, cod 200 means "OK"
    
    temp = data["main"]["temp"]     #grabs main data from dictionary and temp from inside that
    condition = data["weather"][0]["description"]   #returns weather list, retrieves 1st item and description inside
    humidity = data["main"]["humidity"]     #grabs main data from dictionary and temp from inside that
    city_name = data["name"]    #returns country name
    country = data["sys"]["country"]    #gets country code from sys dictionary

        #then we print our findings 
    print(f"Weather in {city_name}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {condition.title()}")
    print(f"Humidity: {humidity}%")
    
else:   #if code not 200, dictionary with error message is sent back
    print("Error:", data["message"])    #error message displayed
