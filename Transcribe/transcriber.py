import whisper
import glob
import os
import time

path_to_watch = "./Recorder/Records/"
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
        if extension == ".wav":
            # * means all if need specific format then *.csv
            list_of_files = glob.glob('../Recorder/Records/**')
            latest_file = max(list_of_files, key=os.path.getctime)
            with open(f'{newfile[0]}', 'r') as file:
                data = file.read()
            model = whisper.load_model("base")
            result = model.transcribe(latest_file)
            timestr = time.strftime("%Y%m%d-%H%M%S")
            with open(f'../spanish/{timestr}.txt', 'w') as f:
                f.write(result["text"])
        else:
            continue
    else:
        continue