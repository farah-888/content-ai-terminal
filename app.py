import streamlit as st
import pandas as pd

# Estética Terminal / Hacker
st.set_page_config(page_title="Content OS", layout="wide")
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    header, footer { visibility: hidden; }
    h1, h2, h3, p, span { color: #00FF41 !important; font-family: 'Courier New', monospace !important; }
    .stTextInput>div>div>input { background-color: #111; color: #00FF41; border: 1px solid #00FF41; }
    </style>
""", unsafe_allow_html=True)

st.title(">> CONTENT_INTELLIGENCE_TERMINAL_V1")

# Selector de Fuente de Datos
option = st.sidebar.selectbox('CONECTAR_FUENTE', ['API_WINDSOR_AI', 'DUMMY_DATA_TEST'])

if option == 'DUMMY_DATA_TEST':
    # Datos de ejemplo para que veas el diseño
    df = pd.DataFrame({
        'video_title': ['Hook_Venta_01', 'Tutorial_IA', 'Vlog_Retencion'],
        'avd_percent': [65, 42, 78],
        'retention_3s': [88, 55, 92],
        'sales_conversion': [1200, 300, 2500],
        'platform': ['TikTok', 'YouTube', 'Meta']
    })
    st.write("--- DATA_LOADED_SUCCESSFULLY ---")
    st.dataframe(df)

# Sección de IA
st.subheader(">> AI_CONTENT_ANALYSIS")
query = st.text_input("CONSULTA_A_LA_IA:")
if query:
    st.info(f"Analizando patrones en {len(df)} videos... (Aquí conectarás tu API de OpenAI)")
    # Aquí es donde la IA te dirá por qué el video de 78% retención vendió más.
