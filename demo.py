import streamlit as st
from cutlet import Cutlet
import pysbd 

# Instanciar el segmentador de frases para japonés con la configuración por defecto
senter = pysbd.Segmenter(language="ja", clean=False)
ZKS = " " # Espacio de ancho completo para segmentar texto japonés

def romajify(text, system="hepburn"):
    """
    Convierte texto japonés a romaji.
    
    Args:
        text (str): Texto japonés para convertir.
        system (str): Sistema de romanización ('hepburn' o 'kunrei').
    
    Returns:
        str: Versión en romaji del texto ingresado.
    """
    out = []
    katsu = Cutlet(system)
    katsu.use_foreign_spelling = False
    
    # Procesa cada línea y cada sección
    for line in text.split("\n"):
        line_out = []
        for chunk in line.split(ZKS):
            if chunk.strip():
                segment_out = []
                for sent in senter.segment(chunk):
                    segment_out.append(katsu.romaji(sent, capitalize=False, title=False))
                line_out.append("".join(segment_out))
            else:
                line_out.append(chunk)
        out.append("".join(line_out))
    
    return "\n".join(out)

# Configuración de la página de Streamlit
st.set_page_config("cutlet ローマ字変換ツール", 'https://cotonoha.io/android-icon-144x144.png')

st.title("cutlet ローマ字変換")

# Opciones de selección para el sistema de romanización
system = st.radio("ローマ字の種類", ("ヘボン式", "訓令式"))

text = st.text_area('変換したいテキストを入力してください', "吾輩は猫である。名前はまだ無い。")

# Mapeo de selecciones a identificadores internos
systems = {"ヘボン式": "hepburn", "訓令式": "kunrei"}
system = systems[system]

# Mostrar el resultado de la conversión
st.subheader("変換結果")
st.write(romajify(text, system))

# Enlace al recurso
st.markdown('<div style="width: 200px; margin: 0 auto; display: block;"><a href="https://cotonoha.io"><img src="https://cotonoha.io/cotonoha.png" /></a></div>', unsafe_allow_html=True)
