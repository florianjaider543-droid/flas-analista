
import streamlit as st

st.set_page_config(page_title="Flas Analista - En Vivo", page_icon="⚽", layout="wide")

st.title("⚽ Flas Analista | Panel Táctico en Directo")
st.markdown("---")

# Barra lateral para configurar el partido
st.sidebar.header("⚙️ Configuración del Partido")
equipo_local = st.sidebar.text_input("Equipo Local", "Local")
equipo_visitante = st.sidebar.text_input("Equipo Visitante", "Visitante")
minuto_actual = st.sidebar.slider("Minuto del Partido", 0, 90, 1)

st.subheader(f"📊 {equipo_local} vs {equipo_visitante} (Minuto {minuto_actual}')")

# Métricas rápidas en columnas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Córners Totales", value="0", delta="Tendencia Alta")
with col2:
    st.metric(label="Faltas Acumuladas", value="0", delta="Árbitro Tarjetero")
with col3:
    st.metric(label="Remates a Puerta", value="0")
with col4:
    st.metric(label="Presión Alta", value="Media")

st.markdown("---")
st.text("💡 Escribe aquí abajo tu lectura en caliente o notas del jugador clave:")
nota_en_vivo = st.text_area("Observación táctica:")

if st.button("Guardar / Actualizar Análisis"):
    st.success("¡Datos actualizados con éxito en el sistema!")
              
