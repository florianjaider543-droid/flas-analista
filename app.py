import streamlit as st

st.set_page_config(
    page_title="Flas Analista - Centro Táctico",
    page_icon="⚽",
    layout="centered",
)

st.title("⚽ Flas Analista | Motor Previa & Apuestas")
st.markdown("### Centro de Inteligencia Táctica (Córners, Faltas y Jugadores)")

# Formulario principal con campos vacíos para evitar errores en móviles
with st.form("analisis_form"):
  st.subheader("1. Configuración del Encuentro")
  col_t1, col_t2 = st.columns(2)
  with col_t1:
    local = st.text_input("Equipo Local", value="", placeholder="Ej. Junior")
  with col_t2:
    visitante = st.text_input(
        "Equipo Visitante", value="", placeholder="Ej. América"
    )

  st.subheader("2. Carga de Referencia (Opcional)")
  uploaded_file = st.file_uploader(
      "Sube captura de alineación o cuotas (BetPlay)",
      type=["jpg", "jpeg", "png"],
  )

  st.subheader("3. Variables Estadísticas y Arbitraje")
  col_m1, col_m2 = st.columns(2)
  with col_m1:
    prom_corners = st.number_input(
        "Línea / Promedio Córners",
        min_value=0.0,
        max_value=20.0,
        value=9.5,
        step=0.5,
    )
    arbitro = st.selectbox(
        "Perfil del Árbitro",
        [
            "Estricto / Tarjetero (Alto registro de faltas)",
            "Permisivo / Deja jugar (Bajo roce)",
        ],
    )
  with col_m2:
    jugador = st.text_input(
        "Jugador Clave", value="", placeholder="Ej. Carlos Bacca"
    )
    intensidad = st.slider("Intensidad de Faltas (1 a 10)", 1, 10, 7)

  submitted = st.form_submit_button("Analizar y Generar Jugada 🚀")

# Mostrar imagen si el usuario la sube
if uploaded_file is not None:
  st.image(uploaded_file, caption="Referencia cargada", use_container_width=True)

# Procesamiento dinámico al enviar el formulario
if submitted:
  # Si dejan los campos vacíos, usa un texto genérico para evitar errores feos
  eq_local = local if local.strip() != "" else "Local"
  eq_vis = visitante if visitante.strip() != "" else "Visitante"
  jug_clave = jugador if jugador.strip() != "" else "el jugador clave"

  st.success(f"¡Análisis generado con éxito para {eq_local} vs {eq_vis}!")
  st.markdown("---")
  st.markdown(f"### 🎯 Reporte de Jugadas Clave: {eq_local} vs {eq_vis}")

  # Lógica 100% dinámica para Córners
  if prom_corners >= 9.5:
    c_msg = (
        f"Alta tendencia proyectada por bandas entre {eq_local} y {eq_vis}."
        f" Considerar mercado de **Más de {prom_corners - 1.0} córners**."
    )
  elif prom_corners >= 8.0:
    c_msg = (
        f"Dinámica moderada en costados para este {eq_local} vs {eq_vis}."
        f" Apuntar a una línea prudente de **Más de {prom_corners - 1.5}"
        f" córners**."
    )
  else:
    c_msg = (
        f"Encuentro trabado en zona medular entre {eq_local} y {eq_vis}. Se"
        f" sugiere evitar líneas altas de tiros de esquina."
    )

  st.markdown(f"* **Mercado de Córners ({prom_corners} proj.):** {c_msg}")

  # Lógica para Faltas y Jugadores
  if "Estricto" in arbitro or intensidad >= 7:
    f_msg = (
        f"Con un juez de perfil estricto y una intensidad calculada de"
        f" {intensidad}/10, hay que vigilar de cerca las infracciones y duelos"
        f" individuales de **{jug_clave}**."
    )
  else:
    f_msg = (
        f"Escenario de menor fricción táctica. El impacto de faltas sobre"
        f" **{jug_clave}** baja; enfocar la atención en sus estadísticas"
        f" directas de remates al arco."
    )

  st.markdown(f"* **Faltas y Duelos Individuales:** {f_msg}")

  st.markdown("---")
  st.info(
      "💡 **Nota Táctica:** Contasta este bloque dinámico con tu lectura de"
      " BetPlay y deja lista tu jugada antes del pitazo inicial."
  )
