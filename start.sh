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

# Pull Latest source code
git pull

# Start the bot
python3 main.py
