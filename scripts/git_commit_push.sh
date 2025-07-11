#!/bin/bash

# Function to add, commit, and push changes
function git_commit_push() {
  git add .
  if [[ -z "$1" ]]; then
    read -p "Enter commit message: " message
  else
    message="$1"
  fi
  git commit -m "$message"
  git push
}

# Call the function
git_commit_push "$@"

