
import streamlit as st
from gtts import gTTS
import tempfile

# Diccionario con palabras a traducir
diccionario = {
    'uno': '1uno',
    'dos': '2dos',
    'tres': '3tres',
    'cuatro': '4cuatro',
    'cinco': '5cinco',
}

# Lista para palabras personalizadas
palabras_personalizadas = [ 'uno', 'dos', 'tres']

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = []
    palabras_a_mover = []
    
    # Combina el diccionario con las palabras personalizadas
    diccionario_completo = {**diccionario}
    for palabra in palabras_personalizadas:
        diccionario_completo[palabra.lower()] = palabra.lower()  # Mantiene la palabra original

    for palabra in palabras:
        palabra_lower = palabra.lower()
        if palabra_lower in diccionario_completo:
            # Añadimos la traducción y guardamos la palabra para mover
            oracion_traducida.append(diccionario_completo[palabra_lower])
            palabras_a_mover.append(diccionario_completo[palabra_lower])
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
# Opción para añadir palabras personalizadas
nueva_palabra = st.text_input("Añade una palabra personalizada para traducir:")

# Agregar la nueva palabra a la lista de palabras personalizadas
if nueva_palabra:
    palabras_personalizadas.append(nueva_palabra)

# Traducir la oración ingresada por el usuario
if oracion_usuario:
    oracion_traducida = traducir_oracion(oracion_usuario)
    st.session_state.oracion_traducida = oracion_traducida
    st.write(f"Traducción: {oracion_traducida}")
    audio_bytes = reproducir_audio(oracion_traducida, 'es')  # Usando español por defecto
    st.audio(audio_bytes, format='audio/mp3')






