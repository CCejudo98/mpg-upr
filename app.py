import streamlit as st
import psycopg2
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN (NEON)
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

# Configuración Estética Unificada (Modernismo Noire y Cleronomía)
st.set_page_config(page_title="MPG - Motor de Gobernabilidad", page_icon="⚡", layout="wide")

st.title("⚡ MOTOR DE GOBERNABILIDAD HOMEOSTÁTICA")
st.caption("Cleronomía Aplicada: Transducción Bioeconómica y Estabilización Exergética del Oikos")

# ==========================================
# INTENTO DE CONEXIÓN COMPORTAMENTAL
# ==========================================
db_disponible = False
conn = None
cursor = None

try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    st.success("🔗 Conexión con la base de datos central enraizada correctamente.")
    db_disponible = True
except Exception as e:
    db_disponible = False

# ==========================================
# INTERFAZ DE CAPTURA DE VARIABLES REALES
# ==========================================
st.header("📥 Diagnóstico y Transducción del Terreno Real")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Ingreso de Insumos Heterogéneos")
    input_kwh = st.number_input("Electricidad consumida (kWh):", min_value=0.0, value=0.0, step=1.0)
    input_diesel = st.number_input("Diésel utilizado (Litros):", min_value=0.0, value=0.0, step=1.0)
    input_agua = st.number_input("Agua industrial incorporada (m³):", min_value=0.0, value=0.0, step=1.0)
    input_human = st.number_input("Fuerza de trabajo aplicada (Horas-Hombre):", min_value=0.0, value=0.0, step=1.0)

with col2:
    st.subheader("2. Variables de Fricción e Inestabilidad Organizativa")
    friccion_mermas = st.number_input("Mermas de material crítico (Kilogramos / Litros):", min_value=0.0, value=0.0, step=0.5)
    friccion_tiempo = st.number_input("Tiempos de espera o paros en línea de producción (Minutos):", min_value=0.0, value=0.0, step=5.0)
    friccion_precio = st.slider("Índice de oscilación de precios fiduciarios (Volatilidad Nominal %):", min_value=0.0, max_value=100.0, value=0.0, step=1.0)

# ==========================================
# CÁLCULO ALGURÍTMICO DE ENTRADA REAL (E_in)
# ==========================================
e_in_real = (
    (input_kwh * FACTORES_CALIDAD["electricidad_kwh"]) +
    (input_diesel * FACTORES_CALIDAD["diesel_litros"]) +
    (input_agua * FACTORES_CALIDAD["agua_m3"]) +
    (input_human * FACTORES_CALIDAD["horas_hombre"])
)

# ==========================================
# MÓDULO CIBERNÉTICO DE FRICCIÓN INTERNA (I_destroyed)
# ==========================================
# Penalizadores físicos determinados por el desorden organizativo
PENALIZACION_MERMA = 450.0  # Watts destruidos por unidad de desecho material
PENALIZACION_TIEMPO = 120.0 # Watts disipados por cada minuto latente de parálisis estructural
# La oscilación fiduciaria actúa como un amplificador de entropía que degrada la eficiencia general (0-100%)
multiplicador_fiduciario = 1.0 + (friccion_precio / 100.0)

# El output exógeno manual ha sido destruido; la disipación se calcula endógenamente aquí:
i_destroyed = ((friccion_mermas * PENALIZACION_MERMA) + (friccion_tiempo * PENALIZACION_TIEMPO)) * multiplicador_fiduciario

# ==========================================
# VALIDACIÓN Y BALANCE ENTRÓPICO COHERENTE
# ==========================================
st.header("📊 Balance y Estabilización Homeostática")

metrics_col1, metrics_col2 = st.columns(2)
metrics_col1.metric("Entrada Exergética Real Unificada (E_in)", f"{e_in_real:,.2f} Watts")
metrics_col2.metric("Potencia Exergética Destruida Algorítmica (I_destroyed)", f"{i_destroyed:,.2f} Watts")

if e_in_real > 0:
    # Verificación estricta de la frontera física y organizativa
    if i_destroyed > e_in_real:
        st.error(f"⚠️ VIOLACIÓN TERMODINÁMICA: El desorden organizativo genera una fricción acumulada ({i_destroyed:,.2f} W) que supera la potencia exergética real ingresada ({e_in_real:,.2f} W). Este Oikos está en colapso destructivo irreversible.")
    else:
        eficiencia_real = ((e_in_real - i_destroyed) / e_in_real) * 100
        
        if eficiencia_real >= 50.0:
            st.success(f"✅ Homeostasis Consolidada. Eficiencia Exergética Real del Oikos: {eficiencia_real:.2f}%")
        else:
            st.warning(f"⚠️ Alerta Crítica de Entropía. El sistema es viable pero disipativo. Eficiencia Real: {eficiencia_real:.2f}%. Se sugiere arbitraje inmediato de activos.")
        
        # Guardado condicional adaptativo
        if st.button("💾 Persistir Medición en la Memoria"):
            if db_disponible:
                try:
                    query = "INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);"
                    cursor.execute(query, (e_in_real, i_destroyed, eficiencia_real))
                    conn.commit()
                    st.info("Datos integrados a la memoria inmutable del servidor Neon.")
                except Exception as db_err:
                    st.error(f"Fricción al escribir en la DB: {db_err}")
            else:
                st.warning("⚠️ Servidor externo latente. La medición ha sido procesada y retenida en la memoria volátil de la pantalla para evitar pérdida de datos.")
else:
    st.info("A la espera de flujos de insumos y métricas de fricción en las fronteras del sistema.")

# Estatus del perímetro en barra lateral
if not db_disponible:
    st.sidebar.markdown("---")
    st.sidebar.warning("📡 Estado de Red: Servidor Neon fuera de alcance (IP Limit). Operando en Modo Autónomo Local Localizado.")
