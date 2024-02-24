from info import *
import subprocess


botid = 7004812988

command = """
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

PAT="replace with pat"

gh auth login --with-token $PAT

git clone https://github.com/sounddrill31/AndroidDumpsCI.git
cd AndroidDumpsCI
gh repo set-default https://github.com/sounddrill31/AndroidDumpsCI.git

URL=$1

gh workflow run DumprX-crave.yml -f ROM_URL=$URL"""

def command(m): 
    if m.text == "/start":
        request()


def request():
    result = subprocess.run(
    [command, 'google.com'],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)
    print(result.stdout)
    print(result.stderr)