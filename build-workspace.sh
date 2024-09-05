#!/usr/bin/env bash

export script_dir=$(dirname "$0")
export root_dir=$(readlink -f "$script_dir")
source $root_dir/utility/logging.sh

check_installed() { 
    if ! command -v $1 &> /dev/null; then 
        log_error "$1 not installed"
        return 1
    fi 
    return 0
}

##
## Prep Work to make sure the system is ready for unpacking 
##
check_installed brew
if [ ! $? -eq 0 ]; then 
    exit 1
fi 

check_installed jq
if [ ! $? -eq 0 ]; then 
    log_info "Instal JQ with command \$brew install jq"
    exit 1
fi 

check_installed python3
if [ ! $? -eq 0 ]; then 
    log_info "Instal python3 or symlink command"
    exit 1
fi 

python3 workspace/builder.py workspace/structure.json

source ~/.zshrc
## Ideally, all future commands should be using the workspace built environment variables. 


