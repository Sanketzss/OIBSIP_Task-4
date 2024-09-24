import os
import requests

# List of all icon codes from OpenWeatherMap
icon_codes = [
    "01d", "01n", "02d", "02n", "03d", "03n", "04d", "04n",
    "09d", "09n", "10d", "10n", "11d", "11n", "13d", "13n", "50d", "50n"
]

# Base URL for downloading icons
base_url = "https://openweathermap.org/img/wn/"

# Directory to save the icons
icon_dir = "weather_icons"

# Create the directory if it doesn't exist
if not os.path.exists(icon_dir):
    os.makedirs(icon_dir)

# Download each icon
for icon in icon_codes:
    url = f"{base_url}{icon}@2x.png"  # 2x size for better quality
    response = requests.get(url)

    if response.status_code == 200:
        # Save the icon in the specified directory
        with open(f"{icon_dir}/{icon}.png", "wb") as file:
            file.write(response.content)
        print(f"Downloaded {icon}.png")
    else:
        print(f"Failed to download {icon}.png")
