import streamlit as st

st.set_page_config(
    page_title="Flas Analista - Previa Inteligente", page_icon="⚽"
)

st.title("⚽ Flas Analista | Previa y Jugadas Clave")
st.markdown("### Sube tu captura y procesa tu análisis pre-partido")

# Botón para subir la foto/captura de pantalla (alineación, estadísticas, etc.)
uploaded_file = st.file_uploader(
    "📷 Sube aquí la captura de pantalla (Alineación, Estadísticas o BetPlay)",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:
  st.image(
      uploaded_file, caption="Captura cargada para referencia", use_container_width=True
  )
  st.success("¡Imagen cargada con éxito! Ya puedes revisar los datos abajo.")

with st.form("prematch_form"):
  st.subheader("1. Datos del Partido")
  local = st.text_input("Equipo Local", "Ej: Equipo Local")
  visitante = st.text_input("Equipo Visitante", "Ej: Equipo Visitante")

  st.subheader("2. Métricas Clave de la Previa")
  col1, col2 = st.columns(2)

  with col1:
    prom_corners = st.number_input(
        "Promedio Proyectado de Córners", min_value=0.0, value=9.5
    )
    arbitro_tarj = st.selectbox(
        "Perfil del Árbitro",
        [
            "Riguroso (Saca muchas tarjetas / pita faltas)",
            "Permisivo (Deja jugar)",
        ],
    )

  with col2:
    jugador_clave = st.text_input(
        "Jugador Clave (Extremo o Volante)", "Ej: Delantero o Volante marca"
    )
    tendencia_faltas = st.slider(
        "Intensidad de Faltas Esperada (1 a 10)", 1, 10, 7
    )

  submitted = st.form_submit_button("Procesar Jugada Clave 🚀")

if submitted:
  st.success("¡Análisis previo procesado con éxito!")
  st.markdown("### 🎯 Jugadas Recomendadas para la Previa:")

  if prom_corners >= 9.0:
    st.markdown(
        f"- **Córners:** Alta proyección ofensiva. Apuntar al **Más de 8.5 o"
        f" 9.5 córners** entre **{local}** y **{visitante}**."
    )
  else:
    st.markdown(
        f"- **Córners:** Partido cerrado por las bandas. Considerar líneas"
        f" bajas de tiros de esquina."
    )

  if "Riguroso" in arbitro_tarj or tendencia_faltas >= 6:
    st.markdown(
        f"- **Faltas y Duelos:** Con un árbitro estricto y alta intensidad,"
        f" vigilar las estadísticas individuales de faltas cometidas o"
        f" recibidas por **{jugador_clave}**."
    )
  else:
    st.markdown(
        f"- **Faltas y Duelos:** Encuentro fluido. Menos margen para"
        f" mercados pesados de faltas."
    )

  st.info(
      "💡 *Tip:* Usa la imagen que subiste arriba para contrastar los datos y"
      " arma tu jugada en BetPlay."
  )
