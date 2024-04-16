import glob
import time
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

def translator():
    path_to_watch = "./spanish"
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
                list_of_files = glob.glob('./spanish/**')
                latest_file = max(list_of_files, key=os.path.getctime)
                with open(f'{latest_file}', 'r') as file:
                    data = file.read()
                    print(data)
                url_api = 'http://localhost:5000/translate'
                # Parámetros de la solicitud (aquí puedes ajustar según los requisitos de tu API)
                params = {
                    "q": data,
                    "source": "en",
                    "target": "ja"
                }
                # Realizar la solicitud POST a tu API
                translator = requests.post(url_api, json=params)
                result = translator.json()
                print(result)
                timestr = time.strftime("%Y%m%d-%H%M%S")
                translated_text = result.get("translatedText", "")
                # Eliminar etiquetas HTML usando BeautifulSoup
                soup = BeautifulSoup(translated_text, "html.parser")
                clean_text = soup.get_text()
                print(clean_text)
                print(timestr)
                with open(f'./japanese/{timestr}.txt', 'w',encoding='UTF-8') as f:
                    f.write(clean_text)
            else:
                continue
        else:
            continue

