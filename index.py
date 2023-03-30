from transcriber import transcriber
from translator import translator
from voiceBox import voicebox
from player import player
from threading import Thread

t1 = Thread(target=transcriber)
t2 = Thread(target=translator)
t3 = Thread(target=voicebox)
t4 = Thread(target=player)
t1.start()
t2.start()
t3.start()
t4.start()
