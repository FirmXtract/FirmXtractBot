#!/bin/bash

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

# Pull latest source code
git pull

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
