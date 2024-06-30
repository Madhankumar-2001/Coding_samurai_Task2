# Weather forecast using python Coding_samurai_Task2
**Task-2**

*******************************
Project Title: Weather Forecast Application  
**************************************
## Overview

This project is a simple command-line weather forecast application in Python, designed to provide users with current weather information for a specified location. It fetches weather data from the OpenWeatherMap API and displays it in a user-friendly format.

### How to Run

1. **Clone the Repository:**
   ```sh
   git clone (repository-url)
   cd (repository-directory)
   ```

2. **Install Dependencies:**
   pip install requests
   
4. **Run the Application:**
   python <filename>.py


### Code Explanation

1. **Imports:**
   - `import requests`: For making HTTP requests to the weather API.

2. **Function to Fetch Weather Data:**
   - `def get_weather(api_key, city, units="metric")`: Fetches weather data for the specified city and units from the OpenWeatherMap API.
     - Constructs the API URL with the city, API key, and units (metric for Celsius, imperial for Fahrenheit).
     - Sends a GET request to the API.
     - Returns the JSON response.

3. **Function to Display Weather Data:**
   - `def display_weather(data, units)`: Displays the fetched weather data in a readable format.
     - Checks if the API response is successful (`cod` 200).
     - Extracts relevant information (city name, temperature, humidity, wind speed, weather description).
     - Determines the units for temperature and wind speed based on the user's choice.
     - Prints the weather information.

4. **Main Function:**
   - `def main()`: The main function that runs the application.
     - Prompts the user for the city name.
     - Asks the user to choose temperature units (C for Celsius, F for Fahrenheit).
     - Fetches the weather data using `get_weather()`.
     - Displays the weather data using `display_weather()`.

5. **Run the Main Function:**
   - `if __name__ == "__main__":`: Ensures the main function runs only when the script is executed directly.

### Features

- **Fetch Weather Data:** Retrieves current weather information for any city using the OpenWeatherMap API.
- **Display Weather Data:** Presents the weather data in a user-friendly format, including temperature, humidity, wind speed, and weather conditions.
- **Unit Conversion:** Supports both Celsius and Fahrenheit for temperature, and meters/sec and miles/hour for wind speed.

### Usage

1. **Enter City Name:** Input the name of the city for which you want to fetch weather information.
2. **Choose Units:** Select temperature units (C for Celsius, F for Fahrenheit).
3. **View Weather Data:** The application will display the current weather details for the specified city.

### Example

Enter the city name: London
Choose units for temperature (C for Celsius, F for Fahrenheit): C
Weather in London:
Temperature: 15° Celsius

