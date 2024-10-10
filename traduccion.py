import speech_recognition as sr
from pydub import AudioSegment

import os
# Establecer la ruta a ffmpeg de forma manual
AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe = "C:/ffmpeg/bin/ffprobe.exe"

def convertir_audio_a_texto(audio_path):
    # Convertir audio a formato compatible
    audio = AudioSegment.from_file(audio_path)
    audio.export("temp.wav", format="wav")
    
    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()
    
    # Cargar el archivo de audio
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        
    try:
        # Usar el motor de reconocimiento de Google
        texto = recognizer.recognize_google(audio_data, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return "No se pudo reconocer el audio"
    except sr.RequestError as e:
        return f"Error al procesar el audio; {e}"

# Prueba con un archivo
audio_path = "audio.mp3"  # Cambiar por el nombre del archivo de audio
texto_resultante = convertir_audio_a_texto(audio_path)
print("Texto reconocido:", texto_resultante)
