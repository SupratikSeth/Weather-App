import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city = "Kolkata"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    
    result = requests.get(request_url).json()

    return result

if __name__ == "__main__":
    city = input("Enter a city: \n")

    #check for empty string or string with spaces
    if not bool(city.strip()):
        city = "Kolkata"
    result = get_current_weather(city)

    pprint(result)
