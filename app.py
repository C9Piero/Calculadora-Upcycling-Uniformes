import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Pequeños Detalles - Calculadora de Impacto Sostenible", 
    page_icon="🌸", 
    layout="wide"
)

# 2. ESTILOS CSS CON LOS TONOS ROSADOS Y CORPORATIVOS DE TU LOGO
st.markdown("""
    <style>
    .stApp {
        background-color: #faf6f5;
    }
    
    div[data-testid="stVerticalBlock"] > div[data-testid="stContainer"] {
        background-color: #ffffff;
        padding: 26px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(224, 182, 182, 0.15);
        border: 1px solid #f2e6e6;
        margin-bottom: 20px;
    }
    
    h1 {
        color: #3a2226;
        font-family: 'Segoe UI', Roboto, sans-serif;
        font-weight: 700;
        text-align: center;
    }
    
    h3 {
        color: #e57393;
        font-family: 'Segoe UI', Roboto, sans-serif;
        font-weight: 600;
        margin-bottom: 15px !important;
    }
    
    .stButton>button {
        background-color: #f17394;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #d65677;
        color: white;
        transform: translateY(-1px);
    }
    
    /* Estilos especiales para las tarjetas de equivalencias */
    .eq-card {
        background-color: #fff8f9;
        border: 1px solid #fce4ec;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }
    .eq-icon {
        font-size: 2.8rem;
        margin-bottom: 10px;
    }
    .eq-value {
        font-size: 1.6rem;
        font-weight: bold;
        color: #3a2226;
        margin-bottom: 5px;
    }
    .eq-text {
        font-size: 0.9rem;
        color: #705a5d;
    }
    </style>
""", unsafe_allow_html=True)

# 3. INTERFAZ: LOGO CENTRADO
logo_path = "pequeños detalles logo.png"
if os.path.exists(logo_path):
    col_logo1, col_logo2, col_logo3 = st.columns([2, 1, 2])
    with col_logo2:
        st.image(logo_path, use_container_width=True)

st.markdown("<h1>Calculadora de Impacto Ambiental</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #665255; font-size: 1.1rem;'>Descubre el impacto positivo y el CO₂ que evitamos juntos al transformar tus uniformes en desuso a través del Upcycling con Pequeños Detalles.</p>", unsafe_allow_html=True)

st.markdown("---")

# BASE DE DATOS MAESTRA COMPLETA (Oculta para el cliente)
bd_factores_completa = {
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

if 'lista_calculadora' not in st.session_state:
    st.session_state.lista_calculadora = []

col_izq, col_der = st.columns([1.1, 2], gap="large")

with col_izq:
    with st.container():
        st.subheader("📥 Tus Uniformes")
        
        prenda_sel = st.selectbox("👔 Tipo de Prenda / Uniforme", options=sorted(list(bd_factores_completa.keys())))
        
        c1, c2 = st.columns(2)
        with c1:
            cantidad = st.number_input("🔢 Cantidad (unidades)", min_value=1, value=100, step=10)
        with c2:
            peso_total = st.number_input("⚖️ Peso Total (kg)", min_value=0.1, value=43.0, step=1.0)
        
        st.markdown(" ")
        
        c_btn1, c_btn2 = st.columns(2)
        with c_btn1:
            if st.button("➕ Añadir al Cálculo", use_container_width=True):
                factor_actual = bd_factores_completa.get(prenda_sel, 5.0)
                st.session_state.lista_calculadora.append({
                    "Tipo de prenda": prenda_sel,
                    "Cantidad (und)": int(cantidad),
                    "Peso total (kg)": round(peso_total, 2),
                    "CO2 Evitado (kg)": round(peso_total * factor_actual, 2)
                })
                st.toast(f"🌸 {prenda_sel} agregada")
                
        with c_btn2:
            if st.button("🗑️ Vaciar", use_container_width=True):
                st.session_state.lista_calculadora = []
                st.toast("Calculadora reiniciada")

with col_der:
    with st.container():
        st.subheader("📋 Resumen del Impacto")
        
        if st.session_state.lista_calculadora:
            df = pd.DataFrame(st.session_state.lista_calculadora)
            
            st.dataframe(
                df[["Tipo de prenda", "Cantidad (und)", "Peso total (kg)", "CO2 Evitado (kg)"]], 
                use_container_width=True, 
                hide_index=True,
                column_config={
                    "CO2 Evitado (kg)": st.column_config.NumberColumn(format="%.2f kg CO2e 🍃"),
                    "Peso total (kg)": st.column_config.NumberColumn(format="%.2f kg ⚖️")
                }
            )
            
            st.markdown(" ")
            st.subheader("🌸 Totales de Triple Impacto")
            
            tot_und = int(df["Cantidad (und)"].sum())
            tot_kg = round(df["Peso total (kg)"].sum(), 2)
            tot_co2 = round(df["CO2 Evitado (kg)"].sum(), 2)
            
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric(label="📦 Uniformes Recuperados", value=f"{tot_und} und")
            with m2:
                st.metric(label="♻️ Residuo Textil Evitado", value=f"{tot_kg} kg")
            with m3:
                st.metric(label="🍃 Huella de CO₂ Mitigada", value=f"{tot_co2} kg CO2e")
            
            # --- NUEVA SECCIÓN VISUAL DE EQUIVALENCIAS CORPORATIVAS ---
            st.markdown("---")
            st.subheader("🌍 Equivalencias de tu Impacto Ecológico")
            st.markdown("<p style='color: #705a5d; margin-bottom: 20px;'>Para entender mejor tu huella, mitigar esa cantidad de CO₂ equivale visualmente a:</p>", unsafe_allow_html=True)
            
            # Cálculos exactos basados en la EPA
            auto_km = round(tot_co2 / 0.25, 1)
            arboles_ano = round(tot_co2 / 22.0, 1)
            celulares_carga = int(tot_co2 / 0.008)
            
            eq1, eq2, eq3 = st.columns(3)
            
            with eq1:
                st.markdown(f"""
                <div class="eq-card">
                    <div class="eq-icon">🚗</div>
                    <div class="eq-value">{auto_km:,} km</div>
                    <div class="eq-text">Recorridos por un auto promedio sin emitir gases contaminantes.</div>
                </div>
                """, unsafe_allow_html=True)
                
            with eq2:
                st.markdown(f"""
                <div class="eq-card">
                    <div class="eq-icon">🌳</div>
                    <div class="eq-value">{arboles_ano:,} árboles</div>
                    <div class="eq-text">Absorbiendo carbono activamente de la atmósfera durante todo un año completo.</div>
                </div>
                """, unsafe_allow_html=True)
                
            with eq3:
                st.markdown(f"""
                <div class="eq-card">
                    <div class="eq-icon">🔋</div>
                    <div class="eq-value">{celulares_carga:,}</div>
                    <div class="eq-text">Baterías de smartphones cargadas por completo desde cero de forma limpia.</div>
                </div>
                """, unsafe_allow_html=True)
                
        else:
            st.markdown("""
            <div style='text-align:center; padding:40px; color:#7a5c62;'>
                <h4>✨ ¡Te damos la bienvenida!</h4>
                <p>Agrega las prendas que deseas procesar a la izquierda para ver en tiempo real cómo reduces el impacto ambiental de tu empresa corporativa.</p>
            </div>
            """, unsafe_allow_html=True)
