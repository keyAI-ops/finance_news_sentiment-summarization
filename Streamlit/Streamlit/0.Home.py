import streamlit as st
import pandas as pd
import numpy as np

from IPython.display import display
import ipywidgets as widgets

import streamlit as st

from transformers import (
    EncoderDecoderModel,
    GPT2Tokenizer,
)

from lib.tokenization_kobert import KoBertTokenizer


st.title("인공지능 주식추천 및 종목분석 자동생성 서비스")
page_names = ['종목추천', '종목 분석보고서']
page = st.radio('서비스 항목', page_names)
st.write("**선택 항목:**", page)

# if 'tokenizer' not in st.session_state:
#     src_tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')
#     trg_tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
#     st.session_state.tokenizer = src_tokenizer, trg_tokenizer
# else:
#     src_tokenizer, trg_tokenizer = st.session_state.tokenizer


# @st.cache
# def get_model(bos_token_id):
#     model = EncoderDecoderModel.from_pretrained('dump/best_model')
#     model.config.decoder_start_token_id = bos_token_id
#     model.eval()
#     model.cuda()

#     return model

# model = get_model(trg_tokenizer.bos_token_id)







# columns=('col %d' % i for i in range(10))


# for i in range(10):
#     a = 'col %d' % i
#     a=st.columns(10)
#     a.metric("Low risk Low return", "종목명", "종가")
    

if page == '종목추천':
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
    st.image('ai_robot.png')
elif page == '종목 분석보고서':
    st.subheader("종목 분석보고서에 오신것을 환영합니다!")
    st.write("종목명")
    
    df = pd.read_json("train.json")  # read a CSV file inside the 'data" folder next to 'app.py'
    # df = pd.read_excel(...)  # will work for Excel files

    st.title("종목 뉴스 긍정/부정 분류")  # add a title
    st.write(df)  # visualize my dataframe in the Streamlit app

    df = pd.DataFrame(
    np.random.randn(1, 2),
    columns=('긍정', '부정'))

    st.dataframe(df)

    df = pd.DataFrame(
    np.random.randn(1, 2),
    columns=('종합 분석','비고'))

    st.dataframe(df)

    st.title("한-영 번역기")
    st.subheader("한-영 번역기에 오신 것을 환영합니다!")

    kor = st.text_area("입력", placeholder="번역할 한국어")

    if st.button("번역!", help="해당 한국어 입력을 번역합니다."):
        embeddings = src_tokenizer(kor, return_attention_mask=False, return_token_type_ids=False, return_tensors='pt')
        embeddings = {k: v.cuda() for k, v in embeddings.items()}
        output = model.generate(**embeddings)[0, 1:-1].cpu()
        st.text_area("출력", value=trg_tokenizer.decode(output), disabled=True)
        st.write("State of button:", result)

# if check:
#     nested_btn = st.button("Button nested in Checkbox")

#     if nested_btn:
#         st.write(":cake:"*20)

# if page == 'Checkbox':
#     st.subheader('Welcome to the Checkbox page!')
#     st.write("Nice to see you! :wave:")
#     check = st.checkbox("Click here")
#     st.write('State of the checkbox:', check)


# if result:
#     nested_check = st.checkbox("Checkbox nested in Button")

#     if nested_check:
#         st.write(":heart:"*20)