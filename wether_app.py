import requests

def get_weather(city):
    api_key = "9017844f5234cab6acc85ce8c3f347dc"  # Replace with your key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    # Debugging output
    if "main" not in data:
        print("⚠️ Something went wrong! Here's what the API returned:")
        print(data)
        return

    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]

    print(f"\n🌆 City: {city}")
    print(f"🌡️ Temperature: {main['temp']}°C")
    print(f"💧 Humidity: {main['humidity']}%")
    print(f"🌤️ Weather: {weather['description'].capitalize()}")
    print(f"🌬️ Wind Speed: {wind['speed']} m/s")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
