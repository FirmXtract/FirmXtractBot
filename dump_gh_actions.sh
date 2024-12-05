# Check if gh is installed
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

# Authenticate against github.com by reading the token from a file
gh auth login --with-token < token.txt


# Set the repository
git clone https://github.com/FirmXtract/FirmXtract.git
cd FirmXtract
gh repo set-default https://github.com/FirmXtract/FirmXtract.git

# Take URL as an argument
URL=$1
# Run the GitHub Actions workflow with the specified URL
gh workflow run FirmXtract-DumprX.yml -f ROM_URL=$URL USER_NAME=$2 EXTRA_CMD="sudo wget https://raw.githubusercontent.com/Fornax96/pdup/master/pdup -O "/usr/local/bin/pdup"; sudo chmod +x "/usr/local/bin/pdup"; pdup out/vbmeta.img"