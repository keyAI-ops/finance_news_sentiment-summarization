import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.image('ai_robot2.png')
st.write("# 구름 팀1의 인공지능 주가예측 및 분석서비스에 오신 것을 환영합니다! 👋")

#st.sidebar.success("Select a demo above.")

st.markdown(
    """
    - Low risk Low return
    - Medium risk Medium return
    - High risk High return
    ### 추천된 종목에 대해서 더 자세한 정보를 아시고 싶으신가요?
    - 추천된 종목 중 원하는 종목 클릭
    - 인공지능으로 분석된 긍정 뉴스 요약 / 부정 뉴스 요약
    - 인공지능으로 자동생성된 주식분석보고서를 보실 수 있습니다.
    ### 지금 추천 클릭을 눌러보세요.
"""
)




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

#st.button('추천') 

if st.button('#주식 추천'):
    nav_page("recommend")
    st.write('종목 추천을 받으셨습니다')
else:
    st.write('추천을 받으시겠습니까?')
