import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.write('# 종목추천')
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Low risk Low return", "종목명1", "종가1")
col2.metric("Low risk Low return", "종목명2", "종가2")
col3.metric("Low risk Low return", "종목명3", "종가3")
col4.metric("Low risk Low return", "종목명4", "종가4")
col5.metric("Low risk Low return", "종목명5", "종가5")

st.write('# 종목추천')
col6, col7, col8, col9, col10 = st.columns(5)
col6.metric("Low risk Low return", "종목명6", "종가6")
col7.metric("Low risk Low return", "종목명7", "종가7")
col8.metric("Low risk Low return", "종목명8", "종가8")
col9.metric("Low risk Low return", "종목명9", "종가9")
col10.metric("Low risk Low return", "종목명10", "종가10")




tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


# view = [100, 150, 30]
# st.write('# Youtube view')
# st.write('## raw')
# st.write('# 구름팀')

# view

# st.write('## bar chart')
# st.bar_chart(view)

# sview = pd.Series(view)
# st.write('# pandas view')
# sview