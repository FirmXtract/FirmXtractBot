from info import *
import subprocess


botid = 7004812988


def command(m): 
    if m.text == "/start":
        request(m)

def request(m):
    URL = m.text.split()[1]
    process = subprocess.Popen(
    ["sh", "./dump.sh"],  # Replace with the actual path to your script
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,  # Combine stdout and stderr for simplicity
    universal_newlines=True  # Ensure text output is handled correctly
    )
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        print(output.strip())  # Print the output line without trailing newline


