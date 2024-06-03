#!/bin/bash 

brew update
brew upgrade

brew install coreutils
brew install moreutils
brew install findutils
brew install gnu-sed --with-default-names
brew install zsh 

## Productivity 
brew install --cask spotify
brew install --cask pomatez
brew install --cask iterm2

## Editor Information 
brew install --cask visual-studio-code
## Trying to use vscode instead 
# brew install --cask pycharm-ce
# brew install --cask sublime-text

## Tools 
brew install tree
brew install ripgrep
brew install clang-format
brew install dockutil
brew install trash
brew install tldr

# Remove outdated versions from the cellar.
brew cleanup