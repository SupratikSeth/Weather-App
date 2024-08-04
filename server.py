from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/weather')
def get_weather():
    city = request.args.get("city")

    #check for empty string or string with spaces
    city = city.strip()
    if not bool(city):
        city = "Kolkata"
    results = get_current_weather(city)

    if not results['cod'] == 200:
        return render_template("city-not-found.html")

    return render_template(
        "weather.html",
        title = results['name'],
        status = results['weather'][0]['description'].capitalize(),
        temp = f"{results['main']['temp']:.1f}",
        feels_like = f"{results['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=7000)