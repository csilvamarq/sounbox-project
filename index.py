from voiceBox import voicebox
from player import player
from threading import Thread
from translator import translator
t1 = Thread(target=translator)
t2 = Thread(target=voicebox)
t3 = Thread(target=player)
t1.start()
t2.start()
t3.start()
