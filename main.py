import requests

api_key = "8e19eef1243f4f0fbd5367901ce0eb37"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
    "2025-05-03&sortBy=publishedAt&apiKey=" \
    "8e19eef1243f4f0fbd5367901ce0eb37"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

# Exercise/challenge: send these titles and articles to my email address
# use code from the portfolio app