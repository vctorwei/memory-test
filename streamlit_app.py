import streamlit as st

# 设置页面布局
st.set_page_config(page_title="深圳记忆", layout="wide", initial_sidebar_state="collapsed")

# 隐藏 Streamlit UI 并用白色块覆盖 footer
hide_footer_styles = """
<style>
    header {display: none !important;}  /* 隐藏顶部栏 */
    footer {visibility: hidden !important;}  /* 隐藏 footer */
    div[data-testid="stToolbar"] { display: none !important; }
    div[data-testid="stStatusWidget"] { display: none !important; }
    iframe[title="streamlit doc"] { display: none !important; }

    /* 用白色块覆盖 footer */
    div.footer-cover {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 40px;  /* 适当调整高度以完全覆盖 footer */
        background-color: white;  /* 白色背景 */
        z-index: 9999;
    }
</style>
<div class="footer-cover"></div>
"""
st.markdown(hide_footer_styles, unsafe_allow_html=True)

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
