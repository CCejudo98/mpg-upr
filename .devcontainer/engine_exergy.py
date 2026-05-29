import streamlit as st
import psycopg2
import pandas as pd
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN INMUTABLE (NEON)
# ==========================================
DB_URL = "postgresql://alexcejudo98:ep_dark_sound_p5p4wzrm@ep-dark-sound-a5x836m4.us-east-2.aws.neon.tech/neondb?sslmode=require"

# ==========================================
# PARÁMETROS BIOFÍSICOS E INFORMACIONALES (𝛽)
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

st.set_page_config(page_title="MPG - Exergy Core", page_icon="⚛️", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #080808; color: #dcdcdc; font-family: 'SF Pro Display', sans-serif; }
    [data-testid="stSidebar"] { background-color: #1a1a1a !important; border-right: 1px solid #2d2d2d !important; }
    h1, h2, h3, h4, h5, h6, label { color: #f5f5f5 !important; }
    .stNumberInput input, .stTextInput input { background-color: #121212 !important; color: #ffffff !important; border: 1px solid #222222 !important; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

st.title("⚛️ MOTOR DE OPTIMIZACIÓN EXERGÉTICA")
st.caption("Consola Soberana: Control de Flujos, Inmunidad Fiscal y Acumulación Negentrópica")

# ==========================================
# ENLACE CON EL LÓGOS (DB)
# ==========================================
db_disponible = False
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exergy_history (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            foco VARCHAR(100),
            e_in DOUBLE PRECISION,
            i_destroyed DOUBLE PRECISION,
            total_value_mxn DOUBLE PRECISION,
            tax_deductible_total DOUBLE PRECISION
        );
    """)
    conn.commit()
    db_disponible = True
    st.sidebar.success("🔗 Lógos Central Activo")
except:
    db_disponible = False
    st.sidebar.warning("📡 Modo Autónomo Localizado")

# ==========================================
# SECTOR Y RADAR
# ==========================================
foco_metabolico = st.radio("Sector de Transducción:", ["Producción Industrial (UPR)", "Logística", "Regulatorio", "Financiero"], horizontal=True)
lambda_entorno = 1.2 # Factor simplificado de entorno

# ==========================================
# SISTEMA 1: CAPTURA CON FILTRO FISCAL
# ==========================================
st.header(f"📥 SISTEMA 1: Inyección Exergética - {foco_metabolico}")

with st.form("flujo_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        in_nominal = st.number_input("Inyección de Energía/Capital (W o MXN):", value=100.0)
    with col2:
        in_friccion = st.number_input("Destrucción de Energía (Entropía W):", value=10.0)
    with col3:
        es_deducible = st.checkbox("¿Es gasto deducible por innovación?", help="Suma al escudo fiscal del Oikos.")
    
    submit = st.form_submit_button("Sellar en el Lógos")

# ==========================================
# SISTEMA 2 Y 3: DIAGNÓSTICO Y ARBITRAJE
# ==========================================
if submit:
    excedente = in_nominal - in_friccion
    valor_deducible = in_nominal if es_deducible else 0.0
    
    if db_disponible:
        cursor.execute("INSERT INTO exergy_history (foco, e_in, i_destroyed, total_value_mxn, tax_deductible_total) VALUES (%s, %s, %s, %s, %s);",
                       (foco_metabolico, in_nominal, in_friccion, in_nominal, valor_deducible))
        conn.commit()
        st.success("Transacción sellada. El Sistema 3 ha recalibrado el escudo fiscal.")

# ==========================================
# SISTEMA 5: REGISTRO PSICOHISTÓRICO Y ESCUDO FISCAL
# ==========================================
st.markdown("---")
st.header("📡 SISTEMA 5: Registro Psicohistórico")

if db_disponible:
    df = pd.read_sql("SELECT * FROM exergy_history", conn)
    
    c1, c2 = st.columns(2)
    with c1:
        st.line_chart(df[['e_in', 'i_destroyed']])
    with c2:
        # Cálculo del Escudo Fiscal (ISR 30%)
        escudo_fiscal = df['tax_deductible_total'].sum() * 0.30
        st.metric("Escudo Fiscal Acumulado (ISR 30%)", f"${escudo_fiscal:,.2f} MXN", 
                  help="Soberanía financiera recuperada mediante optimización fiscal tecnológica.")
        
        upr_acumulada = (df['e_in'] - df['i_destroyed']).sum()
        st.metric("Potencia Regenerativa Acumulada ($\Phi_{UPR}$)", f"{upr_acumulada:,.2f} W-Neg")
