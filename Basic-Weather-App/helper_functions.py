def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def convert_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_speed_to_kmh(speed):
    return speed * 3.6  # m/s to km/h

def handle_api_error(error_message):
    return f"Error fetching data: {error_message}"
