import requests
import datetime as dt


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


API_KEY = "6dd962b4bf9e8166cd734dcb38b32dae"


CITY = input("Enter the name of the city: ")


url = f"{BASE_URL}q={CITY}&appid={API_KEY}"


print(f"URL: {url}")


response = requests.get(url)


if response.status_code == 200:

    data = response.json()


    def kelvin_to_celsius_fahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit


    temp_kelvin = data["main"]["temp"]
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

    feels_like_kelvin = data["main"]["feels_like"]
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    wind_speed = data["wind"]["speed"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    sunrise_time = dt.datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"])
    sunset_time = dt.datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"])


    print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
    print(f"Humidity in {CITY}: {humidity}%")
    print(f"Wind speed in {CITY}: {wind_speed} m/s")
    print(f"General weather in {CITY}: {description}")
    print(f"Sun rises in {CITY} at {sunrise_time} local time")
    print(f"Sun sets in {CITY} at {sunset_time} local time")
else:

    print("Error:", response.status_code, response.json().get("message", "No message"))
