import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN ESTÉTICA (Replica el CSS del archivo) ---
st.set_page_config(page_title="Content OS - CEO Dashboard", layout="wide")

st.markdown("""
    <style>
    /* El "Code Vibe" basado en tu estructura */
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #00FF41 !important; font-family: 'Courier New', monospace !important; }
    
    /* Estilo de Tarjetas */
    .metric-card {
        background-color: #111;
        border: 1px solid #00FF41;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
    }
    .metric-value { font-size: 24px; font-weight: bold; color: #fff !important; }
    .metric-label { font-size: 12px; text-transform: uppercase; color: #00FF41; }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN (TABS) ---
tab_ceo, tab_bonos, tab_equipo = st.tabs(["Panel Cliente / CEO", "Bonos — Vista Interna", "Vista Equipo"])

# ==========================
# VISTA CEO
# ==========================
with tab_ceo:
    st.header(">> DESEMPEÑO_DEL_CANAL - ABRIL 2025")
    
    # Métricas Top (Metric Grid)
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card"><p class="metric-label">Ingresos</p><p class="metric-value">$1,840</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><p class="metric-label">Videos</p><p class="metric-value">24</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><p class="metric-label">Retención Global</p><p class="metric-value">38%</p></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><p class="metric-label">Seguidores</p><p class="metric-value">+2,340</p></div>', unsafe_allow_html=True)

    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader(">> INGRESOS_POR_RED")
        # Aquí puedes usar st.bar_chart con tus datos de Windsor.ai
        chart_data = pd.DataFrame({'Red': ['YT', 'FB', 'IG', 'TK'], 'USD': [1100, 480, 120, 140]})
        st.bar_chart(chart_data.set_index('Red'))

    with col_right:
        st.subheader(">> METAS_DE_ABRIL")
        st.write("YT: Horas de reproducción (82%)")
        st.progress(0.82)
        st.write("FB: Minutos reproducidos (65%)")
        st.progress(0.65)

# ==========================
# VISTA BONOS (Interna)
# ==========================
with tab_bonos:
    st.header(">> CALCULO_DE_BONOS_ABRIL")
    
    # Tabla de bonos (reemplaza con tu lógica de IA)
    st.markdown("### Bono Individual por Persona")
    bonos_df = pd.DataFrame({
        'Persona': ['Lucía C.', 'Marcos R.', 'Andrea S.', 'José P.'],
        'KPI': ['Ret > 35%', 'Crec. RPM', 'Ret 30s > 50%', 'Ret > 35%'],
        'Estado': ['✓ 51%', '✓ +18%', '⏳ 48%', '✗ 29%'],
        'Bono USD': [25.76, 25.76, 25.76, 0.00]
    })
    st.table(bonos_df)
    
    st.warning("🔒 Bono grupal ($55.20) bloqueado hasta cumplir metas de YT y FB")

# ==========================
# VISTA EQUIPO (Motivacional)
# ==========================
with tab_equipo:
    st.header(">> ESTATUS_EQUIPO")
    
    st.info("¡Van increíble! YouTube está al 82%, un empuje más en Facebook y liberamos el bono.")
    
    # Grid de KPIs individuales con barras de progreso
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Lucía C.** - Retención: 51%")
        st.progress(0.51)
        st.write("Meta: >35% | ¡La estás rompiendo! 🔥")
        
    with c2:
        st.markdown("**José P.** - Retención: 29%")
        st.progress(0.29)
        st.write("Meta: >35% | Revisemos el guion esta semana")
