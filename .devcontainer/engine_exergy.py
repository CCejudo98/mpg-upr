import streamlit as st
import psycopg2
from datetime import datetime
# ==========================================
# VECTOR DE CONEXIÓN INMUTABLE (NEON)
# ==========================================
DB_URL =
"postgresql://alexcejudo98:ep_dark_sound_p5p4wzrm@ep-dark-sound-a5x836
m4.us-east-2.aws.neon.tech/neondb?sslmode=require"
# ==========================================
# PARÁMETROS BIOFÍSICOS E INFORMACIONALES (β)
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
st.set_page_config(page_title="MPG - Exergy Core", page_icon="⚛️",
layout="wide")
# ==========================================
# CÁPSULA ESTÉTICA: MODERNISMO NOIRE PURO
# ==========================================
st.markdown("""
""", unsafe_allow_html=True)
st.title("⚛️ MOTOR DE OPTIMIZACIÓN EXERGÉTICA")
st.caption("Cleronomía Avanzada // Consola Soberana de Diagnóstico y
Control de Sistemas Viables Fuera del Equilibrio")

# ==========================================
# ENLACE CON EL LÓGOS DE DATOS
# ==========================================
db_disponible = False
conn = None
cursor = None
try:
conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS exergy_history (
id SERIAL PRIMARY KEY,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
foco VARCHAR(100),
e_in DOUBLE PRECISION,
i_destroyed DOUBLE PRECISION,
efficiency DOUBLE PRECISION
);
""")
conn.commit()
st.success("🔗 Sincronización inmutable con el repositorio de
exergía activa.")
db_disponible = True
except Exception as e:
st.sidebar.error(f"Fricción de enlace con DB: {e}")
db_disponible = False
# ==========================================
# ADUANA DE IDENTIDAD DEL OIKOS (Sistema 5)
# ==========================================
st.sidebar.header("🔑 SISTEMA 5: Soberanía")
nodo_id = st.sidebar.text_input("Identificador del Oikos (Nodo_ID):",
value="UNAM-CLERONOMIC-CORE")
# ==========================================
# SELECCIÓN DEL CANAL METABÓLICO DETALLADO
# ==========================================
st.markdown("---")
foco_metabolico = st.radio(
"Seleccione el Sector de Transducción Exergética:",
[
"Producción Industrial (UPR)",
"Logística y Suministros (Termodinámica Comercial)",
"Riesgo Regulatorio y Compliance (Motor de Fragilidad)",
"Coherencia de Carteras y Activos (Matriz Exergética

Financiera)"

],
horizontal=True
)
# ==========================================
# SISTEMA 4: RADAR DE PERTURBACIÓN AMBIENTAL
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📡 SISTEMA 4: Radar Termodinámico")
if foco_metabolico == "Producción Industrial (UPR)":
v_ext_1 = st.sidebar.slider("Estrés de Capacidad Estructural Red
CFE (%):", 0, 100, 25)
v_ext_2 = st.sidebar.slider("Degradación de Insumos Críticos por
Aranceles (%):", 0, 100, 35)
v_ext_3 = st.sidebar.slider("Variedad Inmanejable del Mercado
Colectivo (%):", 0, 100, 20)
elif foco_metabolico == "Logística y Suministros (Termodinámica
Comercial)":
v_ext_1 = st.sidebar.slider("Latencia y Atascamiento de Flujos
Urbanos (%):", 0, 100, 45)
v_ext_2 = st.sidebar.slider("Fricción Portuaria y de Aduanas
(%):", 0, 100, 30)
v_ext_3 = st.sidebar.slider("Disipación de Energía en Canales de
Distribución (%):", 0, 100, 25)
elif foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de
Fragilidad)":
v_ext_1 = st.sidebar.slider("Tasa de Mutación Normativa en el DOF
(%):", 0, 100, 50)
v_ext_2 = st.sidebar.slider("Intensidad Fiscalizadora de
Organismos Centrales (%):", 0, 100, 60)
v_ext_3 = st.sidebar.slider("Complejidad de Restricciones
GAFI/Internacionales (%):", 0, 100, 35)
else:
v_ext_1 = st.sidebar.slider("Riesgo de Ruptura de Liquidez
Sistémica (%):", 0, 100, 55)
v_ext_2 = st.sidebar.slider("Presencia de Colas Pesadas
Estocásticas (%):", 0, 100, 45)
v_ext_3 = st.sidebar.slider("Coeficiente de Acoplamiento y Pánico
de Activos (%):", 0, 100, 65)
lambda_entorno = 1.0 + ((v_ext_1 + v_ext_2 + v_ext_3) / 300.0)
# ==========================================
# SISTEMA 1 Y SISTEMA 2: BALANCES EXERGÉTICOS PUROS
# ==========================================
st.header(f"📥 SISTEMA 1: Transducción de Flujos - {foco_metabolico}")

col1, col2 = st.columns(2)
eficiencia_real = 0.0
with col1:
st.subheader("Inyección de Energía Útil (Exergía de Entrada)")
if foco_metabolico == "Producción Industrial (UPR)":
in_1 = st.number_input("Electricidad Incorporada (kWh):",

min_value=0.0, value=150.0)

in_2 = st.number_input("Combustible Hidrocarburo (Litros):",

min_value=0.0, value=40.0)

in_3 = st.number_input("Materia Hídrica de Proceso (m3):",

min_value=0.0, value=10.0)

in_4 = st.number_input("Trabajo Vivo Aplicado

(Horas-Hombre):", min_value=0.0, value=32.0)

e_in_real = (in_1 * FACTORES_CALIDAD["electricidad_kwh"]) +

(in_2 * FACTORES_CALIDAD["diesel_litros"]) + (in_3 *
FACTORES_CALIDAD["agua_m3"]) + (in_4 *
FACTORES_CALIDAD["horas_hombre"])
elif foco_metabolico == "Logística y Suministros (Termodinámica
Comercial)":

in_1 = st.number_input("Unidades Estructurales Entrantes

(Volumen):", min_value=0.0, value=600.0)

in_2 = st.number_input("Trabajo Logístico en Rutas

(Horas-Hombre):", min_value=0.0, value=20.0)

in_3 = st.number_input("Energía de Tracción - Diésel

(Litros):", min_value=0.0, value=120.0)

e_in_real = (in_1 * FACTORES_CALIDAD["suministro_unidad"]) +

(in_2 * FACTORES_CALIDAD["horas_hombre"]) + (in_3 *
FACTORES_CALIDAD["diesel_litros"])
elif foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de
Fragilidad)":

in_1 = st.number_input("Procesamiento Analítico Experto

(Horas-Auditoría):", min_value=0.0, value=60.0)

in_2 = st.number_input("Capacidad Informacional Instalada

(Tech Stack):", min_value=0.0, value=25.0)

in_3 = st.number_input("Activo Líquido de Mitigación

Estructural (M-Pesos):", min_value=0.0, value=8.0)

e_in_real = (in_1 * FACTORES_CALIDAD["horas_auditoria"]) +
(in_2 * FACTORES_CALIDAD["infraestructura_tech"]) + (in_3 *
FACTORES_CALIDAD["capital_respaldo"])
else:
in_1 = st.number_input("Asignación de Capital de Baja Entropía

(M-Pesos):", min_value=0.0, value=200.0)

in_2 = st.number_input("Información Mutua Calculada
Inter-Activos (Megabits):", min_value=0.0, value=60.0)

in_3 = st.number_input("Reserva de Coherencia Fuera del

Equilibrio:", min_value=0.0, value=40.0)

e_in_real = (in_1 * FACTORES_CALIDAD["capital_respaldo"]) +

(in_2 * FACTORES_CALIDAD["informacion_bits"]) + (in_3 *
FACTORES_CALIDAD["capital_respaldo"])
with col2:
st.subheader("Aniquilación de Capacidad por Irreversibilidades
(Entropía Destruida)")
if foco_metabolico == "Producción Industrial (UPR)":
f_1 = st.number_input("Mermas Estructurales de Material

(Kg):", min_value=0.0, value=12.0)

f_2 = st.number_input("Paros Críticos en Línea de Flujo

(Minutos):", min_value=0.0, value=25.0)

i_destroyed = ((f_1 * 450.0) + (f_2 * 120.0)) * lambda_entorno
elif foco_metabolico == "Logística y Suministros (Termodinámica
Comercial)":

f_1 = st.number_input("Latencia y Retraso en Red de

Distribución (Días):", min_value=0.0, value=4.0)

f_2 = st.number_input("Degradación de Inventario en Almacén

(Unidades):", min_value=0.0, value=12.0)

i_destroyed = ((f_1 * 2500.0) + (f_2 * 600.0)) *

lambda_entorno
elif foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de
Fragilidad)":

f_1 = st.number_input("Contratos y Expedientes No Indexados

(Caos Informacional):", min_value=0.0, value=20.0)

f_2 = st.number_input("Retraso en Adopción de Circulares CNBV

(Días de Brecha):", min_value=0.0, value=25.0)

i_destroyed = ((f_1 * 950.0) + (f_2 * 400.0)) * lambda_entorno
else:
f_1 = st.number_input("Entropía Cruzada Excedente
(Acoplamientos Ocultos):", min_value=0.0, value=10.5)

f_2 = st.number_input("Divergencia de Kullback-Leibler de la

Cartera:", min_value=0.0, value=16.0)

i_destroyed = ((f_1 * 4500.0) + (f_2 * 1800.0)) *

lambda_entorno
# ==========================================
# DIAGNÓSTICO DE LA ECUACIÓN COHERENTE (Sistema 2)
# ==========================================
st.markdown("---")
st.header("📊 SISTEMA 2: Diagnóstico de la Ecuación Coherente")
excedente_neto = e_in_real - i_destroyed
soberania_exergetica = (excedente_neto / e_in_real) * 100.0 if
e_in_real > 0 else 0.0
mc1, mc2, mc3 = st.columns(3)
with mc1:
st.markdown(f"""<div style="background-color: #111; padding: 25px;

border-radius: 4px; border: 1px solid #222;">

<span style="font-size: 11px; text-transform: uppercase;
letter-spacing: 1.5px; color: #888; font-weight: bold;">Ingreso
Exergético Real ($E_{{in}}$)</span>

<p style="font-size: 36px; font-family: monospace;

font-weight: bold; color: #fff; margin: 10px 0 0 0;">{e_in_real:,.2f}
<span style="font-size: 16px; color: #555;">W</span></p>
</div>""", unsafe_allow_html=True)
with mc2:
st.markdown(f"""<div style="background-color: #111; padding: 25px;
border-radius: 4px; border: 1px solid #222;">

<span style="font-size: 11px; text-transform: uppercase;
letter-spacing: 1.5px; color: #ff6b6b; font-weight: bold;">Potencia
Aniquilada ($I_{{destroyed}}$)</span>

<p style="font-size: 36px; font-family: monospace;
font-weight: bold; color: #ff6b6b; margin: 10px 0 0
0;">{i_destroyed:,.2f} <span style="font-size: 16px; color:
#933;">W</span></p>
</div>""", unsafe_allow_html=True)
with mc3:
st.markdown(f"""<div style="background-color: #111; padding: 25px;
border-radius: 4px; border: 1px solid #222;">

<span style="font-size: 11px; text-transform: uppercase;
letter-spacing: 1.5px; color: #4ade80; font-weight: bold;">Coeficiente
de Soberanía del Oikos ($S_e$)</span>

<p style="font-size: 36px; font-family: monospace;
font-weight: bold; color: #4ade80; margin: 10px 0 0
0;">{soberania_exergetica:.2f}%</p>
</div>""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
if e_in_real > 0:
if i_destroyed > e_in_real:
st.error("🛑 VIOLACIÓN TERMODINÁMICA CRÍTICA: La destrucción
de exergía ha superado la inyección de capacidad. Colapso del Oikos.")
else:
eficiencia_real = (excedente_neto / e_in_real) * 100.0
if eficiencia_real >= 85.0: st.success(f"✅ Homeostasis
Consolidada. Coherencia Sistémica: {eficiencia_real:.2f}%")
elif eficiencia_real >= 60.0: st.warning(f"⚠️ Régimen
Disipativo Crítico. Coherencia Sistémica: {eficiencia_real:.2f}%")
else: st.error(f"🛑 Degradación Irreversible del Sistema

Viable. Coherencia Sistémica: {eficiencia_real:.2f}%")
else:
st.info("A la espera de flujos vectoriales en las fronteras de
control.")

# ==========================================
# INCENTIVO ONTOLÓGICO: ACUMULACIÓN NEGENTRÓPICA
# ==========================================
st.markdown("---")
st.header("📈 Proyección de Acumulación Negentrópica y Autonomía de
Variedad")
st.markdown("*Cálculo de la capacidad de orden y blindaje
psicohistórico del sistema a largo plazo (Retorno de Variedad)*")
# Supuesto: El control del motor optimiza y recupera el 75% de la
exergía disipada
exergy_recuperada_anual = (i_destroyed * 0.75) * 365.0
variedad_ashby_acumulada_5_anos = exergy_recuperada_anual * 5.0
proy_col1, proy_col2, proy_col3 = st.columns(3)
with proy_col1:
st.markdown(f"""<div style="background-color: #0f1612; padding:
25px; border: 1px solid #14532d; border-radius: 4px;">

<span style="font-size: 11px; text-transform: uppercase;
letter-spacing: 1.5px; color: #4ade80; font-weight: bold;">Exergía
Retenida Anual</span>

<p style="font-size: 32px; font-family: monospace;
font-weight: bold; color: #4ade80; margin: 10px 0 0
0;">{exergy_recuperada_anual:,.2f} <span style="font-size:
16px;">W/año</span></p>
</div>""", unsafe_allow_html=True)
with proy_col2:
deuda_mitigada = (exergy_recuperada_anual / 100000.0)
st.markdown(f"""<div style="background-color: #111; padding: 25px;
border: 1px solid #222; border-radius: 4px;">

<span style="font-size: 11px; text-transform: uppercase;
letter-spacing: 1.5px; color: #aaa; font-weight: bold;">Mitigación de
Deuda Ontológica</span>

<p style="font-size: 32px; font-family: monospace;

font-weight: bold; color: #fff; margin: 10px 0 0
0;">{deuda_mitigada:.4f} <span style="font-size:
16px;">ψ-Core</span></p>
</div>""", unsafe_allow_html=True)
with proy_col3:
st.markdown(f"""<div style="background-color: #111; padding: 25px;
border: 1px solid #222; border-radius: 4px;">

<span style="font-size: 11px; text-transform: uppercase;
letter-spacing: 1.5px; color: #facc15; font-weight: bold;">Variedad
Expandida (5 Años)</span>

<p style="font-size: 32px; font-family: monospace;
font-weight: bold; color: #facc15; margin: 10px 0 0
0;">{variedad_ashby_acumulada_5_anos:,.2f} <span style="font-size:
16px;">Bits-Ω</span></p>

</div>""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📋 Matriz Quinquenal de Metamorfosis de la Capacidad
Estructural")
html_table = f"""
<table style="width:100%; border-collapse: collapse; background-color:
#111111; color: #dcdcdc; font-family: monospace; font-size: 14px;
text-align: left; border: 1px solid #222222;">
<tr style="background-color: #1a1a1a; border-bottom: 2px solid
#333333;">

<th style="padding: 12px; color: #ffffff;">Dimensión

Temporal</th>

<th style="padding: 12px; color: #ffffff;">Ciclo I</th>
<th style="padding: 12px; color: #ffffff;">Ciclo II</th>
<th style="padding: 12px; color: #ffffff;">Ciclo III</th>
<th style="padding: 12px; color: #ffffff;">Ciclo IV</th>
<th style="padding: 12px; color: #ffffff;">Ciclo V</th>
</tr>
<tr style="border-bottom: 1px solid #222222;">
<td style="padding: 12px; font-weight: bold;">Capacidad

Negentrópica Acumulada (W)</td>

<td style="padding: 12px;">{exergy_recuperada_anual:,.2f}</td>
<td style="padding:

12px;">{(exergy_recuperada_anual*2):,.2f}</td>

<td style="padding:

12px;">{(exergy_recuperada_anual*3):,.2f}</td>

<td style="padding:

12px;">{(exergy_recuperada_anual*4):,.2f}</td>

<td style="padding:

12px;">{(exergy_recuperada_anual*5):,.2f}</td>
</tr>
<tr style="border-bottom: 1px solid #222222; color: #4ade80;
background-color: #0d1410;">

<td style="padding: 12px; font-weight: bold;">Índice de

Inmunidad del Oikos ($S_e$)</td>

<td style="padding: 12px;">{soberania_exergetica:.2f}%</td>
<td style="padding: 12px;">{min(100.0,

soberania_exergetica*1.05):.2f}%</td>

<td style="padding: 12px;">{min(100.0,

soberania_exergetica*1.10):.2f}%</td>

<td style="padding: 12px;">{min(100.0,

soberania_exergetica*1.15):.2f}%</td>

<td style="padding: 12px;">{min(100.0,

soberania_exergetica*1.20):.2f}%</td>
</tr>
</table>

"""
st.markdown(html_table, unsafe_allow_html=True)
# ==========================================
# SISTEMA 3: ARBITRAJE DE INMUNIDAD OPERATIVA
# ==========================================
st.markdown("---")
st.header("⚙️ SISTEMA 3: Arbitraje de Inmunidad Operativa")
ac1, ac2, ac3 = st.columns(3)
if foco_metabolico == "Riesgo Regulatorio y Compliance (Motor de
Fragilidad)":
l_maint, l_assets = "️ Vectorización NLP / Automatización (%):",
"📈 Fondo Jurídico Indexado (%):"
elif foco_metabolico == "Logística y Suministros (Termodinámica
Comercial)":
l_maint, l_assets = "️ Blindaje de Rutas e Infraestructura (%):",
"📈 Activos Fijos (%):"
elif foco_metabolico == "Coherencia de Carteras y Activos (Matriz
Exergética Financiera)":
l_maint, l_assets = "️ Cobertura contra Colas Pesadas (%):", "📈
Recalibración Estocástica (%):"
else:
l_maint, l_assets = "️ Mantenimiento de Capital Fijo (%):", "📈
Reserva de Activos Reales (%):"
l_slack = "️ Holgura / Amortiguación Homeostática (%):"
with ac1: r_maint = st.slider(l_maint, min_value=5, max_value=40,
value=15, step=1)
with ac2: r_assets = st.slider(l_assets, min_value=5, max_value=40,
value=15, step=1)
with ac3: r_slack = st.slider(l_slack, min_value=0, max_value=20,
value=10, step=1)
res_total = r_maint + r_assets + r_slack
salida_libre = 100 - res_total
if res_total > 90 or res_total < 10:
st.error(f"⚠️ CONFIGURACIÓN INVIABLE: La reserva consolidada rompe
las fronteras de absorción del Sistema 3.")
else:
nivel_sancion = 0
motivo_sancion = "Coherencia algorítmica alineada con las reglas
comunes de protección recíproca."
if eficiencia_real < 75.0 and res_total < 35:

nivel_sancion = 1
motivo_sancion = "Sanción Graduada G1: Confiscación automática

del 15% de Viabilidad Libre para reyección de capital."
if r_maint == 5 or r_assets == 5:
nivel_sancion = 2
motivo_sancion = "Sanción Coercitiva G2: Veto algorítmico
activo por desprotección del fondo común. Escritura bloqueada."
p_maint = r_maint + 15.0 if nivel_sancion == 1 else r_maint
p_salida = max(0.0, salida_libre - 15.0) if nivel_sancion == 1
else (0.0 if nivel_sancion == 2 else salida_libre)
st.subheader("📊 Distribución de Potencia Activa Final")
def estilo_noire_puro(p, min_o, max_o, veto=False):
if veto: return "background-color: #2a0a0a; color: #ff5555;

border: 1px dashed #ff0000;"

if p < min_o: return "background-color: #1a0808; color:

#ff6b6b; border: 1px solid #500;"

elif p <= max_o: return "background-color: #0c140e; color:

#4ade80; border: 1px solid #14532d;"

else: return "background-color: #1c180c; color: #facc15;

border: 1px solid #713f12;"
e_m = estilo_noire_puro(p_maint, 15, 30, veto=(nivel_sancion ==
1))
e_a = estilo_noire_puro(r_assets, 15, 30)
e_s = estilo_noire_puro(r_slack, 5, 15)
e_o = "background-color: #111; color: #fff; border: 1px solid
#333;" if nivel_sancion < 2 else "background-color: #3a0000; color:
#ff0000; border: 2px solid #ff0000;"
dc1, dc2, dc3, dc4 = st.columns(4)
t1 = "NLP Regulatorio" if foco_metabolico == "Riesgo Regulatorio y
Compliance (Motor de Fragilidad)" else ("Blindaje Rutas" if
foco_metabolico == "Logística y Suministros (Termodinámica Comercial)"
else ("Blindaje Portafolio" if foco_metabolico == "Coherencia de
Carteras y Activos (Matriz Exergética Financiera)" else
"Mantenimiento"))
t2 = "Fondo Indexado" if foco_metabolico == "Riesgo Regulatorio y
Compliance (Motor de Fragilidad)" else "Reserva Activos"
t3 = "Cobertura GAFI" if foco_metabolico == "Riesgo Regulatorio y
Compliance (Motor de Fragilidad)" else "Holgura Operativa"
t4 = "Viabilidad Libre" if foco_metabolico == "Riesgo Regulatorio
y Compliance (Motor de Fragilidad)" else "Salida Útil Real"
for col, t, val, est in zip([dc1, dc2, dc3, dc4], [t1, t2, t3,
t4], [excedente_neto*(p_maint/100), excedente_neto*(r_assets/100),

excedente_neto*(r_slack/100), excedente_neto*(p_salida/100)], [e_m,
e_a, e_s, e_o]):
with col:
st.markdown(f"""<div style="{est} padding: 25px;

border-radius: 4px; text-align: center;">

<h4 style='margin: 0; text-transform: uppercase;
font-size: 11px; letter-spacing: 2px; opacity: 0.7;'>{t}</h4>
<p style='font-size: 24px; font-family: monospace;

font-weight: bold; margin: 15px 0;'>{val:,.2f} W</p>
</div>""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
if nivel_sancion == 0: st.info(f"⚖️ **Auditoría de Control:**
{motivo_sancion}")
elif nivel_sancion == 1: st.warning(f"⚖️ **Auditoría de Control:**
{motivo_sancion}")
else: st.error(f"⚖️ **️ AUDITORÍA COERCITIVA ACTIVA:**
{motivo_sancion}")
if st.button("💾 Sellar Matriz Exergética en la Memoria del
Lógos"):

if nivel_sancion == 2: st.error("Operación bloqueada por el

Sistema 3.")

elif db_disponible:
try:
cursor.execute("INSERT INTO exergy_history (foco,

e_in, i_destroyed, efficiency) VALUES (%s, %s, %s, %s);",
(foco_metabolico, e_in_real, i_destroyed, eficiencia_real))

conn.commit()
st.success(f"Registro sellado inmutablemente para el

nodo {nodo_id}.")

except Exception as err: st.error(f"Falla de grabación:

{err}")

else: st.warning("Memoria local activa únicamente.")

# ==========================================
# SISTEMA 5: REGISTRO PSICOHISTÓRICO (HISTORIAL UPR)
# ==========================================
st.markdown("---")
st.header("📡 SISTEMA 5: Registro Psicohistórico de la UPR")
st.markdown("*Evolución temporal del vector de regeneración exergética
frente a la disipación del entorno*")
if db_disponible:
try:
cursor.execute("SELECT timestamp, (e_in - i_destroyed) as
upr_net FROM exergy_history WHERE foco = %s ORDER BY timestamp ASC;",
(foco_metabolico,))

rows = cursor.fetchall()
if rows:
import pandas as pd
chart_data = pd.DataFrame({
'Potencia UPR Neto (W-Neg)': [max(0.0, r[1]) for r in

rows]

}, index=[r[0].strftime("%m-%d %H:%M") for r in rows])
st.line_chart(chart_data)
else:
st.info("A la espera de registros almacenados en el Lógos

para trazar la línea evolutiva de la UPR.")
except Exception as graph_err:
st.sidebar.error(f"Fricción en el trazado psicohistórico:

{graph_err}")
st.sidebar.markdown("---")
if not db_disponible: st.sidebar.warning("📡 Modo Autónomo Localizado
Activo.")
else: st.sidebar.success("📡 Conexión síncrona con el Lógos central
activa.")
