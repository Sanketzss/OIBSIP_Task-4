import tkinter as tk
from tkinter import messagebox
from weather_api import fetch_weather_data
from helper_functions import handle_api_error
from PIL import Image, ImageTk


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Weather App")
        self.root.geometry("400x500")

        # Labels and Entry for city input
        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.pack(pady=10)
        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.pack(pady=5)

        # Button to get weather data
        self.fetch_btn = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.fetch_btn.pack(pady=10)

        # Labels to display weather data
        self.weather_icon_label = tk.Label(root)
        self.weather_icon_label.pack(pady=10)

        self.weather_info_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.weather_info_label.pack(pady=10)

        # Unit toggle (Celsius/Fahrenheit)
        self.unit_var = tk.StringVar(value="metric")
        self.unit_toggle_btn = tk.Button(root, text="Switch to Fahrenheit", command=self.toggle_units)
        self.unit_toggle_btn.pack(pady=10)

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            data = fetch_weather_data(city, self.unit_var.get())
            if data:
                self.display_weather(data)
            else:
                messagebox.showerror("Error", handle_api_error("Invalid city or API issue"))
        else:
            messagebox.showerror("Input Error", "Please enter a city name")

    def display_weather(self, data):
        city = data['name']
        temp = data['main']['temp']
        weather_condition = data['weather'][0]['main']
        icon = data['weather'][0]['icon']

        # Print the icon code to debug
        print(f"Icon code: {icon}")

        wind_speed = data['wind']['speed']

        weather_text = f"City: {city}\nTemperature: {temp}°\nCondition: {weather_condition}\nWind Speed: {wind_speed} m/s"
        self.weather_info_label.config(text=weather_text)

        self.display_icon(icon)

    def display_icon(self, icon_code):
        # Map icon code to local file
        icon_path = f"weather_icons/{icon_code}.png"

        try:
            img = Image.open(icon_path)
            img = img.resize((100, 100), Image.LANCZOS)  # Updated to Image.LANCZOS
            img_tk = ImageTk.PhotoImage(img)
            self.weather_icon_label.config(image=img_tk)
            self.weather_icon_label.image = img_tk  # Keep reference to avoid garbage collection
        except Exception as e:
            print(f"Error loading icon '{icon_code}.png': {e}")
            self.weather_icon_label.config(text="No Icon Available")  # Show text if icon fails

    def toggle_units(self):
        if self.unit_var.get() == "metric":
            self.unit_var.set("imperial")
            self.unit_toggle_btn.config(text="Switch to Celsius")
        else:
            self.unit_var.set("metric")
            self.unit_toggle_btn.config(text="Switch to Fahrenheit")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
