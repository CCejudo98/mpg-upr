import streamlit as st
import psycopg2
from datetime import datetime

# 1. Configuración Estética (Alineada al Minimalismo Funcional de M&PG)
st.set_page_config(page_title="MPG - Panel de Control UPR", page_icon="⚡", layout="centered")
st.title("Metric & Power Group ⚡ UPR Input")
st.write("---")

# 2. Vector de Conexión Absoluto (Pega aquí tu cadena de Neon)
DB_URL = "postgresql://neondb_owner:npg-w3Bf0vRM@ep-patient-pine-apfibhxx.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require"

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
