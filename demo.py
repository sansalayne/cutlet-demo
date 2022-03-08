import streamlit as st
from cutlet import Cutlet
import pysbd 
import streamlit as st

senter = pysbd.Segmenter(language="ja", clean=False)
ZKS = "　" # full width space

def romajify(text, system="hepburn"):
    out = ""
    katsu = Cutlet(system)
    for text in text.split(" \n"):
        for chunk in text.split(ZKS):
            for sent in senter.segment(chunk):
                out += katsu.romaji(sent) + " "
            out += ZKS
        out += " \n"

    return out

help_input='''This is the line1\n
This is the line 2\n
This is the line 3'''

st.set_page_config("cutlet ローマ字変換ツール", 'https://cotonoha.io/android-icon-144x144.png')

st.title("cutlet ローマ字変換")

system = st.radio(
        "ローマ字の種類",
        ("ヘボン式", "訓令式"))

text = st.text_area('変換したいテキストを入力してください', 
        "吾輩は猫である。名前はまだ無い。")


systems = {"ヘボン式": "hepburn", "訓令式": "kunrei"}
system = systems[system]

"# 変換結果"

st.write(romajify(text, system,##))

st.markdown('<div><a style="width: 200px;margin: 0 auto; display: block" href="https://cotonoha.io"><img src="https://cotonoha.io/cotonoha.png" /></a></div>', unsafe_allow_html=True)
