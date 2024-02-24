from info import *
import subprocess


botid = 7004812988


def command(m): 
    if m.text == "/start":
        request()

def request():
    command_executer = subprocess.call("./dump.sh", shell=True)