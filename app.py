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

# LÓGICA
bd_factores = {"Banner": 9.5, "Bata": 6.5, "Camisa": 6.5, "Casaca": 6.5, "Chaleco": 6.5, "Chompa": 6.5, "Mameluco": 6.5, "Pantalón": 6.5, "Polo": 5.0}

if 'data' not in st.session_state: st.session_state.data = []

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📥 Registro")
    p = st.selectbox("Prenda", list(bd_factores.keys()))
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
        
        # Árboles
        m1.markdown(f'''<div class="metric-card"><div class="metric-icon">🌳</div><div class="metric-val">{round(tot_co2/22, 1)} Árboles</div>
                    <div class="metric-label">Capacidad de absorción</div>
                    <div class="metric-desc">Equivalente al trabajo anual de absorción de CO₂ de árboles maduros gestionados.</div></div>''', unsafe_allow_html=True)
        
        # Agua
        m2.markdown(f'''<div class="metric-card"><div class="metric-icon">💧</div><div class="metric-val">{int(tot_agua):,} Litros</div>
                    <div class="metric-label">Agua dulce ahorrada</div>
                    <div class="metric-desc">Evitamos el consumo hídrico industrial necesario para producir material textil virgen.</div></div>''', unsafe_allow_html=True)
        
        # Coches
        m3.markdown(f'''<div class="metric-card"><div class="metric-icon">🚗</div><div class="metric-val">{int(tot_co2/0.25):,} km</div>
                    <div class="metric-label">Huella vehicular evitada</div>
                    <div class="metric-desc">Distancia que un auto promedio dejaría de emitir gases al ambiente gracias a tu acción.</div></div>''', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
