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

def newsFunc(sentiment,company,stock_name,label,summary):

    senti_text = ""
    if sentiment == 'positive':
        senti_text = "😇긍정"
    elif sentiment == 'negative':
        senti_text = "😈부정"
    elif sentiment == "None":
        senti_text = "🤔중립"

    st.markdown(f"# {senti_text} 뉴스")

    add = ""
    splitted = []
    for i in range(len(label)):
        
        if company[i] == stock_name and label[i] == sentiment:
            add += summary[i]
            splitted.append(summary[i])

    print(sentiment)
    print(splitted)
    print(add)
    st.write(splitted)
    st.write(add)


    # print("🎒")
    # print(type(add))
    # print(summary)



    st.header(f"{senti_text}뉴스 총평")


    st.markdown(f"{senti_text}뉴스의 총평을 보려면 버튼을 클릭해주세요! (시간이 다소 소요됩니다)")
    if st.button(f"{senti_text}뉴스 총평"):
        pos_result = summaryModel(add)
        st.write(f"👉\n{pos_result}")

