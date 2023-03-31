import os
import glob
import wave
import pyaudio
from dotenv import load_dotenv
load_dotenv()


# Configuración de la reproducción de audio
CHUNK = 1024
path_to_watch = "./output"
print('Your folder path is"', path_to_watch, '"')

def player():    
    old = os.listdir(path_to_watch)
    print(old)

    while True:
        new = os.listdir(path_to_watch)
        if len(new) > len(old):
            newfile = list(set(new) - set(old))
            print(newfile[0])
            old = new
            extension = os.path.splitext(path_to_watch + "/" + newfile[0])[1]
            if extension == ".wav":
             # * means all if need specific format then *.csv
                list_of_files = glob.glob('./output/**')
                latest_file = max(list_of_files, key=os.path.getctime)
                out_device_index = os.getenv('AUDIO_OUTPUT_ID')
                # Inicializar PyAudio
                p = pyaudio.PyAudio()

              # Cargar el archivo WAV
                with wave.open(f'./output/{newfile[0]}', 'rb') as wave_file:
                    data = wave_file.readframes(wave_file.getnframes())
                    channels = wave_file.getnchannels()
                    width = wave_file.getsampwidth()
                    rate = wave_file.getframerate()

            # Definir la configuración de salida de audio
                out_stream = p.open(format=p.get_format_from_width(width),
                    channels=channels,
                    rate=rate,
                    output=True,
                    output_device_index=int(out_device_index))

                # Reproducir el archivo WAV utilizando el dispositivo de audio especificado
                out_stream.write(data)

                # Cerrar el flujo de salida 
                out_stream.stop_stream()
                out_stream.close()

                # Cerrar la instancia de PyAudio
                p.terminate()
                print("Terminado")
            else:
                continue
        else:
            continue
