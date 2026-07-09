import streamlit as st
import pandas as pd
import os

# 1. Configuración
st.set_page_config(page_title="Pequeños Detalles - Impacto", layout="wide")

# 2. Estilos profesionales
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    .stApp { background-color: #faf6f5; font-family: 'Montserrat', sans-serif !important; }
    h1 { color: #3a2226; font-family: 'Montserrat', sans-serif !important; text-align: center; }
    .metric-card {
        background-color: #ffffff; padding: 20px; border-radius: 15px;
        text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border: 1px solid #fce4ec; height: 100%;
    }
    .metric-val { font-size: 1.4rem; font-weight: 700; color: #e57393; margin-bottom: 5px; }
    .metric-desc { font-size: 0.8rem; color: #705a5d; line-height: 1.3; }
    .co2-total {
        background-color: #fce4ec; color: #3a2226; padding: 20px; 
        border-radius: 15px; text-align: center; font-weight: 700; font-size: 1.5rem;
        margin: 30px 0; border: 2px solid #f17394;
    }
    </style>
""", unsafe_allow_html=True)

if 'data' not in st.session_state: st.session_state.data = []

# 3. Logo con manejo de error
if os.path.exists("pequeños detalles logo.png"):
    _, c, _ = st.columns([3, 1, 3])
    with c: st.image("pequeños detalles logo.png")

st.markdown("<h1>Calculadora de Impacto Ambiental</h1>", unsafe_allow_html=True)

# 4. Base de datos
bd_factores = {
    "Banner": 9.50, "Bata de laboratorio": 6.57, "Bolsas": 8.00, "Camisa": 6.57,
    "Camisa algodón": 5.00, "Camisa drill": 5.90, "Camisa ignífuga": 5.35,
    "Camisa jean / denim": 5.00, "Camisaco": 5.00, "Camisaco drill": 5.90,
    "Camisaco drill con cinta": 5.96, "Casaca": 6.57, "Casaca drill": 5.90,
    "Casaca polar": 6.00, "Casaca polar con cinta reflectiva": 6.05,
    "Casaca térmica": 5.82, "Chaleco": 6.57, "Chaleco con cinta": 6.62,
    "Chaleco de seguridad": 6.62, "Chaleco polar": 6.00, "Chaleco reversible": 6.57,
    "Chompa": 6.57, "Chompa con cinta reflectiva": 6.62, "Chompa Jorge Chavez": 6.30,
    "Chompa Jorge Chavez con cinta reflectiva": 6.30, "Chompa polar": 6.00,
    "Enterizo": 6.57, "Gorro": 7.92, "Impermeable": 9.42, "Mameluco": 6.57,
    "Mameluco acolchado": 5.82
