import streamlit as st
import time
import numpy as np
from streamlit.components.v1 import html
import pandas as pd

import torch
from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
import pandas as pd
from summaryFunc import summaryModel
from news import newsFunc



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

stocks = pd.read_csv("chosenS.csv")
news = pd.read_csv("chosen ar.csv")

stock_name = stocks["name"][0]
st.header(f"종목명: {stock_name}")


st.sidebar.header("Plotting Demo")

###

st.write(
    """긍정적 뉴스와 부정적인 뉴스에 대한 분류입니다."""
)


title = news["title"]
label = news["label"]
company = news["company"]
summary = news["summary"]

sentiments = ['positive','negative','None']
for sentiment in sentiments:
    newsFunc(sentiment,company,stock_name,label,summary)





