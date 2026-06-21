import streamlit as st
import psycopg2
from datetime import datetime
import pandas as pd

# ==========================================
# VECTOR DE CONEXIÓN UNIFICADO Y SÍNCRONO
# ==========================================
DB_URL = "postgresql://neondb_owner:npg_4IuJofqBpE3v@ep-patient-pine-apfibhxx-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

FACTORES_CALIDAD = {
    "electricidad_kwh": 1000.0, "diesel_litros": 10500.0, "agua_m3": 150.0,
    "horas_hombre": 75.0, "suministro_unidad": 500.0, "horas_auditoria": 500.0,
    "infraestructura_tech": 250.0, "capital_respaldo": 1000.0, "informacion_bits": 850.0      
}

st.set_page_config(page_title="MPG - Exergy Core", page_icon="⚛️", layout="wide")

# ==========================================
# CÁPSULA ESTÉTICA: MODERNISMO NOIRE PURO
# ==========================================
st.markdown("""
<style>
    .stApp {
        background-color: #080808;
        color: #dcdcdc;
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #1a1a1a !important;
        border-right: 1px solid #2d2d2d !important;
    }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h4 {
        color: #f5f5f5 !important;
    }
    h1, h2, h3, h4, h5, h6, label {
        color: #f5f5f5 !important;
        font-weight: 500 !important;
        letter-spacing: -0.5px !important;
    }
    .stNumberInput input, .stTextInput input {
        background-color: #121212 !important;
        color: #ffffff !important;
        border: 1px solid #222222 !important;
        font-family: monospace !important;
        font-size: 16px !important;
    }
    hr {
        border-top: 1px solid #2d2d2d !important;
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚛️ MOTOR DE OPTIMIZACIÓN EXERGÉTICA")
st.caption("Cleronomía Avanzada // Consola Soberana de Diagnóstico y Control de Sistemas Viables Fuera del Equilibrio")

# ==========================================
# ENLACE CON EL LÓGOS DE DATOS
# ==========================================
db_disponible = False
conn = None
cursor = None

try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metric_history (
            id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            foco VARCHAR(100), e_in DOUBLE PRECISION, e_out DOUBLE PRECISION, efficiency DOUBLE PRECISION
        );
    """)
    conn.commit()
    st.sidebar.success("📡 Conexión síncrona con el Lógos central activa.")
    db_disponible = True
except Exception as e:
    st.sidebar.error(f"Fricción de enlace con DB: {e}")

# ==========================================
# ADUANA DE IDENTIDAD DEL OIKOS
# ==========================================
st.sidebar.header("🔑 SISTEMA 5: Soberanía")
nodo_id = st.sidebar.text_input("Identificador del Oikos (Nodo_ID):", value="UNAM-CLERONOMIC-CORE")

# ==========================================
# SELECCIÓN DEL CANAL METABÓLICO
# ==========================================
st.markdown("---")
foco_metabolico = st.radio(
    "Seleccione el Sector de Transducción Exergética:",
    [
        "Producción Industrial (UPR)", 
        "Logística y Suministros (Termodinámica Comercial)", 
        "Riesgo Regulatorio y Compliance (Motor de Fragilidad)",
        "Coherencia de Carteras y Activos (Matriz Exergética Financiera)"
    ],
    horizontal=True,
    key="foco_actual"
)

# Mapeo de consistencia para leer la base de datos común
foco_mapeado = "Producción y Fábrica" if "Industrial" in foco_metabolico else "Logística y Almacén" if "Logística" in foco_metabolico else "Cumplimiento Legal y Riesgos" if "Regulatorio" in foco_metabolico else "Inversiones y Dinero"

# ==========================================
# SISTEMA 4: RADAR DE PERTURBACIÓN AMBIENTAL
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 SISTEMA 4: Radar Termodinámico")
v_ext_1 = st.sidebar.slider("Estrés de Capacidad Estructural (%):", 0, 100, 25)
v_ext_2 = st.sidebar.slider("Variedad Inmanejable del Entorno (%):", 0, 100, 35)
lambda_entorno = 1.0 + ((v_ext_1 + v_ext_2) / 200.0)

# ==========================================
# ASIGNACIÓN DE ADQUISICIÓN DE DATOS EN TIEMPO REAL
# ==========================================
e_in_real, i_destroyed = 100000.0, 20000.0  # Valores base por si la DB está vacía

if db_disponible:
    try:
        cursor.execute("SELECT e_in, e_out FROM metric_history WHERE foco = %s ORDER BY timestamp DESC LIMIT 1", (foco_mapeado,))
        res = cursor.fetchone()
        if res: 
            e_in_real, i_destroyed = res[0], res[1]
    except Exception as read_err:
        st.sidebar.error(f"Fricción de lectura síncrona: {read_err}")

excedente_neto = e_in_real - i_destroyed
soberania_exergetica = (excedente_neto / e_in_real) * 100.0 if e_in_real > 0 else 0.0

st.markdown("---")
st.header(f"📥 SISTEMA 1 & 2: Estado del Flujo Heredado - {foco_mapeado}")
mc1, mc2, mc3 = st.columns(3)
with mc1:
    st.metric("Ingreso Exergético ($E_{in}$)", f"{e_in_real:,.2f} W")
with mc2:
    st.metric("Potencia Aniquilada ($I_{destroyed}$)", f"{i_destroyed:,.2f} W", delta="-Destrucción", delta_color="inverse")
with mc3:
    st.metric("Coeficiente de Soberanía ($S_e$)", f"{soberania_exergetica:.2f}%")

# ==========================================
# SIMULADOR LOGÍSTICO NO LINEAL (SISTEMA 4 AVANZADO)
# ==========================================
def simular_sistema_transductivo(potencia_inicial, factor_retroalimentacion, capacidad_medio, ciclos=30):
    x = potencia_inicial
    potencias = []
    aceleraciones = []
    estados = []
    
    for ciclo in range(1, ciclos + 1):
        variacion = factor_retroalimentacion * x * (1 - (x / capacidad_medio))
        x_siguiente = x + variacion
        
        if ciclo == 1:
            aceleracion = 0.0
        else:
            aceleracion = (x_siguiente - x) - (potencias[-1] - (potencias[-2] if len(potencias) > 1 else potencia_inicial))
            
        potencias.append(x_siguiente)
        aceleraciones.append(aceleracion)
        
        if x_siguiente >= capacidad_medio * 0.95:
            estado = "💥 Saturación Metaestable"
        elif aceleracion > 0.01:
            estado = "⚡ Aceleración Expansiva"
        else:
            estado = "🌱 Acumulación Homeostática"
        estados.append(estado)
        
        if abs(x_siguiente - x) < 1e-6 and ciclo > 10:
            break
        x = x_siguiente
        
    return potencias, aceleraciones, estados

st.markdown("---")
st.header("🔮 SISTEMA 4: Proyección Dinámica y Atractores")
st.markdown("*Ajuste los parámetros cinéticos para modelar la trayectoria del Oikos fuera del equilibrio*")

sc1, sc2, sc3 = st.columns(3)
with sc1:
    p_init = st.number_input("Masa Crítica Inicial ($x_0$):", min_value=1.0, value=max(1.0, excedente_neto))
with sc2:
    f_retro = st.slider("Retroalimentación Sintrópica ($r$):", 0.01, 3.0, max(0.1, 2.0 - lambda_entorno))
with sc3:
    cap_medio = st.number_input("Límite de Capacidad del Entorno ($K$):", min_value=10.0, value=max(100.0, e_in_real * 1.5))

# Ejecución continua de la simulación
potencias, aceleraciones, estados = simular_sistema_transductivo(p_init, f_retro, cap_medio)

df_simulacion = pd.DataFrame({
    "Potencia Proyectada (W)": potencias,
    "Aceleración Cinética": aceleraciones
})

rc1, rc2, rc3 = st.columns(3)
with rc1:
    st.metric("Ciclos hasta Atractor", len(df_simulacion))
with rc2:
    st.metric("Potencia Terminal Convergente", f"{potencias[-1]:,.2f} W")
with rc3:
    st.metric("Régimen de Salida Proyectado", estados[-1])

st.subheader("Evolución de la Masa Exergética Proyectada")
st.line_chart(df_simulacion[["Potencia Proyectada (W)"]])

st.subheader("Fuerza de Aceleración Interna (Segunda Derivada Discreta)")
st.area_chart(df_simulacion[["Aceleración Cinética"]])

if "💥 Saturación Metaestable" in estados:
    st.warning("⚠️ CRÍTICO: La trayectoria proyectada colisionará con la finitud del entorno ($K$). Se requiere expansión de la variedad de Ashby.")
else:
    st.success("💎 Homeostasis predictiva asegurada. El acoplamiento con el medio es armónico.")
