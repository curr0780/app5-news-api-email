import requests
import streamlit as st

# make the api call
nasa_api_key = "" # removed for push to git
url = ("https://api.nasa.gov/planetary/apod?"
       "api_key=") # add key here as well
request = requests.get(url)
content = request.json()
#print(content)
for key in content:
    print(f"{key}, {content[key]}")

# set up website basics
st.set_page_config(layout="wide")
st.title("NASA Astronomy Image of the Day")
st.title(content['title'])
st.image(content['url'], use_column_width=True)
st.write(content['explanation'])
