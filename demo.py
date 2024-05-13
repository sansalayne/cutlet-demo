import streamlit as st
from cutlet import Cutlet
import pysbd 
import re

senter = pysbd.Segmenter(language="ja", clean=False)
ZKS = " " # full width space

def romajify(text, system="hepburn"):
    out = ""
    katsu = Cutlet(system)
    katsu.use_foreign_spelling = False
    
    # Regex pattern to identify timestamps or plain text
    pattern = r'(\[[^\]]+\])|([^\[\]]+)'

    # Processing each line individually
    lines = text.split("\n")
    for line in lines:
        line_out = ""
        elements = re.findall(pattern, line)
        for timestamp, chunk in elements:
            if timestamp:
                line_out += timestamp + ""  # Append timestamp directly
            if chunk:
                segments = senter.segment(chunk)
                for segment in segments:
                    line_out += katsu.romaji(segment, capitalize=False, title=False) + " "
        out += line_out.strip() + "\n"  # Append the processed line and a new line

    return out.strip()

# Streamlit app configuration
st.set_page_config(page_title="cutlet ローマ字変換ツール", page_icon='https://cotonoha.io/android-icon-144x144.png')
st.title("cutlet ローマ字変換")

# Selection of Romanization system
system = st.radio("ローマ字の種類", ("ヘボン式", "訓令式"))
systems = {"ヘボン式": "hepburn", "訓令式": "kunrei"}
system = systems[system]

# User input text area
text = st.text_area('変換したいテキストを入力してください', "吾輩は猫である。名前はまだ無い。")

# Display conversion results
st.subheader("変換結果")
st.write(romajify(text, system))

# Link to external site
st.markorary('</div><a style="width: 200px;margin: 0 auto; display: block" href="https://cotonoha.io"><img src="https://cotonoha.io/cotonoha.png" /></a></div>', unsafe_allow_html=True)
