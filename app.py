import streamlit as st
import pandas as pd

# 1. Configuración de la página con título e icono web de hojas verdes
st.set_page_config(
    page_title="Calculadora Sostenible Eco-Impacto", 
    page_icon="🌱", 
    layout="wide"
)

# Estilos CSS personalizados para darle vida y quitar la frialdad industrial
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    h1 { color: #1e4d2b; font-family: 'Helvetica Neue', sans-serif; }
    h3 { color: #2e7d32; }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #1b5e20; color: white; }
    </style>
""", unsafe_allow_html=True)

# BASE DE DATOS MAESTRA COMPLETA (Tus 56 prendas exactas)
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

# --- ENCABEZADO ILUSTRATIVO ---
st.title("🌱 Sistema de Medición Ecológica: Valorización Textil")
st.caption("Plataforma interactiva para el cálculo instantáneo de huella de carbono evitada mediante Upcycling.")

st.markdown("---")

# Estructura en 2 columnas amplias y estilizadas
col_izq, col_der = st.columns([1.1, 2], gap="large")

with col_izq:
    # Contenedor visual para el formulario de entrada
    with st.container(border=True):
        st.subheader("📥 Registro de Lote")
        
        prenda_sel = st.selectbox("👔 Tipo de Prenda Textil", options=sorted(list(bd_factores_completa.keys())))
        
        c1, c2 = st.columns(2)
        with c1:
            cantidad = st.number_input("🔢 Cantidad (und)", min_value=1, value=100, step=10)
        with c2:
            peso_total = st.number_input("⚖️ Peso Total (kg)", min_value=0.1, value=43.0, step=1.0)
        
        # Muestra el indicador del factor ecológico actual de forma sutil
        factor_actual = bd_factores_completa.get(prenda_sel, 5.0)
        st.info(f"💡 **Factor asignado:** {factor_actual} kg CO2e por cada kilo de {prenda_sel}.")
        
        st.markdown(" ")
        
        # Botones estéticos de control
        c_btn1, c_btn2 = st.columns(2)
        with c_btn1:
            if st.button("➕ Añadir Lote", use_container_width=True):
                st.session_state.lista_calculadora.append({
                    "Tipo de prenda": prenda_sel,
                    "Cantidad (und)": int(cantidad),
                    "Peso total (kg)": round(peso_total, 2),
                    "Factor Eco": factor_actual,
                    "CO2 Evitado (kg)": round(peso_total * factor_actual, 2)
                })
                st.toast(f"✨ ¡{prenda_sel} agregada con éxito!")
                
        with c_btn2:
            if st.button("🗑️ Reiniciar", use_container_width=True):
                st.session_state.lista_calculadora = []
                st.toast("Calculadora limpia")

with col_der:
    st.subheader("📋 Panel de Monitoreo")
    
    if st.session_state.lista_calculadora:
        df = pd.DataFrame(st.session_state.lista_calculadora)
        
        # Tabla interactiva con colores y diseño limpio
        st.dataframe(
            df, 
            use_container_width=True, 
            hide_index=True,
            column_config={
                "CO2 Evitado (kg)": st.column_config.NumberColumn(format="%d 🍃"),
                "Peso total (kg)": st.column_config.NumberColumn(format="%d kg")
            }
        )
        
        # --- BLOQUE VISUAL DE INDICADORES (TARJETAS DE TRIPLE IMPACTO) ---
        st.markdown(" ")
        st.subheader("📊 Métricas de Impacto Acumulado")
        
        tot_und = int(df["Cantidad (und)"].sum())
        tot_kg = round(df["Peso total (kg)"].sum(), 2)
        tot_co2 = round(df["CO2 Evitado (kg)"].sum(), 2)
        
        # Creamos tres tarjetas con fondo visual utilizando columnas de Streamlit
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="📦 Total de Prendas Salvadas", value=f"{tot_und} unidades", delta="Textil recuperado")
        with m2:
            st.metric(label="♻️ Peso Neto Desviado del Vertedero", value=f"{tot_kg} kg", delta="Materia prima viva")
        with m3:
            # Resaltamos con un color verde el indicador clave de impacto de carbono
            st.metric(label="🍃 Huella de CO₂ Evitada Total", value=f"{tot_co2} kg CO2e", delta="Mitigación Ambiental", delta_color="normal")
            
        # Mensaje de motivación ecológico dinámico basado en el éxito del conteo
        st.success(f"🌍 ¡Gran trabajo! Con este proyecto se está evitando el equivalente a la emisión de gases de un auto promedio manejando por {round(tot_co2 * 4, 1)} kilómetros.")
            
    else:
        # Estado vacío interactivo con diseño amigable
        st.markdown("""
        <div style='text-align:center; padding:40px; border:2px dashed #b7d7b7; background-color:#f4fbf4; border-radius:12px; color:#3d6346;'>
            <h3>👋 ¡Hola! La calculadora ambiental está lista para operar.</h3>
            <p>Selecciona una prenda a la izquierda y presiona el botón verde para comenzar a trazar tu impacto sustentable.</p>
        </div>
        """, unsafe_allow_html=True)
