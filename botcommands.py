from info import *
import subprocess


botid = 7004812988


def command(m): 
    if m.text == "/start":
        request(m)

def request(m):
    URL = m.text.split()[1]
    result = subprocess.run(
    ['ls', '-l'],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
    )
    print(result.stdout)
    print(result.stderr)