#news and weather

import requests


#news fun
def get_news(topic="technology"):
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={topic}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url).json()
        articles = response.get("articles", [])[:5]
        if not articles:
            return "Sorry boss, I could not find any news right now."
        news_list = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]
        return "Here are the top headlines: " + " ".join(news_list)
    except Exception as e:
        return f"Error fetching news: {str(e)}"