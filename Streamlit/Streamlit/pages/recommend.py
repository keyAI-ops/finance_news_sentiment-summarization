import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

today = date.today()

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

st.set_page_config(page_title="종목추천", page_icon="📈")

if st.button("Home으로 돌아가기"):
    nav_page("home")
st.image('ai_robot.png')
st.write('# 종목추천')
st.write("종목추천 날짜:", today)




# btn = st.button('Enter')
# if btn:
#     df = pd.read_csv("종목예시.csv")
#     genres = df['종목명'][1]   
#     st.write("장르: ", genres)


# df = pd.read_csv("chosenS.csv")
# df2 = pd.read_csv("chosen ar.csv")

df = pd.read_csv("./data/2.24_recommend.csv")
df2 = pd.read_csv("./data/summary_company.csv")
a = len(df)

for i in range(a):
    if st.button(df["name"][i]):
        nav_page(f"cc{i}")

# st.write('# 종목추천')
# col1, col2, col3, col4, col5 = st.columns(5)
# col1.metric("Low risk Low return", "종목명1", "종가1")
# col2.metric("Low risk Low return", "종목명2", "종가2")
# col3.metric("Low risk Low return", "종목명3", "종가3")
# col4.metric("Low risk Low return", "종목명4", "종가4")
# col5.metric("Low risk Low return", "종목명5", "종가5")

# st.write('# 종목추천')
# col6, col7, col8, col9, col10 = st.columns(5)
# col6.metric("Low risk Low return", "종목명6", "종가6")
# col7.metric("Low risk Low return", "종목명7", "종가7")
# col8.metric("Low risk Low return", "종목명8", "종가8")
# col9.metric("Low risk Low return", "종목명9", "종가9")
# col10.metric("Low risk Low return", "종목명10", "종가10")





# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


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