from info import *
import subprocess


botid = 7004812988


def command(m): 
    if m.text == "/start":
        request(m)

def request(m):
    URL = m.text.split()[1]
    process = subprocess.call(f"./dump.sh {URL}", shell=True, capture_output=True)