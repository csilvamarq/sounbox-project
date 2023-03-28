import requests
import glob
from scipy.io import wavfile
import os
import time
import numpy as np
import pyttsx3
import wave


def voicebox():
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
                print(f"./japanese/{latest_file}")
                timestr = time.strftime("%Y%m%d-%H%M%S")
                audio = f"./{timestr}.wav"
                os.system(f"docker run --rm -v ./japanese/{newfile[0]}:/input.txt -v {audio}:/output.wav voiceboxengine/voicebox python3 /app/voicebox.py -t /input.txt -o /output.wav")

            else:
                continue
        else:
            continue
