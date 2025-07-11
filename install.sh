#!/bin/bash

echo 'installing dotfiles...'

# configuring environment variables
ENV_FILE=".env"
LOCAL_ENV_FILE=".env.local"

# Create .env.local if it doesn't exist
if [ ! -f "$LOCAL_ENV_FILE" ]; then
    echo "Creating $LOCAL_ENV_FILE from $ENV_FILE template..."
    cp "$ENV_FILE" "$LOCAL_ENV_FILE"
else
    echo "$LOCAL_ENV_FILE already exists. Skipping copy."
fi

echo "Configuring environment variables..."
echo "------------------------------------"

comments=()

while IFS= read -r line || [ -n "$line" ]; do
    # Collect comments and blank lines
    if [[ "$line" =~ ^[[:space:]]*$ ]]; then
        comments=()
        continue
    elif [[ "$line" =~ ^# ]]; then
        comments+=("$line")
        continue
    fi

    # Extract key and current value
    key=$(echo "$line" | cut -d= -f1)
    current_value=$(grep "^$key=" "$LOCAL_ENV_FILE" | cut -d= -f2-)

    # Show comments (help text)
    if [ ${#comments[@]} -gt 0 ]; then
        echo
        for comment in "${comments[@]}"; do
            echo "$comment"
        done
    fi

    # Prompt user (redirect from /dev/tty to avoid conflict with while loop)
    read -p "Enter value for $key [default: $current_value]: " input < /dev/tty
    input=${input:-$current_value}
    
    # Expand variables like $HOME in the input
    input=$(eval echo "$input")

    # Escape input for safe sed substitution
    escaped_input=$(printf '%s\n' "$input" | sed 's/[/&]/\\&/g')

    # Update or insert in .env.local
    if grep -q "^$key=" "$LOCAL_ENV_FILE"; then
        sed -i.bak "s|^$key=.*|$key=$escaped_input|" "$LOCAL_ENV_FILE"
    else
        echo "$key=$escaped_input" >> "$LOCAL_ENV_FILE"
    fi

    # Clear comment buffer
    comments=()
done < "$ENV_FILE"

echo
echo "✅ Environment setup complete! You can now use your local configuration."

# env variable configuration is done

source $LOCAL_ENV_FILE

# linking the important configs using the DOTFILES_ROOT variable
echo "Creating symlinks..."
ln -sf "$DOTFILES_ROOT/.bashrc" ~/.bashrc
ln -sf "$DOTFILES_ROOT/.bash_aliases" ~/.bash_aliases  
ln -sf "$DOTFILES_ROOT/.vimrc" ~/.vimrc

# making scripts executable
if [ -d "$DOTFILES_ROOT/scripts" ]; then
    chmod +x "$DOTFILES_ROOT/scripts"/*
fi

echo "✅ Dotfiles installation complete!"
