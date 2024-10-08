## .zsh files 
## -> .zshenv -- Always
## -> .zprofile -- login shells before .zshrc
## -> .zshrc -- interactive shells last. 
##
## Fill in as needed


## workspace/structure.json -> Summary.root_link
source ~/.workspace.sh

export PATH=$PATH:$_ws_bin:$_ws_repo_bin:$_ws_py_env_bin

if [ -d "$HOME/.oh-my-zsh" ]; then 
    export ZSH="$HOME/.oh-my-zsh"
    ZSH_THEME="robbyrussell"
    plugins=(git)
    source $ZSH/oh-my-zsh.sh
fi 