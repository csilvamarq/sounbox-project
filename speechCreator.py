import speech_recognition as sr
import requests
import keyboard
import os
import time

# Función para enviar el texto a tu API de modelo de lenguaje
def enviar_texto_a_api(texto):
    # URL de tu API de modelo de lenguaje
    url_api = 'http://localhost:3001/v1/completions'
    # Parámetros de la solicitud (aquí puedes ajustar según los requisitos de tu API)
    params = {
        "prompt": "\n\n### Instructions:\n" + texto + "\n\n### Response:\n",
        "stop": ["\n", "###"]
    }
    # Realizar la solicitud POST a tu API
    response = requests.post(url_api, json=params)
    # Devolver la respuesta de la API
    return response.json()
def speechcreator():
    # Inicializa el reconocedor
    recognizer = sr.Recognizer()

    # Utiliza el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)

    try:
        # Transcribe el audio a texto utilizando Google Speech Recognition API
        texto_transcrito = recognizer.recognize_google(audio, language='es-ES')
        print("Texto transcribido:", texto_transcrito)

        # Envía el texto transcribido a tu API de modelo de lenguaje
        respuesta_api = enviar_texto_a_api(texto_transcrito)

        # Itera sobre las elecciones y accede al texto de cada una
        choices = respuesta_api["choices"]
        for choice in choices:
            texto_generado = choice["text"]
            print("Texto generado dentro de choices:", texto_generado)

            # Obtiene el timestamp actual como cadena
            timestamp = str(int(time.time()))

            # Ruta del directorio de salida
            output_dir = "./spanish"
            os.makedirs(output_dir, exist_ok=True)  # Crea el directorio si no existe

            # Ruta del archivo de salida
            output_file = os.path.join(output_dir, f"{timestamp}.txt")

            # Escribe el texto generado en el archivo de salida
            with open(output_file, "w") as file:
                file.write(texto_generado)

            print(f"Texto generado guardado en: {output_file}")

    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al solicitar la API de Google: {0}".format(e))
# Inicializa el reconocedor
    recognizer = sr.Recognizer()

# Utiliza el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)

    try:
        # Transcribe el audio a texto utilizando Google Speech Recognition API
        texto_transcrito = recognizer.recognize_google(audio, language='es-ES')
        print("Texto transcribido:", texto_transcrito)
    
        # Envía el texto transcribido a tu API de modelo de lenguaje
        respuesta_api = enviar_texto_a_api(texto_transcrito)

        # Itera sobre las elecciones y accede al texto de cada una
        choices = respuesta_api["choices"]
        for choice in choices:
            texto_generado = choice["text"]
            print("Texto generado dentro de choices:", texto_generado)
    
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al solicitar la API de Google: {0}".format(e))
def on_key_event(event):
    if event.name == 'i':  # Si se presiona la tecla "i"
        speechcreator()

# Registra el controlador de eventos para la tecla "i"
keyboard.on_press(on_key_event)

# Mantenemos el programa en ejecución
keyboard.wait('esc')  # Espera hasta que se presione la tecla "esc" para salir del programa