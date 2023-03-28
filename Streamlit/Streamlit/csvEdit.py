import streamlit as st
import pandas as pd

st.title('News App')


col1, col2 = st.columns([1,4])      #칸 길이 조정
with col1:
    user = st.text_input('Enter Country Name')

with col2:
    category = st.radio('Choose a news category', ('Technology', 'Politics', 'Sports', 'Business'))
    btn = st.button('Enter')



if btn:
    #country = pycountry.countries.get(name=user).alpha_2
    df = pd.read_csv("movies.csv")
    #df = df.json()
    genres = df['genres'][10]
    budget = df['budget']
    homepage = df['homepage']
    keywords = df['keywords']
    st.write("장르: ", genres)
    st.write("요약: ", keywords) 
    st.write("예산: ", budget)
    st.write("홈페이지: ", homepage)
        