import requests
import glob
import os
import time
import numpy as np
from flask import Flask, request, Response
from urllib.parse import urlencode
import json


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
                text = open(f"{latest_file}", "r",encoding='UTF-8').read()
                speaker = int('5')
                if (text is None):
                    return json.dumps({'message': 'No text', 'status': 'BAD_REQUEST'}), 400
                speed_scale = float('1.7')
                volume_scale = float('4.0')
                intonation_scale = float('1.5')
                pre_phoneme_length = float('1.0')
                post_phoneme_length = float('1.0')
                params_encoded = urlencode({'text': text, 'speaker': speaker})
                r = requests.post(
                    f'http://localhost:50021/audio_query?{params_encoded}')
                if r.status_code == 404:
                    return Response(json.dumps({'message': 'Failed to request audio_query', 'json': r.json(), 'status': 'Server Error'}), mimetype='application/json', status=500)
                query = r.json()
                query['speedScale'] = speed_scale
                query['volumeScale'] = volume_scale
                query['intonationScale'] = intonation_scale
                query['prePhonemeLength'] = pre_phoneme_length
                query['postPhonemeLength'] = post_phoneme_length
                params_encoded = urlencode({'speaker': speaker})
                r = requests.post(
                    f'http://localhost:50021/synthesis?{params_encoded}', json=query)
                with open(f'./{timestr}.wav', mode='bx') as f:
                    f.write(r.content)
            else:
                continue
        else:
            continue
