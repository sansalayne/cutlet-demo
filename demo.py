import streamlit as st
from cutlet import Cutlet
import pysbd
import re

senter = pysbd.Segmenter(language="ja", clean=False)
ZKS = " "  # Espacio de ancho completo para segmentar texto japonés

def romajify(text, system="hepburn"):
    """
    Convierte texto japonés a romaji, preservando marcas de tiempo y otros elementos.
    """
    out = []
    katsu = Cutlet(system)
    katsu.use_foreign_spelling = False

    # Expresión regular para detectar y preservar timestamps y otros elementos
    pattern = r'(\[[^\]]+\])|([^\[\]]+)'
    
    for line in text.split("\n"):
        line_out = []
        elements = re.findall(pattern, line)
        for element in elements:
            timestamp, text = element
            if text:
                segments = senter.segment(text)
                romaji_text = ' '.join([katsu.romaji(segment, capitalize=False, title=False) for segment in segments])
                line_out.append(romaji_text)
            else:
                line_out.append(timestamp)
        out.append(''.join(line_out))
    
    return "\n".join(out)

# Configuración de la página de Streamlit
st.set_page_config("cutlet ローマ字変換ツール", 'https://cotonoha.io/android-icon-144x144.png')
st.title("cutlet ローマ字変換")
system = st.radio("ローマ字の種類", ("ヘボン式", "訓令式"))
text = st.text_area('変換したいテキストを入力してください', "吾輩は猫である。名前はまだ無い。")

systems = {"ヘボン式": "hepburn", "訓令式": "kunrei"}
system = systems[system]

st.subheader("変換結果")
st.write(romajify(text, system))

st.markdown('<div style="width: 200px; margin: 0 auto; display: block;"><a href="https://cotonoha.io"><img src="https://cotonoha.io/cotonoha.png" /></a></div>', unsafe_allow_html=True)
