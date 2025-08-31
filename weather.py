import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Current temperature in {city}: {temp}°C")
        print(f"Weather description: {desc}")
    else:
        print("Failed to get weather information. Please check your city name or API key.")

city = input("Enter city name: ")
api_key = input("Enter your OpenWeatherMap API key: ")
get_weather(city, api_key)
