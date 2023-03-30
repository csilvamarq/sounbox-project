import pyaudio
import wave
import os
import glob

# Configuración de la reproducción de audio
CHUNK = 1024

# Inicializar el objeto PyAudio
p = pyaudio.PyAudio()
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
                wf = wave.open(latest_file, 'rb')

                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
                data = wf.readframes(CHUNK)

                while data:
                    stream.write(data)
                    data = wf.readframes(CHUNK)
                stream.stop_stream()
                stream.close()
                p.terminate()
            else:
                continue
        else:
            continue
