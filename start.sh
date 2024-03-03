#!/bin/bash

# Check if gh is installed
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

# Function to store GitHub credentials in .netrc file

function store_github_credentials {

  local username="$1"

  local token_file="$2"


  # Read the token from the file

  local token=$(cat "$token_file")


  # Set the token as an environment variable

  export GITHUB_TOKEN="$token"


  # Create or update the .netrc file

  if [ -f ~/.netrc ]; then

    sed -i "s/^machine github.com\n\tlogin .*\n\tpassword .*$/machine github.com\n\tlogin $username\n\tpassword $token/g" ~/.netrc

  else

    cat >>~/.netrc <<EOF

machine github.com

    login $username

    password $token

EOF

  fi

}


# Set your GitHub username and token file path here

github_username="sounddrill31"

token_file="token.txt"


# Call the function to store the credentials

store_github_credentials "$github_username" "$token_file"


# Perform the git pull command

git pull origin main

# Parse command line argument
case $1 in
    --kill)
        echo "Stopping the bot..."
        tmux kill-session -t dumperbot
        echo "Bot stopped."
        ;;
    --restart)
            tmux kill-session -t dumperbot;
            tmux new-session -d -s dumperbot
            tmux send-keys -t dumperbot 'python3 main.py' Enter
            echo "Runner Restarted"
        ;;
    *)
        if tmux has-session -t dumperbot;
        then
            echo "Bot is already Running"
        else
            tmux new-session -d -s dumperbot
            tmux send-keys -t dumperbot 'python3 main.py' Enter
            echo "Runner Started"
        fi
        ;;
esac
