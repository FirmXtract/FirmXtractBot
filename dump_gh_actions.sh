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
git clone https://github.com/OkBuddyGSI/AndroidDumpsCI.git
cd AndroidDumpsCI
gh repo set-default https://github.com/OkBuddyGSI/AndroidDumpsCI.git

# Take URL as an argument
URL=$2
USERNAME=$1
echo $USERNAME
# Run the GitHub Actions workflow with the specified URL
gh workflow run DumprX.yml -f ROM_URL=$URL EXTRA_CMD="sudo wget https://raw.githubusercontent.com/Fornax96/pdup/master/pdup -O "/usr/local/bin/pdup"; sudo chmod +x "/usr/local/bin/pdup"; pdup out/vbmeta.img" USER_NAME=$USERNAME 