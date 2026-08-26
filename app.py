import streamlit as st

st.set_page_config(
    page_title="Flas Analista - Motor Maestro", page_icon="⚽", layout="centered"
)

st.title("⚽ Flas Analista | Motor Matemático de Apuestas")
st.markdown(
    "### Centro de Cálculo Táctico (Córners, Faltas y Estadísticas de Jugador)"
)

with st.form("motor_maestro_form"):
  st.subheader("1. Datos del Encuentro")
  col_1, col_2 = st.columns(2)
  with col_1:
    local = st.text_input("Equipo Local", value="", placeholder="Ej. Millonarios")
  with col_2:
    visitante = (
        format_vis := st.text_input(
            "Equipo Visitante", value="", placeholder="Ej. Santa Fe"
        )
    )

  st.subheader("2. Estadísticas y Métricas Clave")
  col_3, col_4 = st.columns(2)
  with col_3:
    prom_corners = st.number_input(
        "Promedio / Línea de Córners",
        min_value=0.0,
        max_value=20.0,
        value=9.5,
        step=0.5,
    )
    factor_arbitro = st.selectbox(
        "Perfil y Rigor del Árbitro",
        [
            (
                "Muy Tarjetero / Pita todo (Factor Alto 1.4)",
                1.4,
            ),
            (
                "Neutral / Estándar (Factor Normal 1.0)",
                1.0,
            ),
            (
                "Permisivo / Deja jugar (Factor Bajo 0.7)",
                0.7,
            ),
        ],
        format_func=lambda x: x[0],
    )
  with col_4:
    jugador = st.text_input(
        "Jugador Clave (Extremo / Volante)",
        value="",
        placeholder="Ej. Daniel Ruiz",
    )
    faltas_jugador = st.number_input(
        "Promedio de Faltas Cometidas/Recibidas del Jugador",
        min_value=0.0,
        max_value=10.0,
        value=2.0,
        step=0.5,
    )

  submitted = st.form_submit_button("Calcular Jugada Maestra 🚀")

if submitted:
  # Limpieza de variables
  eq_l = local.strip() if local.strip() else "Equipo Local"
  eq_v = visitante.strip() if visitante.strip() else "Equipo Visitante"
  j_clv = jugador.strip() if jugador.strip() else "Jugador Clave"
  arbt_val = factor_arbitro[1]

  st.success(f"¡Cálculo matemático completado para {eq_l} vs {eq_v}!")
  st.markdown("---")
  st.markdown(f"### 🎯 JUGADA MAESTRA | {eq_l} vs {eq_v}")

  # --- CÁLCULO MATEMÁTICO DE CÓRNERS ---
  if prom_corners >= 9.5:
    linea_corner_sugerida = prom_corners - 1.0
    analisis_corner = (
        f"Alta presión en carriles externos. El promedio proyectado de"
        f" **{prom_corners} córners** respalda entrarle al mercado de **Más de"
        f" {linea_corner_sugerida} Tiros de Esquina**."
    )
  elif prom_corners >= 8.0:
    linea_corner_sugerida = prom_corners - 1.0
    analisis_corner = (
        f"Flujo de juego equilibrado en bandas. Se recomienda una línea"
        f" prudente de **Más de {linea_corner_sugerida} Córners** para asegurar"
        f" cuota en BetPlay."
    )
  else:
    analisis_corner = (
        f"Bloque defensivo cerrado y poca profundidad por costados ({prom_corners}"
        f" proyectados). Se aconseja **evitar** mercados altos de córners o"
        f" buscar un 'Menos'."
    )

  st.markdown(f"* **Análisis de Córners:** {analisis_corner}")

  # --- CÁLCULO MATEMÁTICO DE FALTAS Y JUGADOR ---
  indice_riesgo_faltas = round(faltas_jugador * arbt_val, 2)

  if indice_riesgo_faltas >= 2.5:
    analisis_faltas = (
        f"Índice de fricción alto ({indice_riesgo_faltas} calculado). Con el"
        f" promedio de **{j_clv}** ({faltas_jugador}) cruzado con el carácter"
        f" del juez, la jugada clave es ir por **Más de 1.5 faltas /"
        f" amonestación** de este jugador."
    )
  else:
    analisis_faltas = (
        f"Índice de fricción moderado/bajo ({indice_riesgo_faltas} calculado)."
        f" El contexto favorece que **{j_clv}** se centre en generación y"
        f" remates directos al arco en lugar de acumular infracciones."
    )

  st.markdown(
      f"* **Análisis Individual ({j_clv}):** {analisis_faltas}"
  )

  # --- CONSTRUCCIÓN DE LA COMBINADA / JUGADA MAESTRA FINAL ---
  st.markdown("---")
  st.subheader("🔥 Selección Combinada para BetPlay:")

  if prom_corners >= 9.5 and indice_riesgo_faltas >= 2.5:
    apuesta_final = (
        f"**Combinada Sugerida:** Más de {prom_corners - 1.5} córners en el"
        f" partido + {j_clv} registra 2 o más acciones de falta/duelos"
        f" disputados."
    )
  elif prom_corners >= 8.0:
    apuesta_final = (
        f"**Selección Simple Directa:** Más de {prom_corners - 1.0} tiros de"
        f" esquina totales para {eq_l} y {eq_v}."
    )
  else:
    apuesta_final = (
        f"**Selección Táctica:** Partido cerrado. Buscar líneas asiáticas"
        f" reducidas o mercado de remates a puerta de {j_clv}."
    )

  st.info(apuesta_final)
