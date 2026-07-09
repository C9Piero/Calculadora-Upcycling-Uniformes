import streamlit as st
import pandas as pd
import os

# 1. Configuración de página
st.set_page_config(page_title="Pequeños Detalles - Impacto", layout="wide")

# 2. Estilos profesionales
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;700&display=swap');
    .stApp { background-color: #faf6f5; font-family: 'League Spartan', sans-serif !important; }
    h1 { color: #3a2226; font-family: 'League Spartan', sans-serif !important; text-align: center; font-size: 3.5rem !important; }
    .sub-title { text-align: center; color: #705a5d; font-size: 1.5rem; margin-bottom: 40px; font-weight: 400; }
    .metric-card { background-color: #ffffff; padding: 30px; border-radius: 15px; text-align: center; box-shadow: 0 8px 20px rgba(0,0,0,0.1); border: 1px solid #fce4ec; height: 100%; }
    .metric-val { font-size: 2.2rem; font-weight: 700; color: #e57393; margin-bottom: 10px; }
    .metric-desc { font-size: 1.0rem; color: #705a5d; line-height: 1.4; }
    .co2-total { background-color: #fce4ec; color: #3a2226; padding: 25px; border-radius: 15px; text-align: center; font-weight: 700; font-size: 2.0rem; margin: 40px 0; border: 2px solid #f17394; }
    table { width: 100%; font-family: 'League Spartan', sans-serif; font-size: 1.1rem; }
    </style>
""", unsafe_allow_html=True)

if 'data' not in st.session_state: st.session_state.data = []

# 3. Logo
if os.path.exists("pequeños detalles logo.png"):
    _, c, _ = st.columns([3, 1, 3])
    with c: st.image("pequeños detalles logo.png")

st.markdown("<h1>Calculadora de Impacto Ambiental</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Descubre el impacto positivo que logramos al transformar tus uniformes en desuso a través de nuestro proceso de Upcycling.</p>", unsafe_allow_html=True)

# 4. Base de datos completa (Factor CO2, Factor Agua L/kg)
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
    "Polera polar": (6.0, 5000), "Polo": (5.0, 10000), "Polo algodón": (5.0, 10000), "Polo con cinta reflectiva": (5.05, 5000),
    "Polo manga corta": (5.0, 10000), "Polo manga larga": (6.8, 10000), "Polo manga larga con cinta reflectiva": (6.86, 5000),
    "Polo piqué": (5.0, 10000), "Short": (5.0, 10000), "Toalla": (5.0, 10000), "Chaleco Fluorescente": (6.62, 5000)
}

# 5. Interfaz
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📥 Registro")
    p = st.selectbox("Prenda", sorted(list(bd_factores.keys())))
    q = st.number_input("Cantidad", 1, 1000)
    w = st.number_input("Peso total (kg)", 0.1, 500.0)
    if st.button("➕ Agregar al reporte"):
        f_co2, f_agua = bd_factores[p]
        st.session_state.data.append({"Prenda": p, "Und": q, "Kg": w, "CO2": w * f_co2, "Agua": w * f_agua})
        st.rerun()

with col2:
    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data)
        tot_co2, tot_agua = df["CO2"].sum(), df["Agua"].sum()
        
        st.subheader("📋 Detalle de Prendas")
        st.table(df[["Prenda", "Und", "Kg", "CO2"]].reset_index(drop=True))
        
        st.markdown(f'<div class="co2-total">Total CO₂ Evitado: {round(tot_co2, 2)} kg</div>', unsafe_allow_html=True)
        
        st.subheader("✨ Tu Impacto Total")
        m1, m2, m3 = st.columns(3)
        m1.markdown(f'''<div class="metric-card"><div class="metric-val">🌳 {round(tot_co2/22, 1)} Árboles</div><div class="metric-desc">Absorción de CO₂ anual.</div></div>''', unsafe_allow_html=True)
        m2.markdown(f'''<div class="metric-card"><div class="metric-val">💧 {int(tot_agua):,} L</div><div class="metric-desc">Agua dulce ahorrada.</div></div>''', unsafe_allow_html=True)
        m3.markdown(f'''<div class="metric-card"><div class="metric-val">🚗 {int(tot_co2/0.25):,} km</div><div class="metric-desc">Huella vehicular evitada.</div></div>''', unsafe_allow_html=True)
        
        if st.button("🗑️ Limpiar todo"):
            st.session_state.data = []
            st.rerun()
