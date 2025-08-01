import streamlit as st
import random

st.set_page_config(page_title="Quiz de cumpleaños", page_icon="🎉")

# Inicializar estados
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0
if "puntos" not in st.session_state:
    st.session_state.puntos = 0
if "mostrar_reaccion" not in st.session_state:
    st.session_state.mostrar_reaccion = False
if "respuesta" not in st.session_state:
    st.session_state.respuesta = None
if "mostrar_dado" not in st.session_state:
    st.session_state.mostrar_dado = False
if "dado_resultado" not in st.session_state:
    st.session_state.dado_resultado = 0
if "mostrar_resultado" not in st.session_state:
    st.session_state.mostrar_resultado = False
if "empezar_quiz" not in st.session_state:
    st.session_state.empezar_quiz = False
if "corazon_jugado" not in st.session_state:
    st.session_state.corazon_jugado = False
if "emoji_jugado" not in st.session_state:
    st.session_state.emoji_jugado = False
if "reaccion_minijuego" not in st.session_state:
    st.session_state.reaccion_minijuego = None
if "esperar_siguiente_minijuego" not in st.session_state:
    st.session_state.esperar_siguiente_minijuego = False

st.title("🎂 Quiz de cumpleaños")
st.markdown("#### Hola gordi\n Antes de empezar me gustaría desearte un maravilloso cumple rodeado de quienes más te quieren. Me pone triste un año más no poder pasar ese día juntos. Eres una persona muy especial para mi que merece recibir su regalito de forma también especial.\nEs por eso que te he preparado un Quiz/juego para adaptarnos perfectamente a algún plan chulito del cúal los gastos corren a mi cuenta. Es algo sencillito así que presta mucha atención.")
st.markdown("**Reglas del juego:** Responde con sinceridad: He modificado TODO el código para que haya tres posibles y persuasivos resultados.\n El Quiz constará de 8 preguntas, algunas nos ayudará a elegir regalo y otras me harán cuestionarme la relación (o no).\n Cada pregunta sobre el viaje suma un nº determinado de puntos.\n Las preguntas de valoración amorosa pueden restar puntos (yo que tú respondería bien...)\n. Además, he añadido un par de minujuegos/preguntas chorras para hacerlo más interactivo (estas también suman o restan puntos).\n La suma total de puntos elegirá nuestro destino.\n Antes de ver el resultado se lanzará un dado que podrá cambiar todo...\n ¿Estás listo? jjj ¡SUERTE!")

if not st.session_state.empezar_quiz:
    if st.button("😎 Empezar quiz"):
        st.session_state.empezar_quiz = True
        st.rerun()
    st.stop()

preguntas = [
    {
        "Continuemos": "\nPREGUNTA SOBRE EL REGALO:\n Venga dialoguemos, ¿cuándo te viene bien?",
        "opciones": {
            "a": ("Me da absolutamente igual", 1, "Vaya decepción... qué flexibilidad tan poco emocionante y que poca iniciativa churri...: +1 pt."),
            "b": ("Durante el cuatri", 3, "Venga va, lo organizamos en cuanto empiecen las clases: +3 pts."),
            "c": ("Podemos meditarlo", 5, "Bueno, vamos fluyendo, oki: +5 pts.")
        }
    },
    {
        "Continuemos": "\nVALORACIÓN AMOROSA:\n ¿Quién es la mujer más guapa del mundo? (esta pregunta puede restar puntos...)",
        "opciones": {
            "a": ("Vaya pregunta, Aitana", -1, "Velada VI: Pablo vs Plex; Aitana vs Paula: -1 pt."),
            "b": ("La alegría de mi existir, la razón de mis latidos y el motivo de mi felicidad: MI NOVIA", 3, "Muy bien mi niño: +3 pts."),
            "c": ("No sé pero mi novia no es", -1, "Hoy por lo que sea no dormimos juntos, ¿te parece?: -1 pt.")
        }
    },
    {
        "Continuemos": "\nPREGUNTA SOBRE EL REGALO:\n ⏳Sigamos, ¿cuánto te gustaría alargar tu regalo?",
        "opciones": {
            "a": ("Vamos a relajarnos un findesito", 5, "😌 Findesito pa' los dos, me gusta como piensas: +5 pts."),
            "b": ("Con un día me basta", 1, "⏱️ Exprimiendo el tiempo al máximo eeeee: +1 pt."),
            "c": ("Una noche me es suficiente", 3, "🌙 Bueeeeno espero que te sea suficiente: +3 pts.")
        }
    },
    {
        "Continuemos": "\nVALORACIÓN AMORORSA:\n ¿Cuál es mi desayuno ideal?",
        "opciones": {
            "a": ("Chocolate con churros", -2, "😔 Madre mía, lo voy a omitir: -2 pts."),
            "b": ("Cola-Cao con tostaditas", -1, "Vaya patinazo colega...🥲: -1 pt."),
            "c": ("Tostaditas con zumo de naranja", 2, "Como le sabe mi niño jjjj🥰: +2 pts.")
        }
    },
    {
        "Continuemos": "\nPREGUNTA SOBRE EL REGALO:\n Volviendo al tema principal, ¿qué te gustaría hacer?",
        "opciones": {
            "a": ("Quiero andar mucho, me siento enérgico", 1, "Aventurero total joe, ¡prepara las deportivas y ropa cómoda!: +1 pt."),
            "b": ("Me apetece tranquilidad y buena comida", 3, "🍝 Comida rica y relax, ¡planazo!: +3 pts."),
            "c": ("Un poquito de todo", 5, "😏Equilibrio perfecto, ¡me gusta como piensas!: +5 pts.")
        }
    },
    {
        "Continuemos": "\nVALORACIÓN AMOROSA:\n A ver dime, ¿cuánto me quieres?",
        "opciones": {
            "a": ("No mucho últimamente...", -1, "Ya lo he notado ya...dejamos el regalo aquí entonces, ¿no?: -1 pt."),
            "b": ("Mucho mucho", 3, "Bueeeeeno valeeeeee: +3 pts."),
            "c": ("Yo me casaba mañana mismo mi vida", 5, "No tienes miedo al éxito entonces 😏: +5 pts.")
        }
    },
    {
        "Continuemos": "\nPREGUNTA SOBRE EL REGALO:\n Hablemos ahora de distancia, ¿qué tan lejos quieres ir?",
        "opciones": {
            "a": ("Me vale con algo cerquita", 2, "Vaya sedentario estás colega 🤧: +2 pts."),
            "b": ("Algún sitio guay por Andalucía", 4, "Mmmm me lo apunto 📝: +4 pts."),
            "c": ("¡Cuanto más lejos mejor!", 5, "✈️ Vale vale, veré que puedo hacer: +5 pts")
        }
    },
    {
        "Continuemos": "\nPREGUNTA FINAL:\n 🎉 ¿Qué esperas del plan?",
        "opciones": {
            "a": ("Relajarnos y desconectar", 1, "¿Quizás te gustaría conectar con la naturaleza?: +1 pt."),
            "b": ("Visitar cosas nuevas juntitos", 3, "Me encanta la idea jjjj: +3 pts."),
            "c": ("Quiero un poquito de ambas cosas", 5, "Yeah, lo mejor de los dos mundos 🥡: +5 pts.")
        }
    }
]

total_preguntas = len(preguntas)
indice = st.session_state.pregunta_actual

# Minijuego 1: Emoji relación
if indice == 4 and not st.session_state.corazon_jugado:
    st.markdown("### BONUS")
    st.write("Escoge la serie de emojis que más represente nuestra relación")

    if not st.session_state.esperar_siguiente_minijuego:
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("😎😍🤣😡"):
                st.session_state.puntos += 2
                st.session_state.reaccion_minijuego = "Una montaña rusa maravillosa: +2 pts. extras"
                st.session_state.esperar_siguiente_minijuego = True
        with col2:
            if st.button("😣🙄👿🤧"):
                st.session_state.reaccion_minijuego = "Estoy hablando de nuestra relación, no de la otra que tienes: -1 pt. extra"
                st.session_state.esperar_siguiente_minijuego = True
        with col3:
            if st.button("😭🧑🏽‍❤️‍💋‍👩🏼🫎🤘🏼"):
                st.session_state.puntos -= 1
                st.session_state.reaccion_minijuego = "¿En serio Pablo?: -1 pt. extra"
                st.session_state.esperar_siguiente_minijuego = True

    if st.session_state.esperar_siguiente_minijuego:
        st.info(st.session_state.reaccion_minijuego)
        if st.button("👉 Siguiente"):
            st.session_state.corazon_jugado = True
            st.session_state.esperar_siguiente_minijuego = False
            st.session_state.reaccion_minijuego = None
            st.rerun()
    st.stop()

# Minijuego 2: Emoji premio
if indice == 6 and not st.session_state.emoji_jugado:
    st.markdown("### 🎁 Elige el emoji ganador")
    st.write("Tres emojis, dos esconde un regalito extra, el otro un castigo jjjj. ¡Suerte!")

    if not st.session_state.esperar_siguiente_minijuego:
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🍔"):
                st.session_state.puntos += 1
                st.session_state.reaccion_minijuego = "¡PREMIO! Has ganado un cupón canjeable para hacerte cosquillas en la espalda: +1 pt."
                st.session_state.esperar_siguiente_minijuego = True
        with col2:
            if st.button("🍕"):
                st.session_state.reaccion_minijuego = "¡CASTIGO! Tienes que hacerle cosquillas en la espalda a tu novia las veces que te lo pida en las próximas 24 horas: no sumas puntos."
                st.session_state.esperar_siguiente_minijuego = True
        with col3:
            if st.button("🍪"):
                st.session_state.puntos += 1
                st.session_state.reaccion_minijuego = "¡PREMIO! Ponte guapito cuando volvamos a sevilla que invito a cenar: +1 pt."
                st.session_state.esperar_siguiente_minijuego = True

    if st.session_state.esperar_siguiente_minijuego:
        st.info(st.session_state.reaccion_minijuego)
        if st.button("👉 Siguiente"):
            st.session_state.emoji_jugado = True
            st.session_state.esperar_siguiente_minijuego = False
            st.session_state.reaccion_minijuego = None
            st.rerun()
    st.stop()

# Preguntas normales
if indice < total_preguntas:
    pregunta = preguntas[indice]
    st.markdown(f"### {pregunta['Continuemos']}")

    for clave, (texto, valor, reaccion) in pregunta['opciones'].items():
        if st.button(f"{clave.upper()}) {texto}", key=f"{indice}-{clave}"):
            st.session_state.puntos += valor
            st.session_state.respuesta = reaccion
            st.session_state.mostrar_reaccion = True

    if st.session_state.mostrar_reaccion and st.session_state.respuesta:
        st.info(st.session_state.respuesta)
        if st.button("👉 Siguiente"):
            st.session_state.pregunta_actual += 1
            st.session_state.mostrar_reaccion = False
            st.session_state.respuesta = None
            st.rerun()

else:
    # Lanzar dado final
    if not st.session_state.mostrar_dado:
        st.markdown("### 🎲 BONUS: El dado del destino")
        st.write("Lanza el dado y veamos si modifica el resultado. Si sacas un 6 se suman +2 puntos.")
        if st.button("Lanzar el dado"):
            resultado = random.randint(1, 6)
            st.session_state.dado_resultado = resultado
            st.session_state.puntos += 2 if resultado == 6 else 0
            st.session_state.mostrar_dado = True
            st.rerun()
    else:
        st.write(f"Has lanzado un {st.session_state.dado_resultado} 🎲")
        if st.session_state.dado_resultado == 6:
            st.success("💥 ¡Suerte total! +2 puntos extra.")
        else:
            st.write("Bueeeno, no se suma nada, eso significa que tu regalo no se ha obtenido al azar jjj.")

        st.markdown("""
        ###  **POSIBLES REGALOS**
        - 🌿 Una ruta de senderismo por Doñana  (1-15 PUNTOS)
        - 🏰 Un finde romántico en Granada      (11-25 PUNTOS)
        - 😎 Un viaje maravilloso a Lisboa      (26-Inf PUNTOS)
        """)

        if not st.session_state.mostrar_resultado:
            if st.button("✨ Descubrir sorpresa ✨"):
                st.session_state.mostrar_resultado = True
                st.rerun()
        else:
            st.markdown("## 🎉 Resultado final")
            puntos = st.session_state.puntos
            st.write(f"Has obtenido **{puntos} puntos**.")

            if puntos <= 10:
                regalo = "NOS VAMOS EN BUSCA DEL LINCE IBÉRICO Y LOS CORRELIMOS"
            elif puntos <= 20:
                regalo = "¡¡¡¡¡NOS VAMOS A GRANADAAAAA!!!!!"
            else:
                regalo = "¡¡¡¡¡PREPARA LAS MALETAS QUE NOS VAMOS A LISBOA!!!!"

            st.success(f" ¡Tu regalo sorpresa es: {regalo}!")

            st.markdown("""
            ---
            ### 💌 Notita final:
            Este quiz es solo una excusa para hacerlo más divertido y tratar de sacarte una sonrisilla.  
            Gracias por todo el amor que me das y por darme el gustazo de compartir la vida contigo.  
            **Te quiero muchísimo guapito mío**
            """)

            if st.button("🔄 Volver a empezar"):
                for key in st.session_state.keys():
                    del st.session_state[key]
                st.rerun()
