import streamlit as st
from cutlet import Cutlet
import pysbd 

senter = pysbd.Segmenter(language="ja", clean=False)
ZKS = " " # full width space

def romajify(text, system="hepburn"):
    out = ""
    katsu = Cutlet(system)
    katsu.use_foreign_spelling = False
    for line in text.split("] ["):
        for chunk in line.strip("[]").split(ZKS):
            for sent in senter.segment(chunk):
                out += katsu.romaji(sent, capitalize=False, title=False) + " "
            out += ZKS
        out += " "
    return out.strip()

st.set_page_config("cutlet ローマ字変換ツール", 'https://cotonoha.io/android-icon-144x144.png')

st.title("cutlet ローマ字変換")

system = st.radio(
        "ローマ字の種類",
        ("ヘボン式", "訓令式"))

text = st.text_area('変換したいテキストを入力してください', 
        "[00:21.49]一人 秋の海をみつめて思い出す] [00:31.49]あの夏の影を探して")

systems = {"ヘボン式": "hepburn", "訓令式": "kunrei"}
system = systems[system]

"# 変換結果"

st.write(romajify(text, system))

st.markdown('<div><a style="width: 200px;margin: 0 auto; display: block" href="https://cotonoha.io"><img src="https://cotonoha.io/cotonoha.png" /></a></div>', unsafe_allow_html=True)
