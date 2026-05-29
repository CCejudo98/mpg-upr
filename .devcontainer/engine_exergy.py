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
    "electricidad_kwh": 1000.0, "diesel_litros": 10500.0, "agua_m3": 150.0,
    "horas_hombre": 75.0, "suministro_unidad": 500.0, "horas_auditoria": 500.0,
    "infraestructura_tech": 250.0, "capital_respaldo": 1000.0, "informacion_bits": 850.0
}

COSTOS_MONETARIOS = {
    "Producción Industrial (UPR)": 0.0045,
    "Logística y Suministros (Termodinámica Comercial)": 1.25,
    "Riesgo Regulatorio y Compliance (Motor de Fragilidad)": 2.50,
    "Coherencia de Carteras y Activos (Matriz Exergética Financiera)": 5.00
}

st.set_page_config(page_title="MPG - Exergy Core", page_icon="⚛️", layout="wide")

# ==========================================
# CÁPSULA ESTÉTICA: MODERNISMO NOIRE PURO
# ==========================================
st.markdown("""
<style>
    .stApp { background-color: #080808; color: #dcdcdc; font-family: 'SF Pro Display', sans-serif; }
    [data-testid="stSidebar"] { background-color: #1a1a1a !important; border-right: 1px solid #2d2d2d !important; }
    h1, h2, h3 { color: #f5f5f5 !important; font-weight: 500 !important; }
    .stNumberInput input { background-color: #121212 !important; color: #ffffff !important; border: 1px solid #222 !important; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

st.title("⚛️ MOTOR DE OPTIMIZACIÓN EXERGÉTICA")
st.caption("Cleronomía Avanzada // Consola Soberana de Diagnóstico")

# ==========================================
# CONEXIÓN A NEON
# ==========================================
db_disponible = False
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS exergy_history (id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, foco VARCHAR(100), e_in DOUBLE PRECISION, i_destroyed DOUBLE PRECISION, efficiency DOUBLE PRECISION);")
    conn.commit()
    db_disponible = True
except: st.sidebar.error("Fricción de enlace con el Lógos")

# ==========================================
# SISTEMA 5: IDENTIDAD
# ==========================================
foco_metabolico = st.radio("Sector:", ["Producción Industrial (UPR)", "Logística y Suministros (Termodinámica Comercial)", "Riesgo Regulatorio y Compliance (Motor de Fragilidad)", "Coherencia de Carteras y Activos (Matriz Exergética Financiera)"], horizontal=True)

# --- RADAR TERMODINÁMICO (SISTEMA 4) ---
# [Aquí se mantiene toda tu lógica original de sliders v_ext_1, v_ext_2, v_ext_3]
lambda_entorno = 1.05 # Simplificado para el ejemplo

# --- SISTEMA 1 Y 2 (ENTRADAS Y BALANCE) ---
# [Aquí se mantiene tu lógica original de inputs in_1...in_4 y f_1, f_2]
e_in_real = 1000.0 # Placeholder
i_destroyed = 200.0 # Placeholder
excedente_neto = e_in_real - i_destroyed
eficiencia_real = (excedente_neto / e_in_real) * 100.0

# ==========================================
# SISTEMA 3: ARBITRAJE DE INMUNIDAD OPERATIVA (AUDITORÍA FISCAL)
# ==========================================
st.markdown("---")
st.header("⚙️ SISTEMA 3: Auditoría de Directiva Fiscal Externa")

def obtener_directiva_cliente(foco):
    if db_disponible:
        cursor.execute("SELECT fiscal_investment FROM public_fiscal_stats WHERE foco = %s ORDER BY timestamp DESC LIMIT 1", (foco,))
        res = cursor.fetchone()
        return res[0] if res else 0.0
    return 0.0

ac1, ac2 = st.columns(2)
with ac1: r_maint = st.slider("🛡️ Ajuste Auditoría (Mantenimiento):", 5, 40, 15)
with ac2: r_assets = st.slider("📈 Ajuste Auditoría (Activos):", 5, 40, 15)

directiva_fiscal_externa = obtener_directiva_cliente(foco_metabolico)
impacto_fiscal_porcentaje = (directiva_fiscal_externa / excedente_neto * 100) if excedente_neto > 0 else 0
res_total = r_maint + r_assets + impacto_fiscal_porcentaje
r_slack = max(0, 100 - res_total)

bloqueo_auditoria = False
if res_total > 95:
    st.error("⚠️ ALERTA DE SISTEMA: La carga estructural supera la viabilidad del nodo.")
    bloqueo_auditoria = True
else:
    UMBRAL_FISCAL_CRITICO = 0.40
    if directiva_fiscal_externa > (excedente_neto * UMBRAL_FISCAL_CRITICO):
        st.error(f"🚨 ALERTA DE AUDITORÍA: La directiva (${directiva_fiscal_externa:,.2f}) excede el umbral de soberanía.")
        bloqueo_auditoria = True

if not bloqueo_auditoria:
    dc1, dc2, dc3, dc4, dc5 = st.columns(5)
    data_display = [("Mantenimiento", excedente_neto*(r_maint/100)), ("Activos", excedente_neto*(r_assets/100)), ("Directiva Fiscal", directiva_fiscal_externa), ("Holgura", excedente_neto*(r_slack/100)), ("Viabilidad", excedente_neto*(max(0, 100-res_total)/100))]
    
    for col, (t, val) in zip([dc1, dc2, dc3, dc4, dc5], data_display):
        with col:
            st.markdown(f"<div style='background: #111; padding: 10px;'>{t.upper()}<br><b>{val:,.0f}W</b></div>", unsafe_allow_html=True)
            
    if st.button("💾 Validar y Sellar Auditoría"):
        if db_disponible:
            cursor.execute("INSERT INTO exergy_history (foco, e_in, i_destroyed, efficiency) VALUES (%s, %s, %s, %s);", (foco_metabolico, e_in_real, i_destroyed, eficiencia_real))
            conn.commit()
            st.success("✅ Auditoría completada.")

# ==========================================
# SISTEMA 5: REGISTRO PSICOHISTÓRICO (HISTORIAL UPR)
# ==========================================
st.markdown("---")
st.header("📡 SISTEMA 5: Registro Psicohistórico de la UPR")
st.markdown("*Evolución temporal del vector de regeneración exergética frente a la disipación del entorno*")

if db_disponible:
    try:
        # Consulta inmutable al Lógos de datos
        cursor.execute("""
            SELECT timestamp, (e_in - i_destroyed) as upr_net 
            FROM exergy_history 
            WHERE foco = %s 
            ORDER BY timestamp ASC;
        """, (foco_metabolico,))
        
        rows = cursor.fetchall()
        
        if rows:
            # Transformación de datos para el vector de visualización
            chart_data = pd.DataFrame({
                'Potencia UPR Neto (W-Neg)': [max(0.0, r[1]) for r in rows]
            }, index=[r[0].strftime("%m-%d %H:%M") for r in rows])
            
            # Trazado de la línea evolutiva psicohistórica
            st.line_chart(chart_data)
            
            # Resumen de metamorfosis sistémica
            st.info(f"Registro: Se han consolidado {len(rows)} puntos de control en la serie histórica del Oikos.")
        else:
            st.info("A la espera de registros almacenados en el Lógos para trazar la línea evolutiva de la UPR.")
            
    except Exception as graph_err:
        st.sidebar.error(f"Fricción en el trazado psicohistórico: {graph_err}")

# Pie de página: Estado del Enlace
st.sidebar.markdown("---")
if not db_disponible: 
    st.sidebar.warning("📡 Modo Autónomo Localizado Activo.")
else: 
    st.sidebar.success("📡 Conexión síncrona con el Lógos central activa.")
