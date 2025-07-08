#!/bin/bash

echo 'installing dotfiles...'


ln -sf ~/dotfiles/.bash_aliases ~/.bash_aliases
ln -sf ~/dotfiles/.vimrc ~/.vimrc


# TODO: when bashrc file is made, move this over there
echo 'export PATH="$HOME/dotfiles/scripts:$PATH"' >> ~/.bashrc
echo 'export PLANNER_ROOT="$HOME/dotfiles/plan"' >> ~/.bashrc

chmod +x ~/dotfiles/scripts/*

source ~/.bashrc
