import streamlit as st
import time
import numpy as np
from streamlit.components.v1 import html
import pandas as pd

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


st.set_page_config(page_title="Plotting Demo", page_icon="📈")
if st.button("Home으로 돌아가기"):
    nav_page("home")
if st.button("뒤로가기"):
    nav_page("bb") 

df = pd.read_csv("종목예시.csv")
df2 = pd.read_csv("samsung_label_title.csv")


st.markdown("종목명:")
st.header(df["종목명"][6])


st.sidebar.header("Plotting Demo")
st.write(
    """긍정적 뉴스와 부정적인 뉴스에 대한 분류입니다."""
)



lb = df2["label"]
tt = df2["title"]

st.markdown("# 긍적적인 뉴스")

pos = []
for i in range(len(lb)):
    if lb[i] == "positive":
        pos.append(tt[i])
    

st.write(pos)

st.markdown("# 중립적인 뉴스")

net = []
for i in range(len(lb)):
    if lb[i] == "neutral":
        net.append(tt[i])
    

st.write(net)

st.markdown("# 부정적인 뉴스")

nat = []
for i in range(len(lb)):
    if lb[i] == "negative":
        nat.append(tt[i])
    

st.write(nat)



# a = sum(df2["label"]=="positive")
# print(a)



# for i in range(a):
#     if st.button(df["종목명"][i]):
#         nav_page(f"cc{i}")



#title,label,score