import streamlit as st
import psycopg2
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN ABSOLUTO (NEON)
# ==========================================
DB_URL = "postgresql://alexcejudo98:ep_dark_sound_p5p4wzrm@ep-dark-sound-a5x836m4.us-east-2.aws.neon.tech/neondb?sslmode=require"

# ==========================================
# CONFIGURACIÓN DE PARÁMETROS BIOFÍSICOS (𝛽)
# ==========================================
FACTORES_CALIDAD = {
    "electricidad_kwh": 1000.0,
    "diesel_litros": 10500.0,
    "agua_m3": 150.0,
    "horas_hombre": 75.0
}

# Configuración Estética Unificada (Bajo el alias 'st')
st.set_page_config(page_title="MPG - Panel de Control UPR", page_icon="⚡", layout="wide")

st.title("⚡ METRIC & POWER GROUP // UNIDAD DE PROCESAMIENTO REAL")
st.caption("Módulo de Transducción Bioeconómica y Auditoría Exergética de Grano Fino")

# ==========================================
# PRUEBA DE CONEXIÓN CON EL LÓGOS
# ==========================================
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    st.success("🔗 Conexión con el Lógos consolidada exitosamente.")
except Exception as e:
    st.error("⚠️ Fricción de conexión: No se pudo conectar con el Lógos. El cortafuegos o las credenciales impiden el acceso.")
    st.stop()

# ==========================================
# INTERFAZ DE CAPTURA EN UNIDADES NATIVAS
# ==========================================
st.header("📥 Transducción de Insumos Heterogéneos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Entradas al Oikos (Unidades Nativas)")
    input_kwh = st.number_input("Electricidad consumida (kWh):", min_value=0.0, value=0.0, step=1.0)
    input_diesel = st.number_input("Diésel utilizado (Litros):", min_value=0.0, value=0.0, step=1.0)
    input_agua = st.number_input("Agua industrial incorporada (m³):", min_value=0.0, value=0.0, step=1.0)
    input_human = st.number_input("Fuerza de trabajo aplicada (Horas-Hombre):", min_value=0.0, value=0.0, step=1.0)

with col2:
    st.subheader("Disipación del Sistema")
    e_out = st.number_input("Desperdicio / Disipación térmica observada (Watts):", min_value=0.0, value=0.0, step=10.0)

# ==========================================
# MÓDULO DE TRANSDUCCIÓN MATEMÁTICA (𝛽 · E)
# ==========================================
e_in_real = (
    (input_kwh * FACTORES_CALIDAD["electricidad_kwh"]) +
    (input_diesel * FACTORES_CALIDAD["diesel_litros"]) +
    (input_agua * FACTORES_CALIDAD["agua_m3"]) +
    (input_human * FACTORES_CALIDAD["horas_hombre"])
)

# ==========================================
# VALIDACIÓN Y BALANCE ENTRÓPICO
# ==========================================
st.header("📊 Balance Exergético de Grano Fino")

metrics_col1, metrics_col2 = st.columns(2)
metrics_col1.metric("Entrada Exergética Real Unificada (E_in)", f"{e_in_real:,.2f} Watts")
metrics_col2.metric("Disipación Entrópica (E_out)", f"{e_out:,.2f} Watts")

if e_in_real > 0:
    if e_out > e_in_real:
        st.error(f"⚠️ VIOLACIÓN TERMODINÁMICA: La disipación ({e_out} W) supera al ingreso exergético real ({e_in_real:.2f} W). Operación imposible según la Segunda Ley.")
    else:
        eficiencia_real = ((e_in_real - e_out) / e_in_real) * 100
        st.success(f"✅ Estado del Oikos Coherente. Eficiencia Exergética Real: {eficiencia_real:.2f}%")
        
        if st.button("💾 Persistir Medición en el Lógos"):
            try:
                query = "INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);"
                cursor.execute(query, (e_in_real, e_out, eficiencia_real))
                conn.commit()
                st.info("Datos integrados a la memoria inmutable del servidor.")
            except Exception as db_err:
                st.error(f"Fricción al escribir en la DB: {db_err}")
else:
    st.info("A la espera de flujos de insumos en las fronteras del sistema.")
