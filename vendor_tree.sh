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
git clone https://github.com/OkBuddyGSI/extract_proprietary_blobs.git
cd AndroidDumpsCI
gh repo set-default https://github.com/OkBuddyGSI/extract_proprietary_blobs.git

# Take URL as an argument
FIRMWARE_DUMP_REPO=$1
FIRMWARE_DUMP_BRANCH=$2
DEVICE_TREE_REPO=$3
DEVICE_TREE_BRANCH=$4
DEVICE_CODENAME=$5
DEVICE_VENDORNAME=$6

# Run the GitHub Actions workflow with the specified URL
gh workflow run extract-blobs.yml -f FIRMWARE_DUMP_REPO=$FIRMWARE_DUMP_REPO FIRMWARE_DUMP_BRANCH=$FIRMWARE_DUMP_BRANCH DEVICE_TREE_REPO=$DEVICE_TREE_REPO DEVICE_TREE_BRANCH=$DEVICE_TREE_BRANCH DEVICE_CODENAME=$DEVICE_CODENAME DEVICE_VENDORNAME=$DEVICE_VENDORNAME USER_NAME="sounddrill31" USER_EMAIL="sounddrill31@gmail.com"
