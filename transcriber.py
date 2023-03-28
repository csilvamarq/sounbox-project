import whisper
import glob
import os
import time


def transcriber():
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
                model = whisper.load_model("base")
                result = model.transcribe(f"./Recorder/Records/{newfile[0]}")
                timestr = time.strftime("%Y%m%d-%H%M%S")
                with open(f'./spanish/{timestr}.txt', 'w') as f:
                    f.write(result["text"])
            else:
                continue
        else:
            continue
