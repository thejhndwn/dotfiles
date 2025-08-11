<!-- TOC START -->
- [Commands](#commands)
  - [tridactyl](#tridactyl)
  - [git](#git)
  - [gh](#gh)
  - [websocket](#websocket)
- [Packages](#packages)
<!-- TOC END -->

# Commands

## tridactyl
r                                               | refresh



## git

git rm --cached <file/dir>                          | remove file from git tracking/git cache, add -r for directory removal

## gh
gh repo list thejhndwn                          | view my repos
gh repo clone thejhndwn/<repo_name>             | download repo 
gh repo create <project-name>                   | create github repo. flags: 
                                                | --public or --private
                                                | --source=.           | sets source directory for repo creation
                                                | --remote=origin      | set remote name
                                                | --push               | optional add push to push the current contents

## websocket
wscat --connect ws://<ip>:<port>                | open continuous connection to websocket, from npm

# Arch Commands

## esc tab keyboard mapping
setxkbmap -option caps:swapescape               | swaps the escape and capslock keymapping

# Packages
glow                                            | renders markdown in terminal
