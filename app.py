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

st.set_page_config(page_title="MPG - Motor de Gobernabilidad", page_icon="⚡", layout="wide")

st.title("⚡ MOTOR DE GOBERNABILIDAD HOMEOSTÁTICA")
st.caption("Cleronomía Aplicada: Arquitectura de Sistema Viable (VSM) para la Autonomía del Oikos")

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
# SISTEMA 4: EL RADAR (Prospección del Entorno 2020-2026)
# ==========================================
st.sidebar.header("📡 SISTEMA 4: Radar de Entorno Macroeconómico")
st.sidebar.markdown("*Monitoreo de perturbaciones exógenas en el bloque de Norteamérica (2020-2026)*")

alerta_tmec = st.sidebar.slider("Riesgo de Choque Arancelario T-MEC (%):", min_value=0.0, max_value=100.0, value=35.0, step=5.0)
penetracion_china = st.sidebar.slider("Índice de Canibalización por Insumo Asiático (%):", min_value=0.0, max_value=100.0, value=50.0, step=5.0)
estres_red_cfe = st.sidebar.slider("Estrés de Capacidad Energética (Cortes de Red/CFE %):", min_value=0.0, max_value=100.0, value=20.0, step=5.0)

factor_perturbacion_vsm = 1.0 + ((alerta_tmec + penetracion_china + estres_red_cfe) / 300.0)

# ==========================================
# SISTEMA 1: CAPTURA DEL NODO ACTIVO
# ==========================================
st.header("📥 SISTEMA 1: Diagnóstico y Transducción de Flujos Reales")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Entradas Metabólicas Heterogéneas")
    input_kwh = st.number_input("Electricidad consumida (kWh):", min_value=0.0, value=120.0, step=1.0)
    input_diesel = st.number_input("Diésel utilizado (Litros):", min_value=0.0, value=30.0, step=1.0)
    input_agua = st.number_input("Agua industrial incorporada (m³):", min_value=0.0, value=5.0, step=1.0)
    input_human = st.number_input("Fuerza de trabajo aplicada (Horas-Hombre):", min_value=0.0, value=24.0, step=1.0)

with col2:
    st.subheader("Fricciones Organizativas Locales")
    friccion_mermas = st.number_input("Mermas de material crítico (Kilogramos / Litros):", min_value=0.0, value=15.0, step=0.5)
    friccion_tiempo = st.number_input("Tiempos de espera o paros en línea de producción (Minutos):", min_value=0.0, value=20.0, step=5.0)
    friccion_precio = st.slider("Índice de oscilación de precios fiduciarios (Volatilidad Nominal %):", min_value=0.0, max_value=100.0, value=10.0, step=1.0)

# ==========================================
# SISTEMA 2: FILTRO ANTI-OSCILACIÓN Y PROCESAMIENTO
# ==========================================
e_in_real = (
    (input_kwh * FACTORES_CALIDAD["electricidad_kwh"]) +
    (input_diesel * FACTORES_CALIDAD["diesel_litros"]) +
    (input_agua * FACTORES_CALIDAD["agua_m3"]) +
    (input_human * FACTORES_CALIDAD["horas_hombre"])
)

PENALIZACION_MERMA = 450.0  
PENALIZACION_TIEMPO = 120.0 
multiplicador_interno = 1.0 + (friccion_precio / 100.0)

i_destroyed = ((friccion_mermas * PENALIZACION_MERMA) + (friccion_tiempo * PENALIZACION_TIEMPO)) * multiplicador_interno * factor_perturbacion_vsm

# ==========================================
# VALIDACIÓN TERMODINÁMICA Y HOMEOSTASIS
# ==========================================
st.header("📊 Balances de Coherencia Cibernética")

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
metrics_col1.metric("Ingreso Exergético Real (E_in)", f"{e_in_real:,.2f} Watts")
metrics_col2.metric("Potencia Destruida (I_destroyed)", f"{i_destroyed:,.2f} Watts")

excedente_neto = e_in_real - i_destroyed
metrics_col3.metric("Excedente Exergético Neto disponible", f"{max(0.0, excedente_neto):,.2f} Watts")

if e_in_real > 0:
    if i_destroyed > e_in_real:
        st.error(f"🛑 VIOLACIÓN TERMODINÁMICA SISTÉMICA: La fricción interna y las perturbaciones del entorno ({i_destroyed:,.2f} W) han sobrepasado la potencia de entrada ({e_in_real:,.2f} W). El Oikos está en colapso por entropía incontrolable.")
    else:
        eficiencia_real = ((e_in_real - i_destroyed) / e_in_real) * 100
        
        if eficiencia_real >= 85.0:
            st.success(f"✅ Homeostasis Consolidada. Eficiencia Exergética Real: {eficiencia_real:.2f}%")
        elif eficiencia_real >= 60.0:
            st.warning(f"⚠️ Alerta Crítica de Entropía. Sistema disipativo ante el entorno. Eficiencia Real: {eficiencia_real:.2f}%")
        else:
            st.error(f"🛑 Degradación Estructural Aguda. Eficiencia crítica: {eficiencia_real:.2f}%. Pérdida inminente de viabilidad.")

        # ==========================================
        # SISTEMA 3: HOMEOSTASIS INTERNA (Disección Táctica)
        # ==========================================
        st.header("⚙️ SISTEMA 3: Política de Asignación Exergética Táctica")
        st.markdown("*Distribución analítica del excedente real neto en vectores de inmunidad entrópica*")
        
        alloc_control_col1, alloc_control_col2, alloc_control_col3 = st.columns(3)
        
        with alloc_control_col1:
            r_maint = st.slider("🛡️ Mantenimiento Físico (%):", min_value=5, max_value=40, value=15, step=1)
        with alloc_control_col2:
            r_assets = st.slider("📈 Reserva de Activos Reales (%):", min_value=5, max_value=40, value=15, step=1)
        with alloc_control_col3:
            r_slack = st.slider("🌪️ Holgura y Contingencia (%):", min_value=0, max_value=20, value=10, step=1)
        
        porcentaje_resiliencia_total = r_maint + r_assets + r_slack
        porcentaje_salida = 100 - porcentaje_resiliencia_total
        
        if porcentaje_resiliencia_total > 90:
            st.error(f"⚠️ ERROR DE ASIGNACIÓN: La resiliencia total configurada ({porcentaje_resiliencia_total}%) asfixia la potencia de salida. El Oikos se vuelve un sistema cerrado estéril.")
        elif porcentaje_resiliencia_total < 10:
            st.error(f"⚠️ ERROR DE ASIGNACIÓN: La resiliencia total ({porcentaje_resiliencia_total}%) es peligrosamente baja. El capital fijo se degradará ante la entropía.")
        else:
            potencia_maint = excedente_neto * (r_maint / 100.0)
            potencia_assets = excedente_neto * (r_assets / 100.0)
            potencia_slack = excedente_neto * (r_slack / 100.0)
            potencia_salida_util = excedente_neto * (porcentaje_salida / 100.0)
            
            st.subheader("📊 Distribución Final de Potencia Activa (Semaforización de Grano Fino)")
            
            def obtener_estilo_tarjeta(porcentaje, min_optimo, max_optimo):
                if porcentaje < min_optimo:
                    return "background-color: #fde8e8; color: #9b1c1c; border: 1px solid #f8b4b4;"
                elif porcentaje <= max_optimo:
                    return "background-color: #eafaf1; color: #145a32; border: 1px solid #abebc6;"
                else:
                    return "background-color: #fef9e7; color: #7d6608; border: 1px solid #f9e79f;"

            estilo_maint = obtener_estilo_tarjeta(r_maint, 15, 30)
            estilo_assets = obtener_estilo_tarjeta(r_assets, 15, 30)
            estilo_slack = obtener_estilo_tarjeta(r_slack, 5, 15)
            
            if porcentaje_salida > 75:
                estilo_salida = "background-color: #fde8e8; color: #9b1c1c; border: 1px solid #f8b4b4;"
            elif porcentaje_salida >= 40:
                estilo_salida = "background-color: #eafaf1; color: #145a32; border: 1px solid #abebc6;"
            else:
                estilo_salida = "background-color: #fef9e7; color: #7d6608; border: 1px solid #f9e79f;"

            res_col1, res_col2, res_col3, out_col = st.columns(4)
            
            with res_col1:
                st.markdown(f"""
                <div style="{estilo_maint} padding: 20px; border-radius: 10px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 14px;'>⚙️ Mantenimiento</h4>
                    <p style='font-size: 22px; font-weight: bold; margin: 10px 0;'>{potencia_maint:,.2f} W</p>
                    <span style='font-size: 14px; font-family: monospace;'>({r_maint}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with res_col2:
                st.markdown(f"""
                <div style="{estilo_assets} padding: 20px; border-radius: 10px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 14px;'>📦 Fondo Activos</h4>
                    <p style='font-size: 22px; font-weight: bold; margin: 10px 0;'>{potencia_assets:,.2f} W</p>
                    <span style='font-size: 14px; font-family: monospace;'>({r_assets}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with res_col3:
                st.markdown(f"""
                <div style="{estilo_slack} padding: 20px; border-radius: 10px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 14px;'>🛡️ Holgura / Slack</h4>
                    <p style='font-size: 22px; font-weight: bold; margin: 10px 0;'>{potencia_slack:,.2f} W</p>
                    <span style='font-size: 14px; font-family: monospace;'>({r_slack}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with out_col:
                st.markdown(f"""
                <div style="{estilo_salida} padding: 20px; border-radius: 10px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 14px;'>🚀 Salida Útil</h4>
                    <p style='font-size: 22px; font-weight: bold; margin: 10px 0;'>{potencia_salida_util:,.2f} W</p>
                    <span style='font-size: 14px; font-family: monospace;'>({porcentaje_salida}%)</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"<br><p style='font-size: 16px; text-align: center;'><b>Análisis de Grano Fino:</b> La matriz ha distribuido el excedente. El color refleja el nivel de compromiso termodinámico con la inmunidad del capital fijo.</p>", unsafe_allow_html=True)

        if st.button("💾 Persistir Balance Completo del VSM en el Lógos"):
            if db_disponible:
                try:
                    query = "INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);"
                    cursor.execute(query, (e_in_real, i_destroyed, eficiencia_real))
                    conn.commit()
                    st.info("Datos del VSM integrados a la memoria inmutable del servidor Neon.")
                except Exception as db_err:
                    st.error(f"Fricción al escribir en la DB: {db_err}")
            else:
                st.warning("⚠️ Servidor externo latente. El balance táctico del VSM ha sido calculado y retenido en la memoria local de la pantalla.")
else:
    st.info("A la espera de flujos de insumos y métricas de fricción para activar los sistemas de control.")

st.sidebar.markdown("---")
if not db_disponible:
    st.sidebar.warning("📡 Estado de Red: Servidor Neon fuera de alcance (IP Limit). Operando en Modo Autónomo Local Localizado.")
else:
    st.sidebar.success("📡 Red: Sincronización con el Lógos central activa.")
