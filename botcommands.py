from info import *
import subprocess


botid = 7004812988


def command(m): 
    if m.text == "/start":
        request()

def request():
    result = subprocess.run(
    ["""# Check if gh is installed
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

# Define the Personal Access Token (PAT)
PAT="replace with pat"

# Setup gh with the PAT
gh auth login --with-token $PAT

# Set the repository
git clone https://github.com/sounddrill31/AndroidDumpsCI.git
cd AndroidDumpsCI
gh repo set-default https://github.com/sounddrill31/AndroidDumpsCI.git

# Take URL as an argument
URL=$1

# Run the GitHub Actions workflow with the specified URL
gh workflow run DumprX-crave.yml -f ROM_URL=$URL""", ''],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)
    print(result.stdout)
    print(result.stderr)