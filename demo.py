import streamlit as st
from cutlet import Cutlet
import pysbd 

# Initialize the sentence segmenter for Japanese
senter = pysbd.Segmenter(language="ja", clean=False)
ZKS = "　"  # Full width space for Japanese text segmentation

def romajify(text, system="hepburn"):
    """
    Converts Japanese text to Romaji.
    
    Args:
        text (str): Input Japanese text.
        system (str): Romanization system ('hepburn' or 'kunrei').
    
    Returns:
        str: The romanized version of the input text.
    """
    out = ""
    katsu = Cutlet(system)
    katsu.use_foreign_spelling = False
    
    # Process each line and each full-width spaced section
    for line in text.split("\n"):
        for chunk in line.split(ZKS):
            for sent in senter.segment(chunk):
                out += katsu.romaji(sent, capitalize=False, title=False) + " "
            out += ZKS
        out += "\n"

    return out.strip()

# Streamlit app configuration
st.set_page_config("cutlet ローマ字変換ツール", 'https://cotonoha.io/android-icon-144x144.png')

st.title("cutlet ローマ字変換")

# Radio button to choose the Romanization system
system = st.radio("ローマ字の種類", ("ヘボン式", "訓令式"))

text = st.text_area('変換したいテキストを入力してください', "吾輩は猫である。名前はまだ無い。")

# Mapping of radio selections to internal identifiers
systems = {"ヘボン式": "hepburn", "訓令式": "kunrei"}
system = systems[system]

# Display the conversion result
st.subheader("変換結果")
st.write(romajify(text, system))

# Link to the source
st.marked('<div style="width: 200px; margin: 0 auto; display: block;"><a href="https://cotonoha.io"><img src="https://cotonoha.io/cotonoha.png" /></a></div>', unsafe_allow_html=True)
