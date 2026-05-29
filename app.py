import streamlit as st
import psycopg2
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN (NEON)
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
    "horas_auditoria": 500.0,      # Módulo Fragilidad: Procesamiento por hora experta
    "infraestructura_tech": 250.0,  # Módulo Fragilidad: Soporte técnico y gestión
    "capital_respaldo": 1000.0     # Módulo Fragilidad: Blindaje por liquidez (M-Pesos)
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
# CONEXIÓN A LA MEMORIA INMUTABLE
# ==========================================
db_disponible = False
conn = None
cursor = None

try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    st.success("🔗 Sincronización con la base de datos central enraizada correctamente.")
    db_disponible = True
except Exception:
    db_disponible = False

# ==========================================
# ADUANA DE IDENTIDAD SOBERANA (Ostrom Principio 1)
# ==========================================
st.sidebar.header("🔑 PRINCIPIO 1: Fronteras")
nodo_id = st.sidebar.text_input("Código de Verificación del Nodo (Nodo_ID):", value="UNAM-OIKOS-GLOBAL-01")

# ==========================================
# CONMUTADOR DE FOCO METABÓLICO (TRINIDAD TRIDIMENSIONAL)
# ==========================================
st.markdown("---")
foco_metabolico = st.radio(
    "Seleccione la Dimensión del Diagnóstico de Coherencia:",
    ["Producción Industrial (UPR)", "Logística y Suministros (Termodinámica Comercial)", "Riesgo Regulatorio y Compliance (Motor de Fragilidad)"],
    horizontal=True
)

# ==========================================
# CONFIGURACIÓN DINÁMICA DEL RADAR (SISTEMA 4) SEGÚN EL FOCO
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 SISTEMA 4: Radar de Entorno")

if foco_metabolico == "Producción Industrial (UPR)":
    st.sidebar.markdown("*Monitoreo de perturbaciones exógenas de la infraestructura física (2020-2026)*")
    var_ext_1 = st.sidebar.slider("Riesgo de Choque Arancelario T-MEC (%):", 0, 100, 35)
    var_ext_2 = st.sidebar.slider("Índice de Canibalización por Insumo Asiático (%):", 0, 100, 50)
    var_ext_3 = st.sidebar.slider("Estrés de Capacidad Energética (Red CFE %):", 0, 100, 20)
    lambda_entorno = 1.0 + ((var_ext_1 + var_ext_2 + var_ext_3) / 300.0)

elif foco_metabolico == "Logística y Suministros (Termodinámica Comercial)":
    st.sidebar.markdown("*Monitoreo de latencia y estrangulamiento en redes de distribución*")
    var_ext_1 = st.sidebar.slider("Latencia en Puertos y Tráfico CDMX (%):", 0, 100, 40)
    var_ext_2 = st.sidebar.slider("Inflación y Volatilidad de Suministros (%):", 0, 100, 25)
    var_ext_3 = st.sidebar.slider("Cuellos de Botella Logísticos Globales (%):", 0, 100, 30)
    lambda_entorno = 1.0 + ((var_ext_1 + var_ext_2 + var_ext_3) / 300.0)

else:  # Motor de Fragilidad Regulatoria
    st.sidebar.markdown("*Vectorización NLP de modificaciones normativas en tiempo real (DOF / CNBV / GAFI)*")
    var_ext_1 = st.sidebar.slider("Tasa de Reformas e Impacto DOF (%):", 0, 100, 45)
    var_ext_2 = st.sidebar.slider("Intensidad de Fiscalización CNBV / Banxico (%):", 0, 100, 65)
    var_ext_3 = st.sidebar.slider("Presión Normativa GAFI / Lavado Internacional (%):", 0, 100, 30)
    lambda_entorno = 1.0 + ((var_ext_1 + var_ext_2 + var_ext_3) / 300.0)

# ==========================================
# SISTEMA 1: CAPTURA DE VARIABLES SEGÚN EL FOCO SELECCIONADO
# ==========================================
st.header(f"📥 SISTEMA 1: Diagnóstico de {foco_metabolico}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Flujos de Entrada e Inyección de Capacidad")
    if foco_metabolico == "Producción Industrial (UPR)":
        input_1 = st.number_input("Electricidad consumida (kWh):", min_value=0.0, value=120.0)
        input_2 = st.number_input("Diésel utilizado (Litros):", min_value=0.0, value=30.0)
        input_3 = st.number_input("Agua industrial incorporada (m³):", min_value=0.0, value=5.0)
        input_4 = st.number_input("Fuerza de trabajo aplicada (Horas-Hombre):", min_value=0.0, value=24.0)
        
        e_in_real = (
            (input_1 * FACTORES_CALIDAD["electricidad_kwh"]) +
            (input_2 * FACTORES_CALIDAD["diesel_litros"]) +
            (input_3 * FACTORES_CALIDAD["agua_m3"]) +
            (input_4 * FACTORES_CALIDAD["horas_hombre"])
        )
    elif foco_metabolico == "Logística y Suministros (Termodinámica Comercial)":
        input_1 = st.number_input("Unidades de Mercancía Entrantes (Volumen):", min_value=0.0, value=500.0)
        input_2 = st.number_input("Fuerza de Trabajo Logística (Horas-Hombre):", min_value=0.0, value=15.0)
        input_3 = st.number_input("Combustible de Distribución (Litros):", min_value=0.0, value=100.0)
        
        e_in_real = (
            (input_1 * FACTORES_CALIDAD
