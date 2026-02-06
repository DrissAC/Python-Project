import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY_METEO = os.getenv("API_KEY_METEO")

API_KEY = API_KEY_METEO
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data["name"],
                "Temperature": f"{data["main"]["temp"]}°C",
                "Weather": data["weather"][0]["description"].title(),
                "Humidity": f"{data["main"]["humidity"]}%",
                "Wind Speed": f"{data['wind']['speed']} m/s"
            }
            return weather
        elif response.status_code == 404:
            print("Ville introuvable.")
        else:
            print("Une erreur s'est produite lors de la requête : ", response.status_code)
    except Exception as e:
        print("Une erreur s'est produite lors de la requête : ", e)
    return None

def display_weather(weather):
    print(f"\n--- Météo pour {weather['City']} ---")
    for key, value in weather.items():
        print(f"{key}: {value}")

while True:
    print("\n--- Application Meteo ---")
    city = input("Entrez le nom de la ville : (ou 'q' pour quitter) ")
    if city.lower() == "q":
        break
    weather = get_weather(city)
    if weather:
        display_weather(weather)