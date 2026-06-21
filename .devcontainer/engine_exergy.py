import streamlit as st
import psycopg2
from datetime import datetime
import pandas as pd

# CONFIGURACIÓN DE CONEXIÓN UNIFICADA
DB_URL = "postgresql://neondb_owner:npg_4IuJofqBpE3v@ep-patient-pine-apfibhxx-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

FACTORES_CALIDAD = {
    "electricidad_kwh": 1000.0, "diesel_litros": 10500.0, "agua_m3": 150.0,
    "horas_hombre": 75.0, "suministro_unidad": 500.0, "horas_auditoria": 500.0,
    "infraestructura_tech": 250.0, "capital_respaldo": 1000.0, "informacion_bits": 850.0      
}

st.set_page_config(page_title="MPG - Exergy Core", page_icon="⚛️", layout="wide")

st.markdown("<style>.stApp { background-color: #080808; color: #dcdcdc; font-family: monospace; }</style>", unsafe_allow_html=True)
st.title("⚛️ MOTOR DE OPTIMIZACIÓN EXERGÉTICA")
st.caption("Sistema 5: Consola Soberana de Diagnóstico Central")

db_disponible = False
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

foco_metabolico = st.radio("Sector de Transducción:", ["Producción Industrial (UPR)", "Logística y Suministros (Termodinámica Comercial)", "Riesgo Regulatorio y Compliance (Motor de Fragilidad)", "Coherencia de Carteras y Activos (Matriz Exergética Financiera)"], horizontal=True)

# Mapear foco del Core al foco comercial/operativo para consistencia en DB
foco_mapeado = "Producción y Fábrica" if "Industrial" in foco_metabolico else "Logística y Almacén" if "Logística" in foco_metabolico else "Cumplimiento Legal y Riesgos" if "Regulatorio" in foco_metabolico else "Inversiones y Dinero"

# SISTEMA 4: RADAR
lambda_entorno = 1.2 # Simplificado para acoplamiento directo

# Traer último dato registrado por las otras apps para inicializar balance
e_in_real, i_destroyed = 100000.0, 20000.0
if db_disponible:
    try:
        cursor.execute("SELECT e_in, e_out FROM metric_history WHERE foco = %s ORDER BY timestamp DESC LIMIT 1", (foco_mapeado,))
        res = cursor.fetchone()
        if res: e_in_real, i_destroyed = res[0], res[1]
    except: pass

excedente_neto = e_in_real - i_destroyed
soberania_exergetica = (excedente_neto / e_in_real) * 100.0 if e_in_real > 0 else 0.0

st.metric("Coeficiente de Soberanía ($S_e$) heredado en Tiempo Real", f"{soberania_exergetica:.2f}%")

# SIMULADOR LOGÍSTICO NO LINEAL
def simular_sistema_transductivo(potencia_inicial, factor_retroalimentacion, capacidad_medio, ciclos=30):
    x = potencia_inicial
    potencias = []
    for _ in range(ciclos):
        x = x + factor_retroalimentacion * x * (1 - (x / capacidad_medio))
        potencias.append(x)
    return potencias

if st.button("⚡ Ejecutar Proyección Dinámica del Nodo"):
    trayectoria = simular_sistema_transductivo(excedente_neto, 0.5, e_in_real * 1.5)
    st.line_chart(pd.DataFrame({"Potencia Proyectada (W)": trayectoria}))
