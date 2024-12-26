import streamlit as st
from gtts import gTTS
import tempfile

# Diccionario con palabras a traducir
diccionario = {
    'a': 'uno ',
    'b': 'dos ',
    'c': 'tres ',
    'd': 'cuatro ',
    'e': 'cinco ',
    'f': 'seis ',
    'g': 'siete ',
    'mi': 'ri ',
    'tuyo': 'tu ',
    'mío': 'mi ',
}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = []
    palabras_clave_presentes = [ 'mi' ]

    for palabra in palabras:
        palabra_lower = palabra.lower()
        if palabra_lower in diccionario:
            oracion_traducida.append(diccionario[palabra_lower])
            palabras_clave_presentes.append(palabra_lower)
        else:
            oracion_traducida.append(palabra)

    # Si hay alguna de las palabras clave, las movemos al segundo lugar
    if palabras_clave_presentes:
        # Eliminamos las palabras clave de su posición actual
        for palabra_clave in palabras_clave_presentes:
            oracion_traducida.remove(diccionario[palabra_clave])

        # Insertamos las palabras clave en segundo lugar
        for palabra_clave in palabras_clave_presentes:
            oracion_traducida.insert(1, diccionario[palabra_clave])

    return " ".join(oracion_traducida).strip()

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




