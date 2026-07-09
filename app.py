import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Pequeños Detalles - Impacto", layout="wide")

# 2. ESTILOS (Montserrat + Tarjetas con explicación)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    .stApp { background-color: #faf6f5; font-family: 'Montserrat', sans-serif !important; }
    h1, h2, h3 { color: #3a2226; font-family: 'Montserrat', sans-serif !important; }
    
    .metric-card {
        background-color: #ffffff; padding: 25px; border-radius: 20px;
        text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #fce4ec; height: 100%;
    }
    .metric-icon { font-size: 2.5rem; margin-bottom: 10px; }
    .metric-val { font-size: 1.6rem; font-weight: 700; color: #e57393; margin-bottom: 5px; }
    .metric-label { font-size: 0.9rem; font-weight: 700; color: #3a2226; text-transform: uppercase; margin-bottom: 10px; }
    .metric-desc { font-size: 0.85rem; color: #705a5d; line-height: 1.4; }
    </style>
""", unsafe_allow_html=True)

# 3. LOGO
if os.path.exists("pequeños detalles logo.png"):
    _, c, _ = st.columns([3, 1, 3])
    with c: st.image("pequeños detalles logo.png")

st.markdown("<h1>Calculadora de Impacto Ambiental</h1>", unsafe_allow_html=True)

# BASE DE DATOS COMPLETA
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
    "Polo piqué": 5.00, "Short": 5.00, "Toalla": 5.00, "Chaleco Fluorescente": 6.62
}

if 'data' not in st.session_state: st.session_state.data = []

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📥 Registro")
    p = st.selectbox("Prenda", sorted(list(bd_factores.keys())))
    q = st.number_input("Cantidad", 1, 1000)
    w = st.number_input("Peso (kg)", 0.1, 500.0)
    if st.button("➕ Agregar al reporte"):
        st.session_state.data.append({"Prenda": p, "Kg": w, "CO2": w * bd_factores[p]})

with col2:
    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data)
        tot_kg = df["Kg"].sum()
        tot_co2 = df["CO2"].sum()
        tot_agua = tot_kg * 10000 
        
        st.subheader("✨ Tu Impacto Total")
        m1, m2, m3 = st.columns(3)
        
        m1.markdown(f'''<div class="metric-card"><div class="metric-icon">🌳</div><div class="metric-val">{round(tot_co2/22, 1)} Árboles</div>
                    <div class="metric-label">Capacidad de absorción</div>
                    <div class="metric-desc">Equivalente al trabajo anual de absorción de CO₂ de árboles maduros gestionados.</div></div>''', unsafe_allow_html=True)
        
        m2.markdown(f'''<div class="metric-card"><div class="metric-icon">💧</div><div class="metric-val">{int(tot_agua):,} Litros</div>
                    <div class="metric-label">Agua dulce ahorrada</div>
                    <div class="metric-desc">Evitamos el consumo hídrico industrial necesario para producir material textil virgen.</div></div>''', unsafe_allow_html=True)
        
        m3.markdown(f'''<div class="metric-card"><div class="metric-icon">🚗</div><div class="metric-val">{int(tot_co2/0.25):,} km</div>
                    <div class="metric-label">Huella vehicular evitada</div>
                    <div class="metric-desc">Distancia que un auto promedio dejaría de emitir gases al ambiente gracias a tu acción.</div></div>''', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
