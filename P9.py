import streamlit as st
from gtts import gTTS
import tempfile

# Diccionario con palabras a traducir
diccionario = {
    'mi': 'correcta',
    'tu': 'excelente',
    'idea': 'idea',
    'dedo': '4',
    'espacio': '5',
    'fuego': '6',
    'guerra': '7',
}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = []
    palabras_a_mover = []

    for palabra in palabras:
        palabra_lower = palabra.lower()
        if palabra_lower in diccionario:
            # Añadimos la traducción y guardamos la palabra para mover
            oracion_traducida.append(diccionario[palabra_lower])
            palabras_a_mover.append(diccionario[palabra_lower])
        else:
            oracion_traducida.append(palabra)

    # Si hay palabras a mover, las reubicamos en la segunda posición
    if palabras_a_mover:
        # Eliminamos las palabras que se moverán
        for palabra in palabras_a_mover:
            oracion_traducida.remove(palabra)
        # Insertamos las palabras en la segunda posición
        for palabra in palabras_a_mover:
            oracion_traducida.insert(1, palabra)

    return " ".join(oracion_traducida)

def reproducir_audio(texto, lang):
    tts = gTTS(text=texto, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
        tts.save(tmp.name)
        with open(tmp.name, 'rb') as audio_file:
            audio_bytes = audio_file.read()
    return audio_bytes

st.title("Traductor de números")

# Estado de la sesión para la traducción
if 'oracion_traducida' not in st.session_state:
    st.session_state.oracion_traducida = ""

# Opción para introducir texto
oracion_usuario = st.text_input("Introduce una palabra:")

# Traducir la oración ingresada por el usuario
if oracion_usuario:
    oracion_traducida = traducir_oracion(oracion_usuario)
    st.session_state.oracion_traducida = oracion_traducida
    st.write(f"Traducción: {oracion_traducida}")
    audio_bytes = reproducir_audio(oracion_traducida, 'es')  # Usando español por defecto
    st.audio(audio_bytes, format='audio/mp3')









