#!/bin/bash

# Check if gh is installed
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

# Authenticate using GH
gh auth login --with-token < token.txt

# Perform the git pull command
git pull origin main

sed -i "s/TOKEN/$(cat tele_token.txt)/g" info.py