import streamlit as st
from gtts import gTTS
import tempfile

# Diccionario con palabras a traducir
diccionario = {
    # Agrega aquí tus traducciones
    # 'a': 'uno ',
    # 'b': 'dos ',
    # 'c': 'tres ',
    # 'd': 'cuatro ',
    # 'e': 'cinco ',
    # 'f': 'seis ',
    # 'g': 'siete ',
    # 'mi': 'ri ',
    # 'tuyo': 'tu ',
    # 'mío': 'mi ',
}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = " ".join([diccionario.get(palabra.lower(), palabra) for palabra in palabras])
    return oracion_traducida

def reproducir_audio(texto, lang):
    tts = gTTS(text=texto, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
        tts.save(tmp.name)
        with open(tmp.name, 'rb') as audio_file:
            audio_bytes = audio_file.read()
    return audio_bytes

st.title("Texto a Voz")

# Estado de la sesión para la traducción
if 'oracion_traducida' not in st.session_state:
    st.session_state.oracion_traducida = ""

# Opción para introducir texto
oracion_usuario = st.text_area("Introduce una oración (máx. 10 líneas):", height=200)

# Botón para ejecutar la traducción
if st.button("Traducir"):
    if oracion_usuario:
        oracion_traducida = traducir_oracion(oracion_usuario)
        st.session_state.oracion_traducida = oracion_traducida
        audio_bytes = reproducir_audio(oracion_traducida, 'es')  # Usando español por defecto
        st.audio(audio_bytes, format='audio/mp3')
    else:
        st.warning("Por favor, introduce una oración antes de traducir.")




