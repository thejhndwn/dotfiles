#!/bin/bash

# Dotfiles directory
DOTFILES_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# List of dotfiles to symlink
dotfiles=(
  ".bashrc"
  ".vimrc"
  ".tmux.conf"
  ".gitconfig"
  ".zshrc"
)

# Backup directory for existing dotfiles
BACKUP_DIR="$HOME/dotfiles_backup_$(date +%Y%m%d_%H%M%S)"

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Function to symlink dotfiles
link_dotfile() {
  local src="$1"
  local dest="$2"
  
  if [ -f "$dest" ] || [ -d "$dest" ]; then
    echo "Backing up $dest to $BACKUP_DIR"
    mv "$dest" "$BACKUP_DIR/"
  fi
  
  echo "Creating symlink: $dest -> $src"
  ln -sf "$src" "$dest"
}

# Symlink each dotfile
for file in "${dotfiles[@]}"; do
  link_dotfile "$DOTFILES_DIR/$file" "$HOME/$file"
done

echo "Dotfiles installation complete!"
