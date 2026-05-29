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
    "horas_hombre": 75.0,
    "suministro_unidad": 500.0 # Capacidad informacional por unidad de inventario
}

st.set_page_config(page_title="MPG - Motor Homeostático", page_icon="⚡", layout="wide")

# ==========================================
# CÁPSULA ESTÉTICA: MODERNISMO NOIRE AVANZADO
# ==========================================
st.markdown("""
<style>
    .stApp { background-color: #080808; color: #dcdcdc; font-family: 'SF Pro Display', sans-serif; }
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #1a1a1a !important;
        border-right: 1px solid #2d2d2d !important;
    }
    h1, h2, h3, h4, h5, h6, label { color: #f5f5f5 !important; font-weight: 500 !important; }
    .stNumberInput input, .stTextInput input {
        background-color: #121212 !important; color: #ffffff !important;
        border: 1px solid #222222 !important; font-family: monospace !important;
    }
    hr { border-top: 1px solid #2d2d2d !important; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ MOTOR DE GOBERNABILIDAD HOMEOSTÁTICA")
st.caption("Cleronomía: Gestión de Sistemas Viables, Bienes Comunes y Termodinámica Comercial")

# ==========================================
# CONEXIÓN A LA MEMORIA INMUTABLE
# ==========================================
db_disponible = False
conn = None
cursor = None
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    st.success("🔗 Sincronización con el Lógos central activa.")
    db_disponible = True
except Exception:
    db_disponible = False

# ==========================================
# ADUANA DE IDENTIDAD Y RADAR (SISTEMA 4)
# ==========================================
st.sidebar.header("🔑 PRINCIPIO 1: Fronteras")
nodo_id = st.sidebar.text_input("Código Nodo (Nodo_ID):", value="UNAM-OIKOS-LOG-01")

st.sidebar.markdown("---")
st.sidebar.header("📡 SISTEMA 4: Radar de Entorno")
st.sidebar.markdown("*Perturbaciones Logísticas y Macroeconómicas*")

# Variables de entorno para el Radar
disrupcion_logistica = st.sidebar.slider("Latencia en Puertos/Tráfico (CDMX %):", 0, 100, 30)
inflacion_insumos = st.sidebar.slider("Inflación de Suministros (Volatilidad %):", 0, 100, 20)
estres_red = st.sidebar.slider("Estrés de Capacidad Estructural (%):", 0, 100, 15)

# Factor de Perturbación Logística (Λ)
lambda_entorno = 1.0 + ((disrupcion_logistica + inflacion_insumos + estres_red) / 300.0)

# ==========================================
# SELECCIÓN DEL FOCO METABÓLICO (NUEVO MÓDULO)
# ==========================================
st.markdown("---")
foco_metabolico = st.radio(
    "Seleccione el Foco del Diagnóstico Metabólico:",
    ["Producción Industrial (UPR)", "Logística y Suministros (Termodinámica Comercial)"],
    horizontal=True
)

st.header(f"📥 SISTEMA 1: Transducción de {foco_metabolico}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Entradas de Flujo Real")
    if foco_metabolico == "Producción Industrial (UPR)":
        in_1 = st.number_input("Electricidad (kWh):", min_value=0.0, value=120.0)
        in_2 = st.number_input("Diésel (Litros):", min_value=0.0, value=30.0)
        in_3 = st.number_input("Horas-Hombre:", min_value=0.0, value=24.0)
        e_in_real = (in_1 * 1000) + (in_2 * 10500) + (in_3 * 75)
    else:
        in_1 = st.number_input("Unidades de Mercancía Entrantes:", min_value=0.0, value=500.0)
        in_2 = st.number_input("Horas-Hombre Logística:", min_value=0.0, value=15.0)
        in_3 = st.number_input("Combustible Transporte (Litros):", min_value=0.0, value=100.0)
        e_in_real = (in_1 * FACTORES_CALIDAD["suministro_unidad"]) + (in_2 * 75) + (in_3 * 10500)

with col2:
    st.subheader("Fricciones y Disipación (Entropía)")
    if foco_metabolico == "Producción Industrial (UPR)":
        f_1 = st.number_input("Mermas de Material (Kg):", min_value=0.0, value=15.0)
        f_2 = st.number_input("Paros en Línea (Minutos):", min_value=0.0, value=20.0)
        i_destroyed = ((f_1 * 450) + (f_2 * 120)) * lambda_entorno
    else:
        f_1 = st.number_input("Retraso en Entrega (Días):", min_value=0.0, value=3.0)
        f_2 = st.number_input("Mermas/Roturas de Inventario (Unidades):", min_value=0.0, value=10.0)
        # En logística, el retraso disipa potencia por unidad de tiempo y volumen
        i_destroyed = ((f_1 * 2500) + (f_2 * 600)) * lambda_entorno

# ==========================================
# BALANCES BRUTALISTAS (SISTEMA 2)
# ==========================================
st.markdown("---")
st.header("📊 Balances de Coherencia Cibernética")
excedente_neto = e_in_real - i_destroyed

c1, c2, c3 = st.columns(3)
for col, title, val, color in zip([c1, c2, c3], 
    ["Ingreso Exergético Real", "Potencia Destruida", "Excedente Neto Disponible"],
    [e_in_real, i_destroyed, max(0.0, excedente_neto)],
    ["#ffffff", "#ff6b6b", "#4ade80"]):
    with col:
        st.markdown(f"""<div style="background-color: #1a1a1a; padding: 25px; border: 1px solid #2a2a2a; border-radius: 4px; text-align: left;">
            <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #888888; font-weight: bold;">{title}</span>
            <p style="font-size: 38px; font-family: 'Courier New', monospace; font-weight: bold; color: {color}; margin: 10px 0 0 0;">{val:,.2f} <span style="font-size: 18px; color: #555555;">W</span></p>
        </div>""", unsafe_allow_html=True)

if e_in_real > 0:
    if i_destroyed > e_in_real:
        st.error("🛑 VIOLACIÓN TERMODINÁMICA: La fricción logística ha devorado el ingreso.")
    else:
        eficiencia = (excedente_neto / e_in_real) * 100
        if eficiencia >= 85: st.success(f"✅ Homeostasis Consolidada. Eficiencia: {eficiencia:.2f}%")
        elif eficiencia >= 60: st.warning(f"⚠️ Sistema Disipativo. Eficiencia: {eficiencia:.2f}%")
        else: st.error(f"🛑 Colapso Estructural. Eficiencia: {eficiencia:.2f}%")

        # ==========================================
        # ASIGNACIÓN TÁCTICA (SISTEMA 3)
        # ==========================================
        st.markdown("---")
        st.header("⚙️ SISTEMA 3: Política de Homeostasis Interna")
        st.markdown("*Asignación de excedente para Resiliencia vs Salida Útil*")
        
        ac1, ac2, ac3 = st.columns(3)
        with ac1: r_maint = st.slider("🛡️ Mantenimiento/Seguridad (%):", 5, 40, 15)
        with ac2: r_assets = st.slider("📈 Reserva de Activos (%):", 5, 40, 15)
        with ac3: r_slack = st.slider("🌪️ Holgura/Contingencia (%):", 0, 20, 10)
        
        res_total = r_maint + r_assets + r_slack
        salida_libre = 100 - res_total
        
        # Auditoría Ostrom
        nivel_sancion = 0
        if eficiencia < 75 and res_total < 35:
            nivel_sancion = 1
            st.warning("⚖️ Sanción Ostrom G1: Resiliencia insuficiente. Se confisca 15% de salida.")
        if r_maint == 5 or r_assets == 5:
            nivel_sancion = 2
            st.error("⚖️ Sanción Ostrom G2: Negligencia extrema. Veto de salida.")

        # Flujos ajustados
        multa = 15.0 if nivel_sancion == 1 else 0.0
        p_salida = max(0.0, (salida_libre - multa)) if nivel_sancion < 2 else 0.0
        p_maint = r_maint + multa
        
        # Visualización Semaforizada
        st.subheader("📊 Distribución Final de Potencia Activa")
        def card(title, val, perc, color_bg, color_text):
            return f"""<div style="background-color: {color_bg}; color: {color_text}; padding: 25px; border-radius: 4px; text-align: center; border: 1px solid #333;">
                <h4 style='margin: 0; text-transform: uppercase; font-size: 11px; letter-spacing: 2px; opacity: 0.8;'>{title}</h4>
                <p style='font-size: 26px; font-family: "Courier New", monospace; font-weight: bold; margin: 15px 0;'>{val:,.2f} W</p>
                <span style='font-size: 12px; opacity: 0.7;'>({perc}%)</span>
            </div>"""

        cols = st.columns(4)
        data = [
            ("Mantenimiento", excedente_neto * (p_maint/100), p_maint, "#1a1a1a", "#4ade80"),
            ("Reserva Activos", excedente_neto * (r_assets/100), r_assets, "#1a1a1a", "#4ade80"),
            ("Holgura/Slack", excedente_neto * (r_slack/100), r_slack, "#1a1a1a", "#4ade80"),
            ("Salida Útil", excedente_neto * (p_salida/100), p_salida, "#1a1a1a" if nivel_sancion<2 else "#330d0d", "#ffffff" if nivel_sancion<2 else "#ff4545")
        ]
        for c, d in zip(cols, data):
            c.markdown(card(*d), unsafe_allow_html=True)

        if st.button("💾 Persistir Balance del VSM"):
            if nivel_sancion == 2: st.error("Escritura bloqueada por infracción Ostrom.")
            elif db_disponible:
                cursor.execute("INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);", (e_in_real, i_destroyed, eficiencia))
                conn.commit()
                st.success(f"Registro inmutable sellado para {nodo_id}.")
            else: st.warning("Memoria local activa únicamente.")

st.sidebar.markdown("---")
if not db_disponible: st.sidebar.warning("📡 Modo Autónomo Localizado.")
else: st.sidebar.success("📡 Sincronización activa.")
