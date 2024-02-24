from info import *
import subprocess


botid = 7004812988


def command(m): 
    if m.text == "/start":
        request()

def request():
    process = subprocess.call("./dump.sh", shell=True)
    print(process.stdout)