import streamlit as st
import matplotlib.pyplot as plt
from collections import defaultdict
import Analisis_p
import Análisis_s
import Load_data

st.set_page_config(page_title="Análisis de series y películas", layout="wide")
st.title("Análisis de Contenido Audiovisual")
opcion = st.radio ("¿Qué deseas analizar?", options= ["Series", "Películas"], horizontal=True)
if opcion == "Series":
    bd_series = Analisis_s.analizador_series(Load_data.lista_series)
    opc = st.radio ("¿Qué tipo de analisis quieres hacer?", options=["Géneros más populares en X año", "Año con más series finalizadas", "Año con más series estrenadas"], horizontal= True)
    if opc == "Géneros más populares en X año":
        año_a = st.slider ("Año", 1927, 2023)
        st.pyplot(bd_series.graf_genero_año(año_a))
    elif opc == "Año con más series estrenadas":
        st.write(bd_series.año_emision())
    else:
        st.write(bd_series.año_finalizacion())
else:
    bd_pelis = Analisis_p.analizador_pelis(Load_data.lista_peliculas)
    opt = st.radio("¿Qué tipo de análisis te gustaría hacer?", options=["Géneros más populares en X año", "Película más duradera en X año", "Película menos duradera en X año"], horizontal= True)
    if opt == "Géneros más populares en X año":
        año_p = st.slider("Año", 1896 , 2025)
        st.pyplot(bd_pelis.graf_genero_año(año_p))
    elif opt == "Película más duradera en X año":
        año_b = st.slider("Año", 1896, 2025)
        st.write(bd_pelis.mayor_duración(año_b))
    else:
        año_c = st.slider("Año", 1896, 2025)
        st.write(bd_pelis.menor_duraciom(año_c))