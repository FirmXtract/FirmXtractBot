from info import *
import subprocess


botid = 7004812988


def command(m): 
    if m.text == "/start":
        request()

def request():
    result = subprocess.run(
    ['ls', '-l'],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)
print(result.stdout)
print(result.stderr)