

import streamlit as st

st.set_page_config(page_title="Flas Analista", page_icon="⚽", layout="centered")

st.title("⚽ Flas Analista - Panel Táctico")
st.write("Control en vivo para análisis y jugadas")

st.divider()

# Configuración del partido
st.subheader("📌 Partido en Curso")
local = st.text_input("Equipo Local", "Junior")
visitante = st.text_input("Equipo Visitante", "Rival")
minuto = st.slider("Minuto actual", 1, 90, 10)

st.divider()

# Estadísticas clave
st.subheader(f"📊 Estadísticas: {local} vs {visitante} (Min. {minuto}')")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"**{local}**")
    remates_l = st.number_input("Remates a puerta", 0, 30, 2, key="rl")
    corners_l = st.number_input("Córners", 0, 20, 1, key="cl")

with col2:
    st.markdown(f"**{visitante}**")
    remates_v = st.number_input("Remates a puerta", 0, 30, 1, key="rv")
    corners_v = st.number_input("Córners", 0, 20, 0, key="cv")

st.divider()

# Lectura rápida
st.subheader("💡 Lectura Táctica")
if remates_l > remates_v:
    st.success(f"**{local}** manda en campo rival y genera más peligro.")
elif remates_v > remates_l:
    st.warning(f"**{visitante}** es más punzante con menos llegadas.")
else:
    st.info("Partido parejo, bloque medio muy disputado.")
st.divider()

# Radar de Partidos
st.subheader("📸 Radar de Partidos")
archivo_captura = st.file_uploader("Sube tu captura de cartelera", type=["jpg", "jpeg", "png"])

if archivo_captura is not None:
    st.image(archivo_captura, caption="Captura cargada", use_container_width=True)
    
    if st.button("🚀 Buscar Jugada Maestra"):
        st.success("¡Análisis completado!")
        st.info("🔥 **Jugada Maestra:** [Equipo A] vs [Equipo B] - Más de 1.5 remates.")
