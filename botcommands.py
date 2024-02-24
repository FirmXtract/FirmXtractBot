from info import *
import subprocess


botid = 7004812988


def command(m): 
    if m.text == "/start":
        request(m)

def request(m):
    URL = m.text.split()[1]
    process = subprocess.Popen(["dump.sh"], stdout=subprocess.PIPE)

    while True:
        output = process.stdout.read(1)
        if not output:
            break
        print(output.decode(), end="")

    # Wait for the process to finish and check the return code
    process.wait()
    print(f"Process exited with code {process.returncode}")