import streamlit as st
import psycopg2
from datetime import datetime

# 1. Configuración Estética (Alineada al Minimalismo Funcional de M&PG)
st.set_page_config(page_title="MPG - Panel de Control UPR", page_icon="⚡", layout="centered")
st.title("Metric & Power Group ⚡ UPR Input")
st.write("---")

# 2. Vector de Conexión Absoluto (Pega aquí tu cadena de Neon)
DB_URL = "postgresql://alexcejudo98:ep_dark_sound_p5p4wzrm@ep-dark-sound-a5x836m4.us-east-2.aws.neon.tech/neondb?sslmode=require"
import streamlit as str
import psycopg2

# ==========================================
# CONFIGURACIÓN DE PARÁMETROS BIOFÍSICOS (𝛽)
# ==========================================
# Factores de Calidad Energética basados en la Segunda Ley 
# Transducen unidades nativas a Watts de potencia exergética equivalente.
FACTORES_CALIDAD = {
    "electricidad_kwh": 1000.0,    # 1 kWh = 1000 W durante 1 hora (Exergía pura ~ 1.0)
    "diesel_litros": 10500.0,     # 1 Litro de diésel ≈ 38 MJ/L bruto. Con un 𝛽 técnico de ~0.35, equivale a aprox. 10,500 W útiles disipables en flujo continuo horario.
    "agua_m3": 150.0,             # Exergía química y potencial de presión promedio por m3.
    "horas_hombre": 75.0          # Potencia metabólica promedio de un trabajador en actividad industrial (𝛽 de grano fino).
}

# Conexión al Lógos de Neon (Tu variable corregida de la Línea 11)
DB_URL = "postgresql://alexcejudo98:ep_dark_sound_p5p4wzrm@ep-dark-sound-a5x836m4.us-east-2.aws.neon.tech/neondb?sslmode=require"

str.set_page_config(page_title="MPG - UPR v1.1", page_icon="⚡", layout="wide")

str.title("⚡ METRIC & POWER GROUP // UNIDAD DE PROCESAMIENTO REAL")
str.caption("Módulo de Transducción Bioeconómica y Auditoría Exergética de Grano Fino")

# Intentar conexión inicial
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    str.success("🔗 Conexión con el Lógos consolidada exitosamente.")
except Exception as e:
    str.error("⚠️ Fricción de conexión: No se pudo conectar con el Lógos. Revisa la DB_URL.")
    str.stop()

# ==========================================
# INTERFAZ DE CAPTURA EN UNIDADES NATIVAS
# ==========================================
str.header("📥 Transducción de Insumos Heterogéneos")

col1, col2 = str.columns(2)

with col1:
    str.subheader("Entradas al Oikos (Unidades Nativas)")
    input_kwh = str.number_input("Electricidad consumida (kWh):", min_value=0.0, value=0.0, step=1.0)
    input_diesel = str.number_input("Diésel utilizado (Litros):", min_value=0.0, value=0.0, step=1.0)
    input_agua = str.number_input("Agua industrial incorporada (m³):", min_value=0.0, value=0.0, step=1.0)
    input_human = str.number_input("Fuerza de trabajo aplicada (Horas-Hombre):", min_value=0.0, value=0.0, step=1.0)

with col2:
    str.subheader("Disipación del Sistema")
    # El desperdicio se declara directamente en la potencia térmica disipada observada en los sensores
    e_out = str.number_input("Desperdicio / Disipación térmica observada (Watts):", min_value=0.0, value=0.0, step=10.0)

# ==========================================
# MÓDULO DE TRANSDUCCIÓN MATEMÁTICA (𝛽 · E)
# ==========================================
def transducir_ingreso_exergetico(kwh, diesel, agua, horas):
    """
    Ejecuta el arbitraje biofísico. Multiplica la materia y energía heterogénea
    por sus factores de calidad termodinámica para unificar el Oikos en Watts reales.
    """
    w_electricidad = kwh * FACTORES_CALIDAD["electricidad_kwh"]
    w_diesel = diesel * FACTORES_CALIDAD["diesel_litros"]
    w_agua = agua * FACTORES_CALIDAD["agua_m3"]
    w_human = horas * FACTORES_CALIDAD["horas_hombre"]
    
    # El ingreso exergético total es la sumatoria de las potencias útiles reales
    return w_electricidad + w_diesel + w_agua + w_human

# Calcular la Entrada Exergética Real (E_in unificada)
e_in_real = transducir_ingreso_exergetico(input_kwh, input_diesel, input_agua, input_human)

# ==========================================
# VALIDACIÓN Y BALANCE ENTRÓPICO
# ==========================================
str.header("📊 Balance Exergético de Grano Fino")

metrics_col1, metrics_col2 = str.columns(2)
metrics_col1.metric("Entrada Exergética Real Unificada (E_in)", f"{e_in_real:,.2f} Watts")
metrics_col2.metric("Disipación Entrópica (E_out)", f"{e_out:,.2f} Watts")

if e_in_real > 0:
    # Verificación de la frontera física
    if e_out > e_in_real:
        str.error(f"⚠️ VIOLACIÓN TERMODINÁMICA: La disipación ({e_out} W) no puede ser mayor que el ingreso exergético real ({e_in_real:.2f} W). Operación físicamente imposible según la Segunda Ley.")
    else:
        eficiencia_real = ((e_in_real - e_out) / e_in_real) * 100
        str.success(f"✅ Estado del Oikos Coherente. Eficiencia Exergética Real del Sistema: {eficiencia_real:.2f}%")
        
        # Botón para persistir en las tablas de Neon
        if str.button("💾 Persistir Medición en el Lógos"):
            try:
                # Aquí se asume que tu tabla tiene columnas preparadas para registrar el balance exergético real
                query = "INSERT INTO metric_history (e_in, e_out, efficiency) VALUES (%s, %s, %s);"
                cursor.execute(query, (e_in_real, e_out, eficiencia_real))
                conn.commit()
                str.info("Datos integrados a la memoria inmutable del servidor.")
            except Exception as db_err:
                str.error(f"Fricción al escribir en la DB: {db_err}")
else:
    str.info("A la espera de flujos de insumos en las fronteras del sistema.")
def query_execute(query, params=(), fetch=False):
    with psycopg2.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            if fetch:
                return cur.fetchall()
            conn.commit()

# 3. Interfaz Visual de Captura
st.subheader("Auditoría Energética Inicial (Simulación de Sensor)")
st.write("Introduzca las variables metabólicas recolectadas en el nodo industrial.")

with st.form("upr_sensor_entry"):
    # Selector dinámico que jala las empresas directo de la Base de Datos
    try:
        nodos_raw = query_execute("SELECT nodo_id, nombre_empresa FROM vsm_organizational_nodes;", fetch=True)
        nodos_dict = {f"{r[0]} | {r[1]}": r[0] for r in nodos_raw}
        nodo_seleccionado = st.selectbox("Nodo Organizacional Activo (VSM)", options=list(nodos_dict.keys()))
    except Exception:
        st.error("Fricción de conexión: No se pudo conectar con el Lógos. Revisa la DB_URL.")
        nodo_seleccionado = None

    # Entradas numéricas para el consultor
    e_in = st.number_input("Entrada Exergética Útil (Watts)", min_value=0.0, step=100.0, format="%.2f")
    e_out = st.number_input("Disipación Entrópica / Desperdicio (Watts)", min_value=0.0, step=100.0, format="%.2f")
    
    submit = st.form_submit_button("Inyectar Flujo a la UPR")

# 4. Validación Termodinámica e Inyección
if submit and nodo_seleccionado:
    if e_out > e_in:
        st.error("⚠️ Violación Termodinámica: La disipación no puede ser mayor que la entrada.")
    elif e_in == 0:
        st.warning("⚠️ Nodo Inactivo: La entrada energética no puede ser cero.")
    else:
        nodo_id = nodos_dict[nodo_seleccionado]
        timestamp = datetime.now()
        
        insert_query = """
        INSERT INTO upr_metabolic_flux (nodo_id, timestamp_sat, e_ex_in_watts, e_ex_out_entropy)
        VALUES (%s, %s, %s, %s);
        """
        try:
            query_execute(insert_query, (nodo_id, timestamp, e_in, e_out))
            st.success(f"⚡ Inyección Exitosa. Flujo autónomo retenido: {e_in - e_out:.2f} W")
        except Exception as e:
            st.error(f"Fricción en el almacenamiento: {e}")
