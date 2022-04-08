from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    API_KEY = request.form.get("api_key")
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    city = request.form.get("city")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        x = f'Weather: {weather.capitalize()}'
        temperature = round(data["main"]["temp"] - 273.15, 2)
        y = f'Temperature: {str(temperature)} \N{DEGREE SIGN}C'
        answer = [x , y]
        return render_template("result.html", ans=answer)
    else:
        return render_template("error.html")