#news and weather

import sys
import os
import requests

#add utils path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.config import NEWS_API_KEY,WEATHER_API_KEY

#WEATHER FUN
import sys
import os
import requests

# Add utils path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.config import WEATHER_API_KEY  # Make sure this is defined properly

def get_weather(city="nadiad"):
    try:
        # Step 1: Get lat/lon using geocoding API
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_API_KEY}"
        geo_response = requests.get(geo_url).json()
        if not geo_response:
            return "Sorry, boss. Couldn't find the location."

        lat = geo_response[0]['lat']
        lon = geo_response[0]['lon']

        # Step 2: Use lat/lon to get weather
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
        weather_response = requests.get(weather_url).json()

        if weather_response.get("cod") != 200:
            return "Sorry, boss. I could not fetch the weather."

        temp = weather_response["main"]["temp"]
        desc = weather_response["weather"][0]["description"]
        return f"The temperature in {city.title()} is {temp}°C with {desc}."

    except Exception as e:
        return f"Error fetching weather: {str(e)}"


#news fun
def get_news(topic="health"):
    url = f"https://newsapi.org/v2/top-headlines?category={topic}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)

        # Parse response JSON only after checking status
        data = response.json()

        articles = data.get("articles", [])[:5]
        if not articles:
            return "Sorry boss, I could not find any news right now."
        news_list = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]
        return "Here are the top headlines: " + " ".join(news_list)
    except Exception as e:
        return f"Error fetching news: {str(e)}"
print(get_weather())