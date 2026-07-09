import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Pequeños Detalles - Impacto", layout="wide")

# 2. ESTILOS PROFESIONALES (Tipografía Montserrat)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    .stApp { background-color: #faf6f5; font-family: 'Montserrat', sans-serif !important; }
    h1 { color: #3a2226; font-family: 'Montserrat', sans-serif !important; text-align: center; margin-bottom: 30px; }
    .metric-card {
        background-color: #ffffff; padding: 25px; border-radius: 20px;
        text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #fce4ec; height: 100%;
    }
    .metric-val { font-size: 1.6rem; font-weight: 700; color: #e57393; margin-bottom: 5px; }
    .metric-desc { font-size: 0.85rem; color: #705a5d; line-height: 1.4; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Calculadora de Impacto Ambiental</h1>", unsafe_allow_html=True)

# 3. BASE DE DATOS COMPLETA
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
    "Mameluco acolchado": 5.82, "Mameluco drill": 5.90, "Mameluco jean reflectivo": 5.35,
    "Merma": 6.57, "Overol": 6.57, "Pantalón": 6.57, "Pantalón algodón": 5.00,
    "Pantalón drill": 5.90, "Pantalón drill con cinta": 5.96, "Pantalón ignífugo": 5.35,
    "Pantalón jean": 5.00, "Pantalón jean / drill": 5.45, "Pantalón jean con cinta reflectiva": 5.05,
    "Pantalón polar": 6.00, "Pantalón térmico": 5.82, "Polera": 5.00,
    "Polera polar": 6.00, "Polo": 5.00, "Polo algodón": 5.00, "Polo con cinta reflectiva": 5.05,
    "Polo manga corta": 5.00, "Polo manga larga": 6.80, "Polo manga larga con cinta reflectiva": 6.86,
    "Polo piqué": 5.0
