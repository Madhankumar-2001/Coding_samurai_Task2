import requests

def get_weather(api_key, city, units="metric"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)
    return response.json()

def display_weather(data, units):
    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return
    
    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather_description = data["weather"][0]["description"]

    temp_unit = "Celsius" if units == "metric" else "Fahrenheit"
    wind_unit = "meters/sec" if units == "metric" else "miles/hour"

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}° {temp_unit}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} {wind_unit}")
    print(f"Condition: {weather_description.capitalize()}")

def main():
    api_key = "8fb9b76d2c2d754896174f9dc973871a"  # Replace with your actual API key
    city = input("Enter the city name: ")
    unit_choice = input("Choose units for temperature (C for Celsius, F for Fahrenheit): ").strip().upper()
    units = "metric" if unit_choice == "C" else "imperial"

    weather_data = get_weather(api_key, city, units)
    display_weather(weather_data, units)

if __name__ == "__main__":
    main()

