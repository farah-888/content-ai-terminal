import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN ESTÉTICA ---
st.set_page_config(page_title="Content Intelligence", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    [data-testid="stSidebar"] { background-color: #111; border-right: 1px solid #00FF41; }
    h1, h2, h3, p, span, div, label { color: #00FF41 !important; font-family: 'Courier New', monospace !important; }
    .stDataFrame { border: 1px solid #00FF41; }
    .stTextInput>div>div>input { background-color: #000; color: #00FF41; border: 1px solid #00FF41; }
    </style>
""", unsafe_allow_html=True)

st.title(">> CONTENT_INTELLIGENCE_TERMINAL_V1.1")

# --- CONEXIÓN DE DATOS ---
st.sidebar.header("CONFIG_NETWORK")
fuente = st.sidebar.selectbox('FUENTE_DE_DATOS', ['API_WINDSOR_AI', 'DATO_SIMULADO'])

# Aquí evitamos el NameError definiendo df siempre
if fuente == 'DATO_SIMULADO':
    df = pd.DataFrame({
        'video_title': ['Hook_Venta_01', 'Tutorial_IA', 'Vlog_Retencion'],
        'avd_percent': [65, 42, 78],
        'retention_3s': [88, 55, 92],
        'sales_usd': [1200, 300, 2500],
        'platform': ['TikTok', 'YouTube', 'Meta']
    })
else:
    # REEMPLAZA ESTA URL por tu link de Windsor.ai cuando lo tengas
    url_api = "https://api.windsor.ai/tu_link_aqui" 
    try:
        df = pd.read_json(url_api)
    except:
        st.warning(">> ESPERANDO_CONEXION_API... (USANDO DATOS TEMPORALES)")
        df = pd.DataFrame({'status': ['No connected']})

# --- VISUALIZACIÓN ---
st.subheader(">> METRICAS_MACRO")
st.table(df) # Se ve mucho más "terminal" que el dataframe interactivo

# --- IA ANALYSIS ---
st.subheader(">> AI_CONTENT_ANALYSIS")
query = st.text_input("QUERY_TERMINAL:", placeholder="ej. ¿Por qué bajó la retención?")

if query:
    if 'status' in df.columns:
        st.error(">> ERROR: CONECTA EL API PARA ANALIZAR")
    else:
        st.info(f">> PROCESANDO: '{query}' en {len(df)} registros...")
        # Aquí irá el comando de la IA
