import streamlit as st

# 设置页面布局
st.set_page_config(page_title="深圳记忆", layout="wide", initial_sidebar_state="collapsed")

# 隐藏 Streamlit 的默认 UI
hide_streamlit_styles = """
<style>
    header {display: none !important;}
    footer {visibility: hidden !important;}
    div[data-testid="stToolbar"] { display: none !important; }
    div[data-testid="stStatusWidget"] { display: none !important; }
    iframe[title="streamlit doc"] { display: none !important; }
</style>
"""
st.markdown(hide_streamlit_styles, unsafe_allow_html=True)

# **显示标题**
st.markdown(
    """
    <style>
    .title {
        font-family: SimHei, sans-serif;
        font-size: 20px;
        color: #666;
        text-align: center;
        font-weight: normal;
    }
    .home-text {
        text-align: center;
        font-family: SimHei, sans-serif;
        font-size: 16px;
        color: #666;
        margin-top: 10px;
    }
    </style>
    <div class='title'>关于你的深圳记忆<br>About Your Shenzhen Memory</div>
    """,
    unsafe_allow_html=True
)

# Home/家 显示
st.markdown(
    """
    <div class='home-text'>Home</div>
    <div class='home-text'>家</div>
    """,
    unsafe_allow_html=True
)
