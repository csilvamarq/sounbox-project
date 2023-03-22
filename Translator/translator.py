import deepl
import glob
import time
import os

path_to_watch = "../spanish"
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
            list_of_files = glob.glob('../spanish/**')
            latest_file = max(list_of_files, key=os.path.getctime)
            with open(f'{latest_file}', 'r') as file:
                data = file.read()
            translator = deepl.Translator(
                "e83a265d-9575-1d5f-5b01-194082b95a70:fx")
            result = translator.translate_text(data, target_lang="JA")
            timestr = time.strftime("%Y%m%d-%H%M%S")
            print(timestr)
            with open(f'../japanese/{timestr}.txt', 'w',encoding='UTF-8') as f:
                f.write(result.text)
        else:
            continue
    else:
        continue
