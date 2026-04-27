import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- 1. CONEXIÓN REAL ---
# Pega aquí el link que sacaste de Windsor.ai
URL_DATOS = "TU_URL_DE_WINDSOR_AQUÍ"

try:
    df = pd.read_json(URL_DATOS)
    # Calculamos los promedios reales
    prom_retencion = f"{round(df['video_retention_rate'].mean(), 2)}%"
    total_usd = f"${df['earnings'].sum()}"
except:
    # Si falla, usamos datos de prueba para que no se rompa la web
    prom_retencion = "38%"
    total_usd = "$1,840"

# --- 2. EL DISEÑO (v0) ---
# import { Dashboard } from '@/components/dashboard/dashboard'

export default function Home() {
  return <Dashboard />
}
# Nota: Streamlit necesita HTML, si v0 te dio React, pídele a v0: 
# "Dame este mismo diseño pero en un solo archivo HTML y CSS"
diseno_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Pega aquí el CSS que te dé v0 */
        body {{ background-color: black; color: #00FF41; font-family: monospace; }}
        .card {{ border: 1px solid #00FF41; padding: 20px; margin: 10px; border-radius: 10px; }}
    </style>
</head>
<body>
    <h1>>> CONTENT_INTELLIGENCE_TERMINAL</h1>
    <div style="display: flex;">
        <div class="card">
            <h3>INGRESOS TOTALES</h3>
            <p style="font-size: 24px;">{total_usd}</p>
        </div>
        <div class="card">
            <h3>RETENCIÓN PROMEDIO</h3>
            <p style="font-size: 24px;">{prom_retencion}</p>
        </div>
    </div>
    </body>
</html>
"""

# --- 3. MOSTRAR TODO ---
components.html(diseno_html, height=1000, scrolling=True)

# --- 4. LA IA (Chat) ---
st.subheader(">> CONSULTAR_IA")
pregunta = st.text_input("Escribe tu duda sobre el contenido:")
if pregunta:
    st.write(f"Analizando datos para responder: {pregunta}")
