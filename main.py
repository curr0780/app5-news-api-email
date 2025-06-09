import requests
import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "curr0780@gmail.com"
    password = ""
    receiver = "curr0780@gmail.com"
    context = ssl.create_default_context()

    with open('news-today.txt', 'w', encoding='utf-8') as file:
        file.writelines(message)

    # with smtplib.SMTP_SSL(host, port, context=context) as server:
    #     server.login(username, password)
    #     server.sendmail(username, receiver, message)


topic = "Hawaii"
api_key = "" #removed for push to git
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-05-06&"
       "sortBy=publishedAt&apiKey=") # add key here as well

request = requests.get(url)
content = request.json()
print(type(content))

message_body = ""
for article in content['articles'][:10]:
    message_body = (message_body +
                    article['title'] + "\n")
# for index, article in enumerate(content["articles"][:10]):
#     message_body = message_body + article['title'] + "\n" article['description'] + "\n" + article['url'] + 2*"\n"

#message_body = message_body.encode("utf-8")
print(message_body)
# send_email(message_body)

# Exercise/challenge: send these titles and articles to my email address
# use code from the portfolio app
