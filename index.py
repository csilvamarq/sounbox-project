from transcriber import transcriber
from voiceBox import voicebox
from player import player
from threading import Thread
t1 = Thread(target=transcriber)
t3 = Thread(target=voicebox)
t4 = Thread(target=player)
t1.start()
t3.start()
t4.start()
