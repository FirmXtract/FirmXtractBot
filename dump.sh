# Check if gh is installed
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

# Define the Personal Access Token (PAT)
#PAT="replace with pat"

# Setup gh with the PAT
#gh auth login --with-token $PAT

# Set the repository
#git clone https://github.com/sounddrill31/AndroidDumpsCI.git
#cd AndroidDumpsCI
#gh repo set-default https://github.com/sounddrill31/AndroidDumpsCI.git

# Take URL as an argument
#URL=$1

# Run the GitHub Actions workflow with the specified URL
#gh workflow run DumprX-crave.yml -f ROM_URL=$URL
