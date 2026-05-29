import streamlit as st
import psycopg2
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN INMUTABLE (NEON)
# ==========================================
DB_URL = "postgresql://alexcejudo98:ep_dark_sound_p5p4wzrm@ep-dark-sound-a5x836m4.us-east-2.aws.neon.tech/neondb?sslmode=require"

# ==========================================
# CONFIGURACIÓN DE PARÁMETROS BIOFÍSICOS E INFORMACIONALES (𝛽)
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

st.set_page_config(page_title="MPG - Motor Homeostático", page_icon="⚡", layout="wide")

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

st.title("⚡ MOTOR DE GOBERNABILIDAD HOMEOSTÁTICA")
st.caption("Cleronomía Aplicada: Gestión Multidimensional de Sistemas Viables, Bienes Comunes e Inmunidad ante el Riesgo")

# ==========================================
# CONEXIÓN Y CREACIÓN DE ESTRUCTURAS INMUTABLES
# ==========================================
db_disponible = False
conn = None
cursor = None

try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metric_history (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            e_in DOUBLE PRECISION,
            e_out DOUBLE PRECISION,
            efficiency DOUBLE PRECISION
        );
    """)
    conn.commit()
    st.success("🔗 Sincronización con la base de datos central enraizada correctamente.")
    db_disponible = True
except Exception as e:
    st.sidebar.error(f"Fricción de enlace con DB: {e}")
    db_disponible = False

# ==========================================
# ADUANA DE IDENTIDAD SOBERANA (Ostrom Principio 1)
# ==========================================
st.sidebar.header("🔑 PRINCIPIO 1: Fronteras")
nodo_id = st.sidebar.text_input("Código de Verificación del Nodo (Nodo_ID):", value="UNAM-OIKOS-GLOBAL-01")

# ==========================================
# CONMUTADOR DE FOCO METABÓLICO (TETRADIMENSIONAL)
# ==========================================
st.markdown("---")
foco_metabolico = st.radio(
    "Seleccione la Dimensión del Diagnóstico de Coherencia:",
    [
        "Producción Industrial (UPR)", 
        "Logística y Suministros (Termodinámica Comercial)", 
        "Riesgo Regulatorio y Compliance (Motor de Fragilidad)",
        "Coherencia de Carteras y Activos (Matriz Exergética Financiera)"
    ],
    horizontal=True
)

# ==========================================
# CONFIGURACIÓN DINÁMICA DEL RADAR (SISTEMA 4)
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 SISTEMA 4: Radar de Entorno")

if foco_metabolico == "Producción Industrial (UPR)":
    st.sidebar.markdown("*Monitoreo de perturbaciones exógenas de la infraestructura física (2020-2026)*")
    var_ext_1 = st.sidebar.slider("Riesgo de Choque Arancelario T-MEC (%):", 0, 100, 35)
    var_ext_2 = st.sidebar.slider("Índice de Canibalización por Insumo Asiático (%):", 0, 100, 50)
    var_ext_3 = st.sidebar.slider("Estrés de Capacidad Energética (Red CFE %):", 0, 100, 20)
    lambda_entorno = 1.0 + ((var_ext_1 + var_ext_2 + var_ext_3) / 300.0)

elif foco_metabolico == "Logística y Suministros (Termodinámica Comercial)":
    st.sidebar.markdown("*Monitoreo de latencia y estrangulamiento en redes de distribución*")
    var_ext_1 = st.sidebar.slider("Latencia en Puertos y Tráfico CDMX (%):", 0, 100, 40)
    var_ext_2 = st.sidebar.slider("Inflación y Volatilidad de Suministros (%):", 0, 100, 25)
    var_ext_3 = st.sidebar.slider("Cuellos de Botella Logísticos Globales (%):", 0, 100, 30)
    lambda_entorno = 1.0 + ((var_ext_1 + var_ext_2 + var_ext_3) / 300.0)

elif foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de Fragilidad)":
    st.sidebar.markdown("*Vectorización NLP de modificaciones normativas en tiempo real (DOF / CNBV / GAFI)*")
    var_ext_1 = st.sidebar.slider("Tasa de Reformas e Impacto DOF (%):", 0, 100, 45)
    var_ext_2 = st.sidebar.slider("Intensidad de Fiscalización CNBV / Banxico (%):", 0, 100, 65)
    var_ext_3 = st.sidebar.slider("Presión Normativa GAFI / Lavado Internacional (%):", 0, 100, 30)
    lambda_entorno = 1.0 + ((var_ext_1 + var_ext_2 + var_ext_3) / 300.0)

else:  
    st.sidebar.markdown("*Dinámicas fuera del equilibrio y acoplamientos ocultos en el mercado de capitales*")
    var_ext_1 = st.sidebar.slider("Riesgo Sistémico de Liquidez Global (%):", 0, 100, 55)
    var_ext_2 = st.sidebar.slider("Efecto de Cola Pesada (Shock No Lineal %):", 0, 100, 40)
    var_ext_3 = st.sidebar.slider("Correlación de Pánico Colectivo Inter-Activos (%):", 0, 100, 60)
    lambda_entorno = 1.0 + ((var_ext_1 + var_ext_2 + var_ext_3) / 300.0)

# ==========================================
# SISTEMA 1 Y SISTEMA 2: DIAGNÓSTICO DE FLUJOS Y FRICCIONES
# ==========================================
st.header(f"📥 SISTEMA 1: Diagnóstico de {foco_metabolico}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Flujos de Entrada e Inyección de Capacidad")
    if foco_metabolico == "Producción Industrial (UPR)":
        input_1 = st.number_input("Electricidad consumida (kWh):", min_value=0.0, value=120.0)
        input_2 = st.number_input("Diésel utilizado (Litros):", min_value=0.0, value=30.0)
        input_3 = st.number_input("Agua industrial incorporada (m³):", min_value=0.0, value=5.0)
        input_4 = st.number_input("Fuerza de trabajo aplicada (Horas-Hombre):", min_value=0.0, value=24.0)
        
        e_in_real = (
            (input_1 * FACTORES_CALIDAD["electricidad_kwh"]) +
            (input_2 * FACTORES_CALIDAD["diesel_litros"]) +
            (input_3 * FACTORES_CALIDAD["agua_m3"]) +
            (input_4 * FACTORES_CALIDAD["horas_hombre"])
        )
    elif foco_metabolico == "Logística y Suministros (Termodinámica Comercial)":
        input_1 = st.number_input("Unidades de Mercancía Entrantes (Volumen):", min_value=0.0, value=500.0)
        input_2 = st.number_input("Fuerza de Trabajo Logística (Horas-Hombre):", min_value=0.0, value=15.0)
        input_3 = st.number_input("Combustible de Distribución (Litros):", min_value=0.0, value=100.0)
        
        e_in_real = (
            (input_1 * FACTORES_CALIDAD["suministro_unidad"]) +
            (input_2 * FACTORES_CALIDAD["horas_hombre"]) +
            (input_3 * FACTORES_CALIDAD["diesel_litros"])
        )
    elif foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de Fragilidad)":
        input_1 = st.number_input("Horas-Hombre de personal experto en Auditoría/Riesgo:", min_value=0.0, value=50.0)
        input_2 = st.number_input("Presupuesto / Soporte de Infraestructura Tecnológica:", min_value=0.0, value=20.0)
        input_3 = st.number_input("Fondo Líquido de Respaldo Corporativo (M-Pesos):", min_value=0.0, value=5.0)
        
        e_in_real = (
            (input_1 * FACTORES_CALIDAD["horas_auditoria"]) +
            (input_2 * FACTORES_CALIDAD["infraestructura_tech"]) +
            (input_3 * FACTORES_CALIDAD["capital_respaldo"])
        )
    else:  
        input_1 = st.number_input("Capital Asignado a Activos de Baja Entropía (M-Pesos):", min_value=0.0, value=150.0)
        input_2 = st.number_input("Volumen de Información Mutua Computada (Megabits):", min_value=0.0, value=45.0)
        input_3 = st.number_input("Fondo Inmune Desacoplado de Emergencia:", min_value=0.0, value=30.0)
        
        e_in_real = (
            (input_1 * FACTORES_CALIDAD["capital_respaldo"]) +
            (input_2 * FACTORES_CALIDAD["informacion_bits"]) +
            (input_3 * FACTORES_CALIDAD["capital_respaldo"])
        )

with col2:
    st.subheader("Fricciones de Vulnerabilidad Estructural")
    if foco_metabolico == "Producción Industrial (UPR)":
        friccion_1 = st.number_input("Mermas de material crítico (Kilogramos / Litros):", min_value=0.0, value=15.0)
        friccion_2 = st.number_input("Tiempos de espera o paros en línea (Minutos):", min_value=0.0, value=20.0)
        friccion_precio = st.slider("Índice de oscilación de precios fiduciarios (Volatilidad %):", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
        
        i_destroyed = ((friccion_1 * 450.0) + (friccion_2 * 120.0)) * (1.0 + (friccion_precio / 100.0)) * lambda_entorno
        
    elif foco_metabolico == "Logística y Suministros (Termodinámica Comercial)":
        friccion_1 = st.number_input("Retraso acumulado en entregas de inventario (Días):", min_value=0.0, value=3.0)
        friccion_2 = st.number_input("Mermas / Roturas materiales de stock (Unidades):", min_value=0.0, value=10.0)
        friccion_precio = st.slider("Inestabilidad fiduciaria de costos de transporte (%):", min_value=0.0, max_value=100.0, value=15.0, step=1.0)
        
        i_destroyed = ((friccion_1 * 2500.0) + (friccion_2 * 600.0)) * (1.0 + (friccion_precio / 100.0)) * lambda_entorno
        
    elif foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de Fragilidad)":
        friccion_1 = st.number_input("Expedientes de clientes / Contratos rezagados sin indexar:", min_value=0.0, value=15.0)
        friccion_2 = st.number_input("Latencia en adopción de Circulares de la CNBV (Días de retraso):", min_value=0.0, value=30.0)
        friccion_precio = st.slider("Volatilidad monetaria e inestabilidad financiera nominal (%):", min_value=0.0, max_value=100.0, value=15.0, step=1.0)
        
        i_destroyed = ((friccion_1 * 950.0) + (friccion_2 * 400.0)) * (1.0 + (friccion_precio / 100.0)) * lambda_entorno
        
    else:  
        friccion_1 = st.number_input("Entropía Cruzada excedente entre activos correlacionados:", min_value=0.0, value=8.5)
        friccion_2 = st.number_input("Divergencia de Kullback-Leibler respecto al equilibrio de mercado:", min_value=0.0, value=14.0)
        friccion_precio = st.slider("Grado de apalancamiento sintético expuesto en colas pesadas (%):", min_value=0.0, max_value=100.0, value=25.0, step=1.0)
        
        i_destroyed = ((friccion_1 * 4500.0) + (friccion_2 * 1800.0)) * (1.0 + (friccion_precio / 100.0)) * lambda_entorno

# ==========================================
# BALANCES BRUTALISTAS DE GRIS OXFORD
# ==========================================
st.markdown("---")
st.header("📊 Balances de Coherencia Cibernética")

excedente_neto = e_in_real - i_destroyed

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)

with metrics_col1:
    st.markdown(f"""
    <div style="background-color: #1a1a1a; padding: 25px; border: 1px solid #2a2a2a; border-radius: 4px; text-align: left;">
        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #888888; font-weight: bold;">Capacidad de Entrada Unificada (E_in)</span>
        <p style="font-size: 38px; font-family: 'Courier New', monospace; font-weight: bold; color: #ffffff; margin: 10px 0 0 0;">{e_in_real:,.2f} <span style="font-size: 18px; color: #666666;">W/U</span></p>
    </div>
    """, unsafe_allow_html=True)

with metrics_col2:
    st.markdown(f"""
    <div style="background-color: #1a1a1a; padding: 25px; border: 1px solid #2a2a2a; border-radius: 4px; text-align: left;">
        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #888888; font-weight: bold;">Potencia Destruida por Entropía (I_destroyed)</span>
        <p style="font-size: 38px; font-family: 'Courier New', monospace; font-weight: bold; color: #ff6b6b; margin: 10px 0 0 0;">{i_destroyed:,.2f} <span style="font-size: 18px; color: #993333;">W/U</span></p>
    </div>
    """, unsafe_allow_html=True)

with metrics_col3:
    st.markdown(f"""
    <div style="background-color: #1a1a1a; padding: 25px; border: 1px solid #2a2a2a; border-radius: 4px; text-align: left;">
        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #888888; font-weight: bold;">Excedente de Inmunidad Neto Disponible</span>
        <p style="font-size: 38px; font-family: 'Courier New', monospace; font-weight: bold; color: #4ade80; margin: 10px 0 0 0;">{max(0.0, excedente_neto):,.2f} <span style="font-size: 18px; color: #228844;">W/U</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if e_in_real > 0:
    if i_destroyed > e_in_real:
        st.error("🛑 VIOLACIÓN TERMODINÁMICA SISTÉMICA: La fricción y las vulnerabilidades han colapsado la entrada. Estructura inviable.")
    else:
        eficiencia_real = (excedente_neto / e_in_real) * 100
        
        if eficiencia_real >= 85.0:
            st.success(f"✅ Homeostasis y Robustez Consolidada. Eficiencia del Sistema: {eficiencia_real:.2f}%")
        elif eficiencia_real >= 60.0:
            st.warning(f"⚠️ Alerta Crítica de Entropía. Sistema disipativo ante el Radar. Eficiencia Real: {eficiencia_real:.2f}%")
        else:
            st.error(f"🛑 Degradación Estructural Aguda. Pérdida inminente de viabilidad: {eficiencia_real:.2f}%")

        # ==========================================
        # SISTEMA 3: ARBITRAJE INTERNO (Ostrom)
        # ==========================================
        st.markdown("---")
        st.header("⚙️ SISTEMA 3: Política de Asignación Exergética Táctica")
        st.markdown("*Distribución analítica del excedente real neto en vectores de inmunidad de la firma*")
        
        alloc_control_col1, alloc_control_col2, alloc_control_col3 = st.columns(3)
        
        if foco_metabolico == "Producción Industrial (UPR)":
            label_maint = "🛡️ Mantenimiento Técnico / Infraestructura (%):"
            label_assets = "📈 Reserva de Activos Reales (%):"
        elif foco_metabolico == "Logística y Suministros (Termodinámica Comercial)":
            label_maint = "🛡️ Seguridad de Inventario y Rutas (%):"
            label_assets = "📈 Activos Fijos Stock (%):"
        elif foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de Fragilidad)":
            label_maint = "🛡️ NLP Leyes y Automatización (%):"
            label_assets = "📈 Fondo Legal Indexado Preventivo (%):"
        else: 
            label_maint = "🛡️ Cobertura No Lineal contra Colas Pesadas (%):"
            label_assets = "📈 Recalibración Estocástica de Portafolio (%):"
            
        label_slack = "🌪️ Holgura / Amortiguación de Emergencia (%):"
        
        with alloc_control_col1:
            r_maint = st.slider(label_maint, min_value=5, max_value=40, value=15, step=1)
        with alloc_control_col2:
            r_assets = st.slider(label_assets, min_value=5, max_value=40, value=15, step=1)
        with alloc_control_col3:
            r_slack = st.slider(label_slack, min_value=0, max_value=20, value=10, step=1)
        
        porcentaje_resiliencia_total = r_maint + r_assets + r_slack
        porcentaje_salida = 100 - porcentaje_resiliencia_total
        
        if porcentaje_resiliencia_total > 90:
            st.error(f"⚠️ ERROR DE ASIGNACIÓN: La resiliencia total ({porcentaje_resiliencia_total}%) asfixia la potencia útil de salida exterior.")
        elif porcentaje_resiliencia_total < 10:
            st.error(f"⚠️ ERROR DE ASIGNACIÓN: La resiliencia total ({porcentaje_resiliencia_total}%) es peligrosamente baja.")
        else:
            nivel_sancion = 0
            motivo_sancion = "Cumplimiento total de las reglas de apropiación común y blindaje recíproco."
            
            if eficiencia_real < 75.0 and porcentaje_resiliencia_total < 35:
                nivel_sancion = 1
                motivo_sancion = "Sanción Grado 1: El nodo presenta degradación estructural o fragilidad, y una reserva común insuficiente (<35%). Se confisca preventivamente el 15% de la Viabilidad Libre para reinyectarse al Mantenimiento Colectivo."
            
            if r_maint == 5 or r_assets == 5:
                nivel_sancion = 2
                motivo_sancion = f"Sanción Grado 2 (VETO JURÍDICO): El {nodo_id} ha desprotegido el fondo de mitigación situándolo en el mínimo legal (5%). Intento de extracción oportunista detectado. Escritura bloqueada."

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
            
            st.subheader("📊 Distribución Final de Potencia Activa (Gris Oxford + Semaforización Noire)")
            
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
                estilo_salida = "background-color: #261212; color: #ff6b6b; border: 1px solid #7f1d1d;"
            elif porcentaje_salida_efectivo >= 40:
                estilo_salida = "background-color: #1a1a1a; color: #4ade80; border: 1px solid #14532d;"
            else:
                estilo_salida = "background-color: #211d14; color: #facc15; border: 1px solid #713f12;"

            res_col1, res_col2, res_col3, out_col = st.columns(4)
            
            if foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de Fragilidad)":
                title_card_1 = "⚙️ NLP Regulatorio"
                title_card_2 = "📦 Fondo Indexado"
                title_card_3 = "🛡️ Cobertura GAFI"
                title_card_4 = "🚀 Viabilidad Libre"
            elif foco_metabolico == "Logística y Suministros (Termodinámica Comercial)":
                title_card_1 = "⚙️ Resiliencia de Rutas"
                title_card_2 = "📦 Activos Fijos Stock"
                title_card_3 = "🛡️ Holgura Logística"
                title_card_4 = "🚀 Flujo de Salida"
            elif foco_metabolico == "Coherencia de Carteras y Activos (Matriz Exergética Financiera)":
                title_card_1 = "⚙️ Blindaje No Lineal"
                title_card_2 = "📦 Recalibración Inf."
                title_card_3 = "🛡️ Amortiguación Shock"
                title_card_4 = "🚀 Excedente Líquido"
            else:
                title_card_1 = "⚙️ Mantenimiento Planta"
                title_card_2 = "📦 Fondo de Activos"
                title_card_3 = "🛡️ Holgura Operativa"
                title_card_4 = "🚀 Salida Útil Real"

            with res_col1:
                st.markdown(f"""
                <div style="{estilo_maint} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #888888;'>{title_card_1}</h4>
                    <p style='font-size: 26px; font-family: \"Courier New\", monospace; font-weight: bold; margin: 15px 0;'>{potencia_maint:,.2f} W/U</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.7;'>({r_maint_efectivo}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with res_col2:
                st.markdown(f"""
                <div style="{estilo_assets} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #888888;'>{title_card_2}</h4>
                    <p style='font-size: 26px; font-family: \"Courier New\", monospace; font-weight: bold; margin: 15px 0;'>{potencia_assets:,.2f} W/U</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.7;'>({r_assets}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with res_col3:
                st.markdown(f"""
                <div style="{estilo_slack} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #888888;'>{title_card_3}</h4>
                    <p style='font-size: 26px; font-family: \"Courier New\", monospace; font-weight: bold; margin: 15px 0;'>{potencia_slack:,.2f} W/U</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.7;'>({r_slack}%)</span>
                </div>
                """, unsafe_allow_html=True)
                
            with out_col:
                st.markdown(f"""
                <div style="{estilo_salida} padding: 25px; border-radius: 4px; text-align: center;">
                    <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; color: #ffffff;'>{title_card_4}</h4>
                    <p style='font-size: 26px; font-family: \"Courier New\", monospace; font-weight: bold; margin: 15px 0;'>{potencia_salida_util:,.2f} W/U</p>
                    <span style='font-size: 12px; font-family: monospace; opacity: 0.7;'>({porcentaje_salida_efectivo}%)</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if nivel_sancion == 0:
                st.info(f"⚖️ **Auditoría Ostrom ({nodo_id}):** {motivo_sancion}")
            elif nivel_sancion == 1:
                st.warning(f"⚖️ **Auditoría Ostrom ({nodo_id}):** {motivo_sancion}")
            elif nivel_sancion == 2:
                st.error(f"⚖️ **🛡️ VETO DE CONTROL INSTITUCIONAL ACTIVADO ({nodo_id}):** {motivo_sancion}")

        # ========================================================
        # ADUANA COERCITIVA DE PERSISTENCIA
        # ========================================================
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Persistir Balance del VSM en el Lógos Inmutable"):
            if not db_disponible:
                st.warning("⚠️ Servidor central fuera de alcance. Registro retenido en memoria volátil de pantalla.")
            elif nivel_sancion == 2:
                st.error(f"🛑 ESCRITURA RECHAZADA: El {nodo_id} se encuentra bajo exclusión punitiva por desacato a las reglas de inmunidad recíproca.")
            else:
                try:
                    query = "INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);"
                    cursor.execute(query, (e_in_real, i_destroyed, eficiencia_real))
                    conn.commit()
                    st.success(f"Matriz de balance sellada inmutablemente para el {nodo_id}.")
                except Exception as db_err:
                    st.error(f"Fricción al escribir en la base de datos central: {db_err}")
else:
    st.info("A la espera de flujos y métricas en las fronteras del sistema para iniciar la transducción.")

st.sidebar.markdown("---")
if not db_disponible:
    st.sidebar.warning("📡 Red: Servidor Neon fuera de alcance. Modo Autónomo Localizado Activo.")
else:
    st.sidebar.success("📡 Red: Canal seguro sincronizado con el Lógos.")
