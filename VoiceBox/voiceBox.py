import requests
import glob
from scipy.io.wavfile import write
import os

path_to_watch = "./japanese"
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
            list_of_files = glob.glob('./japanese/**')
            latest_file = max(list_of_files, key=os.path.getctime)
            params = {
                'speaker': '1',
                'text': open(latest_file).read(),
            }
            dataJson = requests.post(
                'http://localhost:50021/audio_query', params=params)
            headers = {
                'Content-Type': 'application/json',
            }
            
            data = dataJson.json().read().replace('\n', '').replace('\r', '').encode()
            response = requests.post('http://localhost:50021/synthesis', params=params, headers=headers, data=data)
            print(response)

        else:
            continue
    else:
        continue
