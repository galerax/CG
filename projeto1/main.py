import threading
import os

t1 = threading.Thread(target = os.system('python input_terminal.py'))
t2 = threading.Thread(target = os.system('python input_terminal.py'))

t1.start()
t2.start()