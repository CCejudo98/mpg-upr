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
   # ==========================================
# SIMULADOR LOGÍSTICO NO LINEAL (SISTEMA 4)
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

# Parámetros cinéticos expuestos para el control del operador
st.markdown("### 🎛️ Parámetros de Control Cinético")
sc1, sc2, sc3 = st.columns(3)
with sc1:
    p_init = st.number_input("Masa Crítica Inicial ($x_0$):", min_value=1.0, value=max(1.0, excedente_neto))
with sc2:
    f_retro = st.slider("Retroalimentación Sintrópica ($r$):", 0.01, 3.0, 0.5)
with sc3:
    cap_medio = st.number_input("Límite de Capacidad del Entorno ($K$):", min_value=10.0, value=max(100.0, e_in_real * 1.5))

# EJECUCIÓN CONTINUA DE LA TRAYECTORIA (Evita que la pantalla quede vacía)
potencias, aceleraciones, estados = simular_sistema_transductivo(p_init, f_retro, cap_medio)

df_simulacion = pd.DataFrame({
    "Potencia Proyectada (W)": potencias,
    "Aceleración Cinética": aceleraciones
})

# PANEL DE RESULTADOS SIEMPRE VISIBLE
st.markdown("---")
st.subheader("🔮 Proyección Dinámica y Puntos de Quiebre del Nodo")

rc1, rc2, rc3 = st.columns(3)
with rc1:
    st.metric("Ciclos hasta Atractor/Saturación", len(df_simulacion))
with rc2:
    st.metric("Potencia Terminal Convergente", f"{potencias[-1]:,.2f} W")
with rc3:
    st.metric("Régimen de Salida", estados[-1])

# RENDERIZADO GRÁFICO AUTOMÁTICO
st.subheader("Evolución de la Masa Exergética Proyectada")
st.line_chart(df_simulacion[["Potencia Proyectada (W)"]])

st.subheader("Fuerza de Aceleración Interna (Segunda Derivada Discreta)")
st.area_chart(df_simulacion[["Aceleración Cinética"]])

# ALERTAS ONTOLÓGICAS
if "💥 Saturación Metaestable" in estados:
    st.warning("⚠️ CRÍTICO: La trayectoria proyectada colisionará con la finitud del entorno ($K$). Expansión de la variedad de Ashby requerida.")
else:
    st.success("💎 Homeostasis de largo plazo asegurada. El acoplamiento con el entorno es armónico.")

# BOTÓN DE REFRESCO SOBERANO (Opcional, para forzar el recálculo)
st.sidebar.markdown("---")
if st.sidebar.button("🔄 Recalibrar Matrices del Core"):
    st.rerun()
