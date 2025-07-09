#!/bin/bash

echo 'installing dotfiles...'


ln -sf ~/dotfiles/.bashrc ~/.bashrc
ln -sf ~/dotfiles/.bash_aliases ~/.bash_aliases
ln -sf ~/dotfiles/.vimrc ~/.vimrc


chmod +x ~/dotfiles/scripts/*
