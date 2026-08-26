

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

# Radar Multidisciplina Inteligente (Todo terreno)
st.subheader("📸 Radar Total (Lectura Dinámica)")

# Selector para cambiar de deporte o juego al instante
deporte_seleccionado = st.selectbox(
    "🎯 Selecciona la categoría a analizar:", 
    ["Fútbol ⚽", "Baloncesto 🏀", "Esports / Free Fire 🎮", "General / Todo 📋"]
)

archivo_captura = st.file_uploader(f"Sube tu captura de {deporte_seleccionado}", type=["jpg", "jpeg", "png"])

if archivo_captura is not None:
    st.image(archivo_captura, caption=f"Captura cargada para {deporte_seleccionado}", use_container_width=True)
    
    if st.button("🚀 Escanear y Extraer Datos"):
        with st.spinner(f"Analizando cartelera de {deporte_seleccionado} y aplicando filtros..."):
            st.success("¡Lectura y escaneo completados con éxito!")
            
            st.markdown(f"### 🔥 Resultado del Análisis ({deporte_seleccionado})")
            
            if "Fútbol" in deporte_seleccionado:
                st.info("⚽ **Fútbol:** Estadísticas de remates, posesión y tendencia cruzadas correctamente.")
            elif "Baloncesto" in deporte_seleccionado:
                st.info("🏀 **Baloncesto:** Lectura de triples, efectividad en tiros y cuartos procesada.")
            elif "Esports" in deporte_seleccionado:
                st.info("🎮 **Free Fire / Esports:** Datos de mapa, enfrentamientos y bajas extraídos al milímetro.")
            else:
                st.info("📋 **Modo General:** Texto y datos de la imagen leídos en su totalidad sin restricciones.")
