## .zsh files 
## -> .zshenv -- Always
## -> .zprofile -- login shells before .zshrc
## -> .zshrc -- interactive shells last. 
##
## Fill in as needed

## Required to use brew 
eval "$(/opt/homebrew/bin/brew shellenv)"


# Setting PATH for Python 3.12
# The original version is saved in .zprofile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:${PATH}"
export PATH
