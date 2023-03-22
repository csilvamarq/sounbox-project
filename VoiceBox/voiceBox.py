import requests
import glob
from scipy.io import wavfile
import os
import time
import numpy as np
import json

path_to_watch = "../japanese"
print('Your folder path is"', path_to_watch, '"')

old = os.listdir(path_to_watch)
print(old)

while True:
    new = os.listdir(path_to_watch)
    if len(new) > len(old):
        newfile = list(set(new) - set(old))
        print(newfile[0])
        old = new
        extension = os.path.splitext(path_to_watch + "/" + newfile[0])[1]
        if extension == ".txt":
            # * means all if need specific format then *.csv
            list_of_files = glob.glob('../japanese/**')
            latest_file = max(list_of_files, key=os.path.getctime)
            params = {
                'speaker': '1',
                'text': open(latest_file,encoding='UTF-8').read(),
            }
            dataJson = requests.post(
                'http://localhost:50021/audio_query', params=params)
            headers = {
                'Content-Type': 'application/json',
            }
            data = dataJson.json()
            timestr = time.strftime("%Y%m%d-%H%M%S")
            response = requests.post('http://localhost:50021/synthesis', params=params, headers=headers, data=data)
            wav = json.loads(response.text.replace('\n', '').replace('\r', '').encode())
            wavfile.write(f"./{timestr}.wav", 44100, wav)

        else:
            continue
    else:
        continue
