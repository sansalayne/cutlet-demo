import streamlit as st
from cutlet import Cutlet

def romajify(text, system="hepburn"):
    katsu = Cutlet(system)
    return katsu.romaji(text)

st.beta_set_page_config("cutlet ローマ字変換ツール", 'https://cotonoha.io/android-icon-144x144.png')

st.title("cutlet ローマ字変換")

text = st.text_area('変換したいテキストを入力してください', 
        "吾輩は猫である。名前はまだ無い。")

"### ヘボン式"

st.write(romajify(text, 'hepburn'))

"### 訓令式"

st.write(romajify(text, 'kunrei'))

st.markdown('<div><a style="width: 200px;margin: 0 auto; display: block" href="https://cotonoha.io"><img src="/cotonoha.png" /></a></div>', unsafe_allow_html=True)
