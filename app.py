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

# Configuración de Página de Grano Fino
st.set_page_config(page_title="MPG - Motor de Gobernabilidad", page_icon="⚡", layout="wide")

# ==========================================
# CÁPSULA ESTÉTICA: MODERNISMO NOIRE (CSS)
# ==========================================
st.markdown("""
<style>
    /* Inyección de la atmósfera Noire en el contenedor global */
    .stApp {
        background-color: #0d0d0d;
        color: #d1d1d1;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Configuración funcionalista para barras laterales */
    [data-testid="stSidebar"] {
        background-color: #141414;
        border-right: 1px solid #262626;
    }
    
    /* Títulos y tipografía de rigurosa sobriedad */
    h1, h2, h3, h4, h5, h6, label, .stMarkdown {
        color: #e5e5e5 !important;
        font-weight: 400 !important;
    }
    
    /* Customización de entradas numéricas y deslizadores al acero industrial */
    .stNumberInput input, .stTextInput input {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
    }
    
    /* Líneas horizontales de separación de baja entropía */
    hr {
        border-top: 1px solid #262626 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ MOTOR DE GOBERNABILIDAD HOMEOSTÁTICA")
st.caption("Cleronomía Aplicada: Arquitectura Noire de Sistema Viable (VSM) y Gobernanza Ostromiana")

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
nodo_id = st.sidebar.text_input("Código de Verificación (Nodo_ID):", value="UNAM-FE-OIKOS-01")

# ==========================================
# SISTEMA 4: EL RADAR (Prospección del Entorno 2020-2026)
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 SISTEMA 4: Radar de Entorno")
st.sidebar.markdown("*Perturbaciones exógenas detectadas (2020-2026)*")

alerta_tmec = st.sidebar.slider("Choque Arancelario T-MEC (%):", min_value=0.0, max_value=100.0, value=35.0, step=5.0)
penetracion_china = st.sidebar.slider("Canibalización Insumo Asiático (%):", min_value=0.0, max_value=100.0, value=50.0, step=5.0)
estres_red_cfe = st.sidebar.slider("Estrés de Capacidad Red CFE (%):", min_value=0.0, max_value=100.0, value=20.0, step=5.0)

factor_perturbacion_vsm = 1.0 + ((alerta_tmec + penetracion_china + estres_red_cfe) / 300.0)

# ==========================================
# SISTEMA 1: CAPTURA DEL NODO ACTIVO
# ==========================================
st.header("📥 SISTEMA 1: Transducción del Metabolismo Real")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Entradas Metabólicas Heterogéneas")
    input_kwh = st.number_input("Electricidad consumida (kWh):", min_value=0.0, value=120.0, step=1.0)
    input_diesel = st.number_input("Diésel utilizado (Litros):", min_value=0.0, value=30.0, step=1.0)
    input_agua = st.number_input("Agua industrial incorporada (m³):", min_value=0.0, value=5.0, step=1.0)
    input_human = st.number_input("Fuerza de trabajo aplicada (Horas-Hombre):", min_value=0.0, value=24.0, step=1.0)

with col2:
    st.subheader("Fricciones Organizativas Locales")
    friccion_mermas = st.number_input("Mermas de material crítico (Kg / L):", min_value=0.0, value=15.0, step=0.5)
    friccion_tiempo = st.number_input("Tiempos de espera / paros en línea (Minutos):", min_value=0.0, value=20.0, step=5.0)
    friccion_precio = st.sidebar.slider("Volatilidad Nominal Fiduciaria (%):", min_value=0.0, max_value=100.0, value=10.0, step=1.0)

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
st.markdown("---")
st.header("📊 Balances de Coherencia Cibernética")

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
metrics_col1.metric("Ingreso Exergético Real (E_in)", f"{e_in_real:,.2f} Watts")
metrics_col2.metric("Potencia Destruida (I_destroyed)", f"{i_destroyed:,.2f} Watts")

excedente_neto = e_in_real - i_destroyed
metrics_col3.metric("Excedente Neto Disponible", f"{max(0.0, excedente_neto):,.2f} Watts")

if e_in_real > 0:
    if i_destroyed > e_in_real:
        st.error("🛑 VIOLACIÓN TERMODINÁMICA SISTÉMICA: La fricción ha devorado la entrada exergética real.")
    else:
        eficiencia_real = ((e_in_real - i_destroyed) / e_in_real) * 100
        
        if eficiencia_real >= 85.0:
            st.success(f"✅ Homeostasis Consolidada. Eficiencia Exergética Real: {eficiencia_real:.2f}%")
        elif eficiencia_real >= 60.0:
            st.warning(f"⚠️ Alerta Crítica de Entropía. Sistema altamente disipativo. Eficiencia Real: {eficiencia_real:.2f}%")
        else:
            st.error(f"🛑 Degradación Estructural Aguda. Eficiencia crítica: {eficiencia_real:.2f}%")

        # ==========================================
        # SISTEMA 3: HOMEOSTASIS INTERNA (Disección Táctica)
        # ==========================================
        st.markdown("---")
        st.header("⚙️ SISTEMA 3: Política de Asignación Exergética Táctica")
        st.markdown("*Distribución del excedente real neto en vectores de inmunidad entrópica*")
        
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
            st.error(f"⚠️ ERROR DE ASIGNACIÓN: La resiliencia total configurada ({porcentaje_resiliencia_total}%) asfixia la potencia de salida.")
        elif porcentaje_resiliencia_total < 10:
            st.error(f"⚠️ ERROR DE ASIGNACIÓN: La resiliencia total ({porcentaje_resiliencia_total}%) es peligrosamente baja.")
        else:
            # ========================================================
            # EVALUACIÓN DE REGLAS DE ACCESO COMÚN (Elinor Ostrom)
            # ========================================================
            nivel_sancion = 0
            motivo_sancion = "Cumplimiento total de las reglas de apropiación común."
            
            if eficiencia_real < 75.0 and porcentaje_resiliencia_total < 35:
                nivel_sancion = 1
                motivo_sancion = "Sanción Grado 1: Degradación crónica y resiliencia insuficiente (<35%). Se confisca preventivamente el 15% de la Salida Útil para el Mantenimiento del fondo común."
            
            if r_maint == 5 or r_assets == 5:
                nivel_sancion = 2
                motivo_sancion = f"Sanción Grado 2 (VETO): El {nodo_id} intentó una extracción depredadora situando la infraestructura en el mínimo (5%). Escritura bloqueada."

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
            
            # DISEÑO DE TARJETAS AL ESTILO MODERNISMO NOIRE Y BRUTALISMO FUNCIONALISTA
            def obtener_estilo_noire(porcentaje, min_optimo, max_optimo, sancionados=False):
                if sancionados:
                    return "background-color: #1a1010; color: #f87171; border: 1px dashed #ef4444;" # Alerta Roja Noire
                if porcentaje < min_optimo:
                    return "background-color: #1a1010; color: #f87171; border: 1px solid #7f1d1d;" # Rojo Fricción
                elif porcentaje <= max_optimo:
                    return "background-color: #0f1612; color: #4ade80; border: 1px solid #14532d;" # Verde Exergético
                else:
                    return "background-color: #1c1912; color: #facc15; border: 1px solid #713f12;" # Ámbar Exeso

            estilo_maint = obtener_estilo_noire(r_maint_efectivo, 15, 30, sancionados=(nivel_sancion == 1))
            estilo_assets = obtener_estilo_noire(r_assets, 15, 30)
            estilo_slack = obtener_estilo_noire(r_slack, 5, 15)
            
            if nivel_sancion == 2:
                estilo_salida = "background-color: #2d0000; color: #ff6b6b; border: 2px solid #ff0000; box-shadow: 0 0 10px #7a0000;"
            elif porcentaje_salida_efectivo > 75:
                estilo_salida = "background-color: #1a1010; color: #f87171; border: 1px solid #7f1d1d;"
            elif porcentaje_salida_efectivo >= 40:
                estilo_salida = "background-color: #0f1612; color: #4ade80; border: 1px solid #14532d;"
            else:
                estilo_salida = "background-color: #1c1912; color: #facc15; border: 1px solid #713f12;"

            res_col1, res_col2, res_col3, out_col = st.columns(4)
            
            with res_col1:
                st.markdown(f"""
                <div style="{estilo_maint} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #8c8c8c;'>⚙️ Mantenimiento</h4>
                    <p style='font-size: 24px; font-weight: bold; margin: 15px 0; font-family: monospace;'>{potencia_maint:,.2f} W</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.8;'>({r_maint_efectivo}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with res_col2:
                st.markdown(f"""
                <div style="{estilo_assets} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #8c8c8c;'>📦 Fondo Activos</h4>
                    <p style='font-size: 24px; font-weight: bold; margin: 15px 0; font-family: monospace;'>{potencia_assets:,.2f} W</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.8;'>({r_assets}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with res_col3:
                st.markdown(f"""
                <div style="{estilo_slack} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #8c8c8c;'>🛡️ Holgura / Slack</h4>
                    <p style='font-size: 24px; font-weight: bold; margin: 15px 0; font-family: monospace;'>{potencia_slack:,.2f} W</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.8;'>({r_slack}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with out_col:
                st.markdown(f"""
                <div style="{estilo_salida} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #e5e5e5;'>🚀 Salida Útil</h4>
                    <p style='font-size: 24px; font-weight: bold; margin: 15px 0; font-family: monospace;'>{potencia_salida_util:,.2f} W</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.8;'>({porcentaje_salida_efectivo}%)</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if nivel_sancion == 0:
                st.info(f"⚖️ **Auditoría Ostrom ({nodo_id}):** {motivo_sancion}")
            elif nivel_sancion == 1:
                st.warning(f"⚖️ **Auditoría Ostrom ({nodo_id}):** {motivo_sancion}")
            elif nivel_sancion == 2:
                st.error(f"⚖️ **🛡️ VETO INSTITUCIONAL ACTIVADO ({nodo_id}):** {motivo_sancion}")

        # ========================================================
        # ADUANA COERCITIVA DE PERSISTENCIA
        # ========================================================
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Persistir Balance Completo del VSM en el Lógos"):
            if not db_disponible:
                st.warning("⚠️ Servidor externo latente. Operando en memoria local localizado.")
            elif nivel_sancion == 2:
                st.error(f"🛑 ESCRITURA DENEGADA: El {nodo_id} viola las reglas de preservación del común.")
            else:
                try:
                    query = "INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);"
                    cursor.execute(query, (e_in_real, i_destroyed, eficiencia_real))
                    conn.commit()
                    st.success(f"Datos del VSM enraizados inmutablemente para el {nodo_id}.")
                except Exception as db_err:
                    st.error(f"Fricción al escribir en la DB: {db_err}")
else:
    st.info("A la espera de flujos metabólicos para iniciar el procesamiento homeostático.")

st.sidebar.markdown("---")
if not db_disponible:
    st.sidebar.warning("📡 Red: Servidor Neon fuera de alcance. Modo Autónomo Localizado.")
else:
    st.sidebar.success("📡 Red: Sincronización con el Lógos activa.")
