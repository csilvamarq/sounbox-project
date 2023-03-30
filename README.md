# VoiceToWaifu Project

Project to syntetize your voice into anime waifu voice made with python and docker


## Features

- Transcribe in real time your voice to japanese waifu
- Fast and easy to setup
- Optimized to be used in low resources


## Requirements

*-Python 3.8*

*-Docker*

Optional :

*-Voicemeter* to redirect audio to mic output


## How to install

```bash
git clone https://github.com/Misil4/sounbox-project.git

pip install -r requirements.txt

docker compose up -d

python index.py

```








## How works?

When start python script you can press v to record your voice and t to stop recording, when you finish recording the record is transcribed by **Whisper** and translated by **Depl** to japanese (*katakana*).
To finish the japanese text file is synthetized by **Voicebox api** and outputs a wav file that plays in the background and can be redirected to be used as game mic output. 


## Related

This project is based in this other project
https://github.com/SociallyIneptWeeb/LanguageLeapAI/blob/main/docs/ENV.md


## Feedback

If you have any feedback, please email me to misil470gamer@gmail.com


## Authors

- [@Misil4](https://github.com/Misil4)


## License

[MIT](https://choosealicense.com/licenses/mit/)

