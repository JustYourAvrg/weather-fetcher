import customtkinter as ctk
import requests
import json
import geocoder

from tkinter import messagebox

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class WeatherFetcher:
    def __init__(self):
        self.location = self.get_location()
        self.key = "YOUR_KEY_HERE"

    def get_location(self) -> str:
        try:
            g = geocoder.ip('me')
            return str(g)

        except Exception as e:
            messagebox.showerror("ERROR", f"{e}")
    

    def get_weather(self) -> str:
        try:
            url = "http://api.weatherapi.com/v1/current.json"
            request = requests.get(url, params={"key": f"{self.key}", "q": self.location})
            response = request.json()

            response_location = response["location"]["name"]
            response_country = response["location"]["country"]
            response_temp = response["current"]["temp_c"]
            response_condition = response["current"]["condition"]["text"]

            return response_location, response_country, response_temp, response_condition

        except Exception as e:
            messagebox.showerror("ERROR", f"{e}")
    

    def display_weather(self):
        try:
            location, country, temp, condition = self.get_weather()
            
            app = ctk.CTk()
            app.title("Weather Fetcher")
            app.geometry("300x100")
            app.resizable(False, False)

            location_label = ctk.CTkLabel(app, text=f"Location: {location}, {country}")
            location_label.pack(pady=10)

            temp_label = ctk.CTkLabel(app, text=f"Temperature: {temp}°C | {temp * 9/5 + 32}°F")
            temp_label.pack(pady=10)

            condition_label = ctk.CTkLabel(app, text=f"Condition: {condition}")
            condition_label.pack(pady=10)

            app.mainloop()

        
        except Exception as e:
            messagebox.showerror("ERROR", f"{e}")


if __name__ == "__main__":
    weather = WeatherFetcher()
    weather.display_weather()
