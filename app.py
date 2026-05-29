import streamlit as st
import psycopg2
import random
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN (NEON)
# ==========================================
DB_URL = "postgresql://alexcejudo98:ep_dark_sound_p5p4wzrm@ep-dark-sound-a5x836m4.us-east-2.aws.neon.tech/neondb?sslmode=require"

# ==========================================
# CONFIGURACIÓN DE PARÁMETROS BIOFÍSICOS Y JURÍDICOS (𝛽)
# ==========================================
FACTORES_CALIDAD = {
    "electricidad_kwh": 1000.0,
    "diesel_litros": 10500.0,
    "agua_m3": 150.0,
    "horas_hombre": 75.0
}

st.set_page_config(page_title="MPG - Motor de Fragilidad", page_icon="⚡", layout="wide")

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

st.title("⚡ MOTOR DE FRAGILIDAD REGULATORIA")
st.caption("Metric & Power Group // Módulo de Inmunidad Operativa y Compliance de Grano Fino")

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
# ADUANA DE IDENTIDAD JURÍDICA (Ostrom Principio 1)
# ==========================================
st.sidebar.header("🔑 PRINCIPIO 1: Fronteras")
nodo_id = st.sidebar.text_input("Código de Verificación (Nodo_ID):", value="UNIFIMEX-NODO-01")

# ==========================================
# SISTEMA 4: EL RADAR (NLP Extracción DOF / CNBV / SHCP)
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 SISTEMA 4: Radar Regulatorio Exógeno")
st.sidebar.markdown("*Vectorización NLP de modificaciones normativas en tiempo real*")

# Simulación de la oscilación dinámica del entorno legal
volatilidad_dof = st.sidebar.slider("Frecuencia de Reformas DOF (Tasa Mensual %):", min_value=0.0, max_value=100.0, value=40.0, step=5.0)
severidad_cnbv = st.sidebar.slider("Severidad de Fiscalización CNBV (%):", min_value=0.0, max_value=100.0, value=60.0, step=5.0)
riesgo_sancion_externa = st.sidebar.slider("Riesgo Cambiario / Presión GAFI (%):", min_value=0.0, max_value=100.0, value=30.0, step=5.0)

# Factor de Perturbación Exógena Regulatoria (Λ)
factor_perturbacion_legal = 1.0 + ((volatilidad_dof + severidad_cnbv + riesgo_sancion_externa) / 300.0)

# ==========================================
# SISTEMA 1: TRANSDUCCIÓN METABÓLICA Y FRICCIONES
# ==========================================
st.header("📥 SISTEMA 1: Diagnóstico de Fricción Organizativa Interna")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Flujos de Potencia Operativa")
    input_kwh = st.number_input("Consumo Energético de Soporte (kWh):", min_value=0.0, value=150.0, step=1.0)
    input_human = st.number_input("Horas-Hombre Asignadas a Control y Riesgo:", min_value=0.0, value=45.0, step=1.0)
    input_diesel = st.number_input("Insumos Logísticos Auxiliares (Litros):", min_value=0.0, value=0.0, step=1.0)
    input_agua = st.number_input("Recursos de Infraestructura (m³):", min_value=0.0, value=0.0, step=1.0)

with col2:
    st.subheader("Fricciones de Vulnerabilidad Estructural")
    friccion_contratos = st.number_input("Contratos o Expedientes no indexados / rezagados:", min_value=0.0, value=12.0, step=1.0)
    friccion_latencia = st.number_input("Latencia en adopción de circulares (Días de retraso):", min_value=0.0, value=25.0, step=5.0)
    friccion_precio = st.sidebar.slider("Volatilidad del Dinero (Inestabilidad Fiduciaria %):", min_value=0.0, max_value=100.0, value=15.0, step=1.0)

# ==========================================
# SISTEMA 2: FILTRO CIBERNÉTICO Y PROCESAMIENTO
# ==========================================
e_in_real = (
    (input_kwh * FACTORES_CALIDAD["electricidad_kwh"]) +
    (input_diesel * FACTORES_CALIDAD["diesel_litros"]) +
    (input_agua * FACTORES_CALIDAD["agua_m3"]) +
    (input_human * FACTORES_CALIDAD["horas_hombre"])
)

PENALIZACION_CONTRATO = 1200.0  # Watts destruidos por cada cabo suelto legal
PENALIZACION_LATENCIA = 350.0   # Exergía disipada por cada día de ceguera institucional
multiplicador_interno = 1.0 + (friccion_precio / 100.0)

# El output exógeno se destruye: la fragilidad destruye potencia útil endógenamente
i_destroyed = ((friccion_contratos * PENALIZACION_CONTRATO) + (friccion_latencia * PENALIZACION_LATENCIA)) * multiplicador_interno * factor_perturbacion_legal

# ==========================================
# AUDITORÍA DE FRAGILIDAD MONUMENTAL
# ==========================================
st.markdown("---")
st.header("📊 Balances de Coherencia y Fragilidad Sistémica")

excedente_neto = e_in_real - i_destroyed

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)

with metrics_col1:
    st.markdown(f"""
    <div style="background-color: #1a1a1a; padding: 25px; border: 1px solid #2a2a2a; border-radius: 4px; text-align: left;">
        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #888888; font-weight: bold;">Capacidad Informacional Inyectada (E_in)</span>
        <p style="font-size: 38px; font-family: 'Courier New', monospace; font-weight: bold; color: #ffffff; margin: 10px 0 0 0;">{e_in_real:,.2f} <span style="font-size: 18px; color: #666666;">W</span></p>
    </div>
    """, unsafe_allow_html=True)

with metrics_col2:
    st.markdown(f"""
    <div style="background-color: #1a1a1a; padding: 25px; border: 1px solid #2a2a2a; border-radius: 4px; text-align: left;">
        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #888888; font-weight: bold;">Exergética Destruida por Fragilidad (I_destroyed)</span>
        <p style="font-size: 38px; font-family: 'Courier New', monospace; font-weight: bold; color: #ff6b6b; margin: 10px 0 0 0;">{i_destroyed:,.2f} <span style="font-size: 18px; color: #993333;">W</span></p>
    </div>
    """, unsafe_allow_html=True)

with metrics_col3:
    st.markdown(f"""
    <div style="background-color: #1a1a1a; padding: 25px; border: 1px solid #2a2a2a; border-radius: 4px; text-align: left;">
        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #888888; font-weight: bold;">Excedente de Inmunidad Neto</span>
        <p style="font-size: 38px; font-family: 'Courier New', monospace; font-weight: bold; color: #4ade80; margin: 10px 0 0 0;">{max(0.0, excedente_neto):,.2f} <span style="font-size: 18px; color: #228844;">W</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if e_in_real > 0:
    if i_destroyed > e_in_real:
        st.error(f"🛑 COLAPSO POR FRAGILIDAD JURÍDICA: Las fricciones de cumplimiento acumuladas ({i_destroyed:,.2f} W) han superado la capacidad informacional del nodo. Riesgo inminente de intervención o sanción punitiva.")
    else:
        eficiencia_real = ((e_in_real - i_destroyed) / e_in_real) * 100
        
        if eficiencia_real >= 80.0:
            st.success(f"✅ Estructura Antifrágil Consolidada. Índice de Robustez Regulatoria: {eficiencia_real:.2f}%")
        elif eficiencia_real >= 50.0:
            st.warning(f"⚠️ Alerta de Vulnerabilidad Informacional. El Oikos está disipando energía útil ante el entorno normativo. Eficiencia Real: {eficiencia_real:.2f}%")
        else:
            st.error(f"🛑 Fragilidad Aguda Detectada. La latencia institucional ha comprometido la soberanía del nodo: {eficiencia_real:.2f}%")

        # ==========================================
        # SISTEMA 3: ASIGNACIÓN DE ACTIVOS DE CONTENCIÓN
        # ==========================================
        st.markdown("---")
        st.header("⚙️ SISTEMA 3: Arbitraje Táctico de Inmunidad Institucional")
        st.markdown("*Mitigación homeostática del excedente informacional para blindar las fronteras corporativas*")
        
        alloc_control_col1, alloc_control_col2, alloc_control_col3 = st.columns(3)
        
        with alloc_control_col1:
            r_maint = st.slider("🛡️ Recalibración Automatizada NLP (%):", min_value=5, max_value=40, value=20, step=1)
        with alloc_control_col2:
            r_assets = st.slider("📈 Fondo de Reserva Legal Indexado (%):", min_value=5, max_value=40, value=15, step=1)
        with alloc_control_col3:
            r_slack = st.slider("🌪️ Cobertura de Contingencia GAFI / CNBV (%):", min_value=0, max_value=20, value=10, step=1)
        
        porcentaje_resiliencia_total = r_maint + r_assets + r_slack
        porcentaje_salida = 100 - porcentaje_resiliencia_total
        
        if porcentaje_resiliencia_total > 90:
            st.error(f"⚠️ ERROR DE ASIGNACIÓN: El exceso de retención defensiva ({porcentaje_resiliencia_total}%) paraliza la Salida Útil corporativa.")
        elif porcentaje_resiliencia_total < 10:
            st.error(f"⚠️ ERROR DE ASIGNACIÓN: Nivel de resiliencia regulatoria peligrosamente bajo. Expuesto a la tragedia de los comunes.")
        else:
            # ========================================================
            # SANCIONES GRADUADAS DE ELINOR OSTROM PARA EL COMPLIANCE
            # ========================================================
            nivel_sancion = 0
            motivo_sancion = "Nodo en total armonía con las reglas de reciprocidad del tejido institucional."
            
            if eficiencia_real < 70.0 and porcentaje_resiliencia_total < 35:
                nivel_sancion = 1
                motivo_sancion = "Sanción Grado 1: El nodo presenta una fragilidad elevada y fondos de mitigación insuficientes. Se confisca preventivamente el 15% de su Salida Útil para reinyectarse al Mantenimiento Legal Común."
            
            if r_maint == 5 or r_assets == 5:
                nivel_sancion = 2
                motivo_sancion = f"Sanción Grado 2 (VETO JURÍDICO): El {nodo_id} ha desprotegido su matriz legal situando los fondos en el mínimo biológico (5%). Intento de extracción oportunista detectado. Persistencia denegada."

            if nivel_sancion == 1:
                penalizacion_ostrom = 15.0
                r_maint_efectivo = r_maint + penalizacion_ostrom
                porcentaje_salida_efectivo = max(0.0, porcentaje_salida - penalizacion_ostrom)
            elif nivel_sancion == 2:
                r_maint_efectivo = r_maint
                porcentaje_salida_efectivo = 0.0
            else:
                r_maint_efectivo = r_maint
                porcentaje_salida_efectivo = porcentaje_salida

            potencia_maint = excedente_neto * (r_maint_efectivo / 100.0)
            potencia_assets = excedente_neto * (r_assets / 100.0)
            potencia_slack = excedente_neto * (r_slack / 100.0)
            potencia_salida_util = excedente_neto * (porcentaje_salida_efectivo / 100.0)
            
            st.subheader("📊 Distribución de Potencia Activa (Modernismo Noire)")
            
            def obtener_estilo_noire(porcentaje, min_optimo, max_optimo, sancionados=False):
                if sancionados:
                    return "background-color: #261212; color: #ff6b6b; border: 1px dashed #ef4444;"
                if porcentaje < min_optimo:
                    return "background-color: #261212; color: #ff6b6b; border: 1px solid #7f1d1d;"
                elif porcentaje <= max_optimo:
                    return "background-color: #1a1a1a; color: #4ade80; border: 1px solid #14532d;"
                else:
                    return "background-color: #211d14; color: #facc15; border: 1px solid #713f12;"

            estilo_maint = obtener_estilo_noire(r_maint_efectivo, 15, 30, sancionados=(nivel_sancion == 1))
            estilo_assets = obtener_estilo_noire(r_assets, 15, 30)
            estilo_slack = obtener_estilo_noire(r_slack, 5, 15)
            
            if nivel_sancion == 2:
                estilo_salida = "background-color: #330d0d; color: #ff4545; border: 2px solid #ff0000; box-shadow: 0 0 15px #500;"
            elif porcentaje_salida_efectivo > 75:
                st.error("⚠️ CRÍTICA: Distribución desproporcionada. Salida útil pone en riesgo la estabilidad interna.")
                estilo_salida = "background-color: #261212; color: #ff6b6b; border: 1px solid #7f1d1d;"
            elif porcentaje_salida_efectivo >= 40:
                estilo_salida = "background-color: #1a1a1a; color: #4ade80; border: 1px solid #14532d;"
            else:
                estilo_salida = "background-color: #211d14; color: #facc15; border: 1px solid #713f12;"

            res_col1, res_col2, res_col3, out_col = st.columns(4)
            
            with res_col1:
                st.markdown(f"""
                <div style="{estilo_maint} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #888888;'>⚙️ NLP Compliance</h4>
                    <p style='font-size: 26px; font-family: \"Courier New\", monospace; font-weight: bold; margin: 15px 0;'>{potencia_maint:,.2f} W</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.7;'>({r_maint_efectivo}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with res_col2:
                st.markdown(f"""
                <div style="{estilo_assets} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #888888;'>📦 Fondo Indexado</h4>
                    <p style='font-size: 26px; font-family: \"Courier New\", monospace; font-weight: bold; margin: 15px 0;'>{potencia_assets:,.2f} W</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.7;'>({r_assets}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with res_col3:
                st.markdown(f"""
                <div style="{estilo_slack} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #888888;'>🛡️ Cobertura Slack</h4>
                    <p style='font-size: 26px; font-family: \"Courier New\", monospace; font-weight: bold; margin: 15px 0;'>{potencia_slack:,.2f} W</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.7;'>({r_slack}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with out_col:
                st.markdown(f"""
                <div style="{estilo_salida} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #ffffff;'>🚀 Viabilidad Libre</h4>
                    <p style='font-size: 26px; font-family: \"Courier New\", monospace; font-weight: bold; margin: 15px 0;'>{potencia_salida_util:,.2f} W</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.7;'>({porcentaje_salida_efectivo}%)</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if nivel_sancion == 0:
                st.info(f"⚖️ **Auditoría Ostrom ({nodo_id}):** {motivo_sancion}")
            elif nivel_sancion == 1:
                st.warning(f"⚖️ **Auditoría Ostrom ({nodo_id}):** {motivo_sancion}")
            elif nivel_sancion == 2:
                st.error(f"⚖️ **🛡️ VETO DE CUMPLIMIENTO ACTIVADO ({nodo_id}):** {motivo_sancion}")

        # ========================================================
        # ADUANA COERCITIVA DE PERSISTENCIA
        # ========================================================
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Persistir Balance del VSM en el Lógos Inmutable"):
            if not db_disponible:
                st.warning("⚠️ Servidor externo latente. Registro retenido en la memoria local localized del Oikos.")
            elif nivel_sancion == 2:
                st.error(f"🛑 ESCRITURA DENEGADA: El {nodo_id} se encuentra bloqueado por desacato a las reglas de resiliencia mutua.")
            else:
                try:
                    query = "INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);"
                    cursor.execute(query, (e_in_real, i_destroyed, eficiencia_real))
                    conn.commit()
                    st.success(f"Matriz de inmunidad enraizada para el {nodo_id} de forma inmutable.")
                except Exception as db_err:
                    st.error(f"Fricción al escribir en la DB: {db_err}")
else:
    st.info("A la espera de flujos informacionales para iniciar el cálculo homeostático de fragilidad.")

st.sidebar.markdown("---")
if not db_disponible:
    st.sidebar.warning("📡 Red: Servidor Neon fuera de alcance. Modo Autónomo Localizado Activo.")
else:
    st.sidebar.success("📡 Red: Sincronización con el Lógos central activa.")
