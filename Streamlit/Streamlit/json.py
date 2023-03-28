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
    df = pd.read_json("train.json")
    #df = df.json()
    st.write("제목: ", df['version','data']['title'])
    # paras = df['data']['paragraphs']
    # for para in paras:
        
    #     st.markdown("문장: ", para['context'])
    #     st.write("질문: ", para['qas']['question'])
    #     st.write("답변", para['qas']['answers']['text'])
        
