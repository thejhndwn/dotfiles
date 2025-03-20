#!/bin/bash

# install necessary initial dependencies
sudo apt update && sudo apt install -y git gh curl vim 

# Decrypt GitHub PAT if available
if [ -f ~/.github_token ]; then
    echo "GitHub token already exists."
else
    # run the PAT decription script
    bash ./scripts/decrypt_pat.sh
fi

# Authenticate GitHub CLI
if [ -f ~/.github_token ]; then
    GITHUB_TOKEN=$(cat ~/.github_token)
    echo "$GITHUB_TOKEN" | gh auth login --with-token
else
    echo "GitHub token file not found!"
fi

# download the github dotfiles
gh repo clone thejhndwn/dotfiles
# sync system setup
bash ./scripts/sync_aliases.sh
# sync system updates


