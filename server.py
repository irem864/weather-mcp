import requests
from fastmcp import FastMCP
from dotenv import load_dotenv, find_dotenv
import os

_=load_dotenv(find_dotenv())

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

mcp = FastMCP("weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """
    Get the current weather for a city using OpenWeatherMap API.
    """
    params = {
        "q": city,
        "appid": os.environ["OPENWEATHER_API_KEY"],
        "units": "metric", 
        "lang": "tr"        
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return f"Hava durumu alınamadı! ({response.status_code})"

    data = response.json()
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    return f"{city} için hava durumu: {description}, sıcaklık: {temp}°C"

if __name__ == "__main__":
    mcp.run()
