import requests
import customtkinter as cc
from PIL import Image, ImageFilter

api_key = "api_key_here"  # Replace with your OpenWeatherMap API key


def get_weather():
    city = city_entry.get()
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    temp = data['main']['temp']
    weather_desc = data['weather'][0]['description'].capitalize()
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    result = f"Temperature: {temp}°C\nDescription: {weather_desc} \nHumidity: {humidity}%\nWind Speed: {wind} m/s "
    label_result.configure(text=result, fg_color="transparent")
    label_result.pack(pady=10)


app = cc.CTk()
app.geometry("400x300")
app.title("Weather App")


label = cc.CTkLabel(app, text="weather App", font=(
    "Arial", 20), fg_color="transparent", text_color="#ffffff")
label.pack(pady=20)

city_entry = cc.CTkEntry(app, placeholder_text="Enter city name")
city_entry.pack(pady=10)
btn_search = cc.CTkButton(app, text="Get Weather", command=get_weather)
btn_search.pack(pady=20)

label_result = cc.CTkLabel(app, text="", font=(
    "Arial", 14), fg_color="transparent")

label_result.pack(pady=10)


app.mainloop()
