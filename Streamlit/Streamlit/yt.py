import streamlit as st
import requests
import pycountry
#from api import apikey
#0c782178639a47a78e65a9e2e4208828

st.title('News App')


col1, col2 = st.columns([1,4])      #칸 길이 조정
with col1:
    user = st.text_input('Enter Country Name')

with col2:
    category = st.radio('Choose a news category', ('Technology', 'Politics', 'Sports', 'Business'))
    btn = st.button('Enter')

if btn:
    #country = pycountry.countries.get(name=user).alpha_2
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=0c782178639a47a78e65a9e2e4208828"
    r = requests.get(url)
    r = r.json()
    articles = r['articles']
    for article in articles:
        st.header(article['title'])
        st.markdown(f"<span style='background-color:grey;'> Published at: {article['publishedAt']}</span>", unsafe_allow_html=True)
        if article['author']:
            st.write("Author: ", article['author'])
        st.write("Source: ", article['source']['name'])
        st.write("Summary",article['description'])
        st.image(article['urlToImage'])
