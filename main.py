#Program to fetch real time weather and temperature in degree celcius from openweathermap.org using API.
import requests

#Get your API key from https://openweathermap.org/api to get access to the data.
api_key = input("Enter your API key: ")
API_KEY = api_key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#Getting location to show weather for.
city = input("Enter City: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

#If the request is satisfied with code 200 (ok) then do the necessary. 'data' gets all the data from the jason file.
#data is trimmed to show what is required.
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather:", weather.capitalize())
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(f"Temperature: " + str(temperature) + "\N{DEGREE SIGN}" + " C")
else:
    print("An error occured!")