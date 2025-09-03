#news and weather

import sys
import os
import requests

#add utils path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.config import NEWS_API_KEY


#news fun
def get_news(topic="health"):
    url = f"https://newsapi.org/v2/top-headlines?category={topic}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)

        # Debug output
        print("API URL:", url)
        print("Response Status Code:", response.status_code)

        # Parse response JSON only after checking status
        data = response.json()
        print("Full API Response:", data)

        articles = data.get("articles", [])[:5]
        if not articles:
            return "Sorry boss, I could not find any news right now."
        news_list = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]
        return "Here are the top headlines: " + " ".join(news_list)
    except Exception as e:
        return f"Error fetching news: {str(e)}"

print(get_news())