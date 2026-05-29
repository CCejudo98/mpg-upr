import streamlit as st
import psycopg2
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN INMUTABLE (NEON)
# ==========================================
DB_URL = "postgresql://alexcejudo98:ep_dark_sound_p5p4wzrm@ep-dark-sound-a5x836m4.us-east-2.aws.neon.tech/neondb?sslmode=require"

# ==========================================
# CONFIGURACIÓN DE PARÁMETROS BIOFÍSICOS E INFORMACIONALES (𝛽)
# ==========================================
FACTORES_CALIDAD = {
    "electricidad_kwh": 1000.0,    
    "diesel_litros": 10500.0,
    "agua_m3": 150.0,
    "horas_hombre": 75.0,
    "suministro_unidad": 500.0,    
    "horas_auditoria": 500.0,      
    "infraestructura_tech": 250.0,  
    "capital_respaldo": 1000.0,
    "informacion_bits": 850.0      
}

st.set_page_config(page_title="MPG - Motor Homeostático", page_icon="⚡", layout="wide")

# ==========================================
# CÁPSULA ESTÉTICA: MODERNISMO NOIRE AVANZADO
# ==========================================
st.markdown("""
<style>
    /* Fondo del Contenedor Principal (Negro Absoluto) */
    .stApp {
        background-color: #080808;
        color: #dcdcdc;
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }
    
    /* LA BARRA LATERAL: Gris Oxford Coherente */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #1a1a1a !important;
        border-right: 1px solid #2d2d2d !important;
    }
    
    /* Forzar color en componentes de la barra sidebar */
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h4 {
        color: #f5f5f5 !important;
    }

    /* Tipografía Rigurosa y Sobria */
    h1, h2, h3, h4, h5, h6, label {
        color: #f5f5f5 !important;
        font-weight: 500 !important;
        letter-spacing: -0.5px !important;
    }
    
    /* Entradas Numéricas Acero Industrial */
    .stNumberInput input, .stTextInput input {
        background-color: #121212 !important;
        color: #ffffff !important;
        border: 1px solid #222222 !important;
        font-family: monospace !important;
        font-size: 16px !important;
    }
    
    /* Estilización de los Deslizadores */
    .stSlider {
        padding-bottom: 20px !important;
    }

    /* Líneas Divisoras de Baja Entropía */
    hr {
        border-top: 1px solid #2d2d2d !important;
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ MOTOR DE GOBERNABILIDAD HOMEOSTÁTICA")
st.caption("Cleronomía Aplicada: Gestión Multidimensional de Sistemas Viables, Bienes Comunes e Inmunidad ante el Riesgo")

# ==========================================
# CONEXIÓN Y CREACIÓN DE ESTRUCTURAS INMUTABLES
# ==========================================
db_disponible = False
conn = None
cursor = None

try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metric_history (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            e_in DOUBLE PRECISION,
            e_out DOUBLE PRECISION,
            efficiency DOUBLE PRECISION
        );
    """)
    conn.commit()
    st.success("🔗 Sincronización con la base de datos central enraizada correctamente.")
    db_disponible = True
except Exception as e:
    st.sidebar.error(f"Fricción de enlace con DB: {e}")
    db_disponible = False

# ==========================================
# ADUANA DE IDENTIDAD SOBERANA (Ostrom Principio 1)
# ==========================================
st.sidebar.header("🔑 PRINCIPIO 1: Fronteras")
nodo_id = st.sidebar.text_input("Código de Verificación del Nodo (Nodo_ID):", value="UNAM-OIKOS-GLOBAL-01")

# ==========================================
# CONMUTADOR DE FOCO METABÓLICO (TETRADIMENSIONAL)
# ==========================================
st.markdown("---")
foco_metabolico = st.radio(
    "Seleccione la Dimensión del Diagnóstico de Coherencia:",
    [
        "Producción Industrial (UPR)", 
        "Logística y Suministros (Termodinámica Comercial)", 
        "Riesgo Regulatorio y Compliance (Motor de Fragilidad)",
        "Coherencia de Carteras y Activos (Matriz Exergética Financiera)"
    ],
    horizontal=True
)

# ==========================================
# CONFIGURACIÓN DINÁMICA DEL RADAR (SISTEMA 4)
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 SISTEMA 4: Radar de Entorno")

if foco_metabolico == "Producción Industrial (UPR)":
    st.sidebar.markdown("*Monitoreo de perturbaciones exógenas de la infraestructura física (2020-2026)*")
    var_ext_1 = st.sidebar.slider("Riesgo de Choque Arancelario T-MEC (%):", 0, 100, 35)
    var_ext_2 = st.sidebar.
