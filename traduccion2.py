import speech_recognition as sr
from pydub import AudioSegment
import os

# Establecer la ruta a ffmpeg de forma manual (ajusta la ruta según donde tengas instalado ffmpeg)
AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe = "C:/ffmpeg/bin/ffprobe.exe"

def convertir_audio_a_texto(audio_path):
    try:
        # Convertir el audio de WhatsApp (ogg/opus) a wav
        audio = AudioSegment.from_file(audio_path)  # Ajusta el formato si es opus
        temp_wav_path = "temp.wav"
        audio.export(temp_wav_path, format="wav")
        
        # Inicializar el reconocedor de voz
        recognizer = sr.Recognizer()
        
        # Cargar el archivo de audio convertido
        with sr.AudioFile(temp_wav_path) as source:
            audio_data = recognizer.record(source)
            
        # Usar el motor de reconocimiento de Google
        texto = recognizer.recognize_google(audio_data, language="es-ES")
        
        return texto
    except sr.UnknownValueError:
        return "No se pudo reconocer el audio"
    except sr.RequestError as e:
        return f"Error al procesar el audio: {e}"
    finally:
        # Eliminar el archivo temporal .wav
        if os.path.exists(temp_wav_path):
            os.remove(temp_wav_path)

# Ejemplo de uso
audio_path = "audio.mp3"  # Coloca aquí la ruta de tu archivo de audio de WhatsApp
resultado = convertir_audio_a_texto(audio_path)
print(resultado)
