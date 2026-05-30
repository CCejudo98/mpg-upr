import streamlit as st
import psycopg2
from datetime import datetime

# ==========================================
# VECTOR DE CONEXIÓN INMUTABLE (NEON)
# ==========================================
DB_URL = "postgresql://neondb_owner:npg_4IuJofqBpE3v@ep-patient-pine-apfibhxx-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require

# ==========================================
# EQUIVALENCIAS DE COSTO Y EFICIENCIA (𝛽)
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

# Costos unitarios para calcular el ahorro real en pesos
COSTOS_MONETARIOS = {
    "Producción y Fábrica": 0.0045,          
    "Logística y Almacén": 1.25, 
    "Cumplimiento Legal y Riesgos": 2.50, 
    "Inversiones y Dinero": 5.00 
}

st.set_page_config(page_title="MPG - Sistema de Ahorro Inteligente", page_icon="📈", layout="wide")

# ==========================================
# ESTILO VISUAL: BUSINESS NAVY (MENOS INTIMIDANTE)
# ==========================================
st.markdown("""
<style>
    /* Fondo Azul Marino Profesional */
    .stApp {
        background-color: #001f3f;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Barra Lateral Gris Oxford (Contraste de Control) */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #1a1a1a !important;
        border-right: 2px solid #003366 !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h4 {
        color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6, label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* Entradas de datos claras */
    .stNumberInput input, .stTextInput input {
        background-color: #f0f2f6 !important;
        color: #001f3f !important;
        border-radius: 5px !important;
    }
    
    .stSlider {
        padding-bottom: 20px !important;
    }

    hr {
        border-top: 1px solid #003366 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("📈 SISTEMA DE GESTIÓN DE EFICIENCIA Y AHORRO")
st.caption("Metric & Power Group // El monitor de salud financiera y operativa para su negocio.")

# ==========================================
# CONEXIÓN A LA BASE DE DATOS
# ==========================================
db_disponible = False
conn = None
cursor = None
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS metric_history (id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, e_in DOUBLE PRECISION, e_out DOUBLE PRECISION, efficiency DOUBLE PRECISION);")
    conn.commit()
    st.sidebar.success("✅ Conexión con Servidor Central Activa")
    db_disponible = True
except Exception:
    st.sidebar.warning("⚠️ Operando en modo local (sin internet)")
    db_disponible = False

# ==========================================
# CONFIGURACIÓN DE LICENCIA Y RIESGOS (BARRA LATERAL)
# ==========================================
st.sidebar.header("🔑 Registro de Empresa")
nodo_id = st.sidebar.text_input("Nombre de su Empresa / Sucursal:", value="Mi PYME Eficiente 01")

st.sidebar.markdown("---")
st.sidebar.header("💼 Costo del Software")
costo_licencia = st.sidebar.number_input("Inversión Anual en este Software (MXN):", min_value=0.0, value=15000.0, step=1000.0)

st.sidebar.markdown("---")
st.sidebar.header("📡 Monitor del Mercado")
st.sidebar.markdown("*Ajuste según cómo vea la situación económica externa*")

if 'foco' not in st.session_state: st.session_state.foco = "Producción y Fábrica"

risk_1 = st.sidebar.slider("Inestabilidad de Precios/Inflación (%):", 0, 100, 20)
risk_2 = st.sidebar.slider("Problemas con Proveedores/Entregas (%):", 0, 100, 15)
risk_3 = st.sidebar.slider("Carga de Impuestos y Trámites (%):", 0, 100, 10)
lambda_entorno = 1.0 + ((risk_1 + risk_2 + risk_3) / 300.0)

# ==========================================
# SELECTOR DE ÁREA DEL NEGOCIO
# ==========================================
st.markdown("---")
foco_metabolico = st.radio(
    "¿Qué parte de su negocio desea analizar hoy?",
    ["Producción y Fábrica", "Logística y Almacén", "Cumplimiento Legal y Riesgos", "Inversiones y Dinero"],
    horizontal=True
)

# ==========================================
# ENTRADA DE DATOS DEL DÍA (SISTEMA 1)
# ==========================================
st.header(f"📥 Registro de Operación: {foco_metabolico}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("¿Qué recursos utilizó hoy?")
    if foco_metabolico == "Producción y Fábrica":
        in_1 = st.number_input("Luz consumida (kWh):", min_value=0.0, value=100.0)
        in_2 = st.number_input("Combustible/Gas (Litros):", min_value=0.0, value=50.0)
        in_3 = st.number_input("Horas de personal trabajadas:", min_value=0.0, value=40.0)
        e_in_real = (in_1 * 1000) + (in_2 * 10500) + (in_3 * 75)
    elif foco_metabolico == "Logística y Almacén":
        in_1 = st.number_input("Unidades de mercancía recibidas:", min_value=0.0, value=200.0)
        in_2 = st.number_input("Horas de choferes/almacén:", min_value=0.0, value=15.0)
        in_3 = st.number_input("Gasolina transporte (Litros):", min_value=0.0, value=80.0)
        e_in_real = (in_1 * 500) + (in_2 * 75) + (in_3 * 10500)
    elif foco_metabolico == "Cumplimiento Legal y Riesgos":
        in_1 = st.number_input("Horas dedicadas a trámites/contabilidad:", min_value=0.0, value=10.0)
        in_2 = st.number_input("Gasto en sistemas de administración:", min_value=0.0, value=5.0)
        in_3 = st.number_input("Fondo de emergencia en caja (Miles):", min_value=0.0, value=20.0)
        e_in_real = (in_1 * 500) + (in_2 * 250) + (in_3 * 1000)
    else: # Inversiones
        in_1 = st.number_input("Dinero invertido en activos seguros (Miles):", min_value=0.0, value=100.0)
        in_2 = st.number_input("Nivel de información de mercado (0-100):", min_value=0.0, value=50.0)
        in_3 = st.number_input("Dinero en efectivo disponible (Miles):", min_value=0.0, value=50.0)
        e_in_real = (in_1 * 1000) + (in_2 * 850) + (in_3 * 1000)

with col2:
    st.subheader("¿Qué problemas o desperdicios hubo?")
    if foco_metabolico == "Producción y Fábrica":
        f_1 = st.number_input("Material desperdiciado/mermas (Kg):", min_value=0.0, value=10.0)
        f_2 = st.number_input("Minutos de máquinas paradas:", min_value=0.0, value=30.0)
        i_destroyed = ((f_1 * 450) + (f_2 * 120)) * lambda_entorno
    elif foco_metabolico == "Logística y Almacén":
        f_1 = st.number_input("Días de retraso en entregas:", min_value=0.0, value=2.0)
        f_2 = st.number_input("Productos dañados o perdidos:", min_value=0.0, value=5.0)
        i_destroyed = ((f_1 * 2500) + (f_2 * 600)) * lambda_entorno
    elif foco_metabolico == "Cumplimiento Legal y Riesgos":
        f_1 = st.number_input("Documentos o facturas pendientes:", min_value=0.0, value=5.0)
        f_2 = st.number_input("Días de retraso en pagos/impuestos:", min_value=0.0, value=3.0)
        i_destroyed = ((f_1 * 950) + (f_2 * 400)) * lambda_entorno
    else: # Inversiones
        f_1 = st.number_input("Nivel de riesgo/desorden en cartera (0-10):", min_value=0.0, value=2.0)
        f_2 = st.number_input("Dinero estancado sin rendimientos (Miles):", min_value=0.0, value=10.0)
        i_destroyed = ((f_1 * 4500) + (f_2 * 1800)) * lambda_entorno

# ==========================================
# RESULTADOS DEL NEGOCIO (SISTEMA 2)
# ==========================================
st.markdown("---")
st.header("📊 Balance de Salud de su Negocio")

excedente_neto = e_in_real - i_destroyed
costo_unidad_perdida = COSTOS_MONETARIOS[foco_metabolico]
perdida_anual = i_destroyed * costo_unidad_perdida * 365.0
eficiencia_real = max(0.0, (excedente_neto / e_in_real) * 100.0) if e_in_real > 0 else 0.0

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px; border: 1px solid #003366;">
        <span style="font-size: 12px; text-transform: uppercase; color: #888;">Capacidad Total Utilizada</span>
        <p style="font-size: 32px; font-weight: bold; color: #ffffff; margin: 0;">{e_in_real:,.0f} <span style="font-size: 16px;">Puntos</span></p>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px; border: 1px solid #003366;">
        <span style="font-size: 12px; text-transform: uppercase; color: #888;">Nivel de Eficiencia</span>
        <p style="font-size: 32px; font-weight: bold; color: #4ade80; margin: 0;">{eficiencia_real:.1f}%</p>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px; border: 1px solid #772222;">
        <span style="font-size: 12px; text-transform: uppercase; color: #ff6b6b;">Dinero Perdido al Año</span>
        <p style="font-size: 32px; font-weight: bold; color: #ff6b6b; margin: 0;">${perdida_anual:,.2f} <span style="font-size: 16px;">MXN</span></p>
    </div>""", unsafe_allow_html=True)

# ==========================================
# PROYECCIÓN DE AHORROS Y ROI
# ==========================================
st.markdown("---")
st.header("💰 ¿Cuánto dinero le ahorra este sistema?")
ahorro_potencial = perdida_anual * 0.70  # El software reduce el 70% del desperdicio
ganancia_5_anos = (ahorro_potencial * 5) - (costo_licencia * 5)

pc1, pc2, pc3 = st.columns(3)
with pc1:
    st.markdown(f"""<div style="background-color: #0f3322; padding: 25px; border-radius: 8px;">
        <span style="color: #4ade80; font-size: 14px;">Ahorro Proyectado (Año 1)</span>
        <p style="font-size: 30px; font-weight: bold; color: #4ade80;">${ahorro_potencial:,.2f}</p>
    </div>""", unsafe_allow_html=True)
with pc2:
    roi_meses = (costo_licencia / (ahorro_potencial / 12)) if ahorro_potencial > 0 else 0
    st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px;">
        <span style="color: #aaa; font-size: 14px;">Su inversión se paga en:</span>
        <p style="font-size: 30px; font-weight: bold; color: #ffffff;">{roi_meses:.1f} Meses</p>
    </div>""", unsafe_allow_html=True)
with pc3:
    st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border-radius: 8px;">
        <span style="color: #aaa; font-size: 14px;">Ganancia Neta a 5 Años</span>
        <p style="font-size: 30px; font-weight: bold; color: #4ade80;">${ganancia_5_anos:,.2f}</p>
    </div>""", unsafe_allow_html=True)

# ==========================================
# REPARTO DE GANANCIAS Y ESCUDO FISCAL (SISTEMA 3)
# ==========================================
st.markdown("---")
st.header("⚙️ Plan de Reparto y Escudo Fiscal")
st.markdown("*Defina sus reservas y el monto a reinvertir para reducir su carga impositiva*")

sc1, sc2, sc3, sc4 = st.columns(4)
with sc1: res_maint = st.slider("Mantenimiento (%):", 5, 40, 15)
with sc2: res_stock = st.slider("Stock/Activos (%):", 5, 40, 15)
with sc3: res_emergencia = st.slider("Emergencias (%):", 0, 20, 10)
with sc4: fiscal_invest = st.number_input("Reinversión Fiscal (MXN):", min_value=0.0, value=0.0, step=1000.0)

# Lógica de persistencia de la directiva fiscal
if st.button("💾 Enviar Directiva y Guardar Informe"):
    if db_disponible:
        try:
            # 1. Guardado de métricas originales
            cursor.execute("INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);", 
                           (e_in_real, i_destroyed, eficiencia_real))
            
            # 2. Guardado de la Directiva Fiscal (Escritura para el Core)
            cursor.execute("""
                INSERT INTO public_fiscal_stats (foco, fiscal_investment, timestamp)
                VALUES (%s, %s, CURRENT_TIMESTAMP)
                ON CONFLICT (foco) 
                DO UPDATE SET fiscal_investment = EXCLUDED.fiscal_investment, timestamp = CURRENT_TIMESTAMP;
            """, (foco_metabolico, fiscal_invest))
            
            conn.commit()
            st.success("✅ Directiva fiscal enviada al Core y métricas guardadas.")
        except Exception as e:
            st.error(f"Error en la comunicación con el Lógos: {e}")
