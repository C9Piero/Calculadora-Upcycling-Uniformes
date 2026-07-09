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
    .sub-title { text-align: center; color: #705a5d; font-size: 1.2rem; margin-bottom: 30px; font-style: italic; }
    .metric-card { background-color: #ffffff; padding: 20px; border-radius: 15px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.05); border: 1px solid #fce4ec; height: 100%; }
    .metric-val { font-size: 1.4rem; font-weight: 700; color: #e57393; margin-bottom: 5px; }
    .metric-desc { font-size: 0.8rem; color: #705a5d; line-height: 1.3; }
    .co2-total { background-color: #fce4ec; color: #3a2226; padding: 20px; border-radius: 15px; text-align: center; font-weight: 700; font-size: 1.5rem; margin: 30px 0; border: 2px solid #f17394; }
    </style>
""", unsafe_allow_html=True)

if 'data' not in st.session_state: st.session_state.data = []

# Logo
if os.path.exists("pequeños detalles logo.png"):
    _, c, _ = st.columns([3, 1, 3])
    with c: st.image("pequeños detalles logo.png")

st.markdown("<h1>Calculadora de Impacto Ambiental</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Descubre el impacto positivo que logramos al transformar tus uniformes en desuso a través de nuestro proceso de Upcycling.</p>", unsafe_allow_html=True)

# 3. Base de datos completa (Factor CO2, Factor Agua L/kg)
# Nota: Los ítems con 5000 son más técnicos/industriales, 10000 son los más simples/algodón.
bd_factores = {
    "Banner": (9.5, 10000), "Bata de laboratorio": (6.57, 10000), "Bolsas": (8.0, 10000), "Camisa": (6.57, 10000),
    "Camisa algodón": (5.0, 10000), "Camisa drill": (5.9, 5000), "Camisa ignífuga": (5.35, 5000),
    "Camisa jean / denim": (5.0, 10000), "Camisaco": (5.0, 10000), "Camisaco drill": (5.9, 5000),
    "Camisaco drill con cinta": (5.96, 5000), "Casaca": (6.57, 5000), "Casaca drill": (5.9, 5000),
    "Casaca polar": (6.0, 5000), "Casaca polar con cinta reflectiva": (6.05, 5000),
    "Casaca térmica": (5.82, 5000), "Chaleco": (6.57, 5000), "Chaleco con cinta": (6.62, 5000),
    "Chaleco de seguridad": (6.62, 5000), "Chaleco polar": (6.0, 5000), "Chaleco reversible": (6.57, 5000),
    "Chompa": (6.57, 10000), "Chompa con cinta reflectiva": (6.62, 5000), "Chompa Jorge Chavez": (6.3, 10000),
    "Chompa Jorge Chavez con cinta reflectiva": (6.3, 5000), "Chompa polar": (6.0, 5000),
    "Enterizo": (6.57, 5000), "Gorro": (7.92, 10000), "Impermeable": (9.42, 5000), "Mameluco": (6.57, 5000),
    "Mameluco acolchado": (5.82, 5000), "Mameluco drill": (5.9, 5000), "Mameluco jean reflectivo": (5.35, 5000),
    "Merma": (6.57, 10000), "Overol": (6.57, 5000), "Pantalón": (6.57, 5000), "Pantalón algodón": (5.0, 10000),
    "Pantalón drill": (5.9, 5000), "Pantalón drill con cinta": (5.96, 5000), "Pantalón ignífugo": (5.35, 5000),
    "Pantalón jean": (5.0, 10000), "Pantalón jean / drill": (5.45, 5000), "Pantalón jean con cinta reflectiva": (5.05, 5000),
    "Pantalón polar": (6.0, 5000), "Pantalón térmico": (5.82, 5000), "Polera": (5.0, 10000),
    "Polera polar": (6.0, 5000), "Polo": (5.0, 10000), "Polo algodón": (5.0, 10000), "Polo con cinta reflectiva
