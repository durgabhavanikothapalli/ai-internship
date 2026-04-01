import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("WEATHER_API")

params = {
    "latitude": 27.7172,
    "longitude": 85.3240,
    "daily": "temperature_2m_max",
    "timezone": "auto"
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    
    dates = data["daily"]["time"]
    temps = data["daily"]["temperature_2m_max"]
    
    # Save weather.csv
    with open("weather.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["date", "max_temp"])
        
        for i in range(len(dates)):
            writer.writerow([dates[i], temps[i]])
    
    # Find hottest day
    max_temp = max(temps)
    index = temps.index(max_temp)
    
    print("Hottest Day:", dates[index])
    print("Temperature:", max_temp)

else:
    print("Failed to fetch weather data")