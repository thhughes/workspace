## Expectation: All of these

## CD Aliases
alias to-all="cd $_ws_root"
alias to-code="cd $_ws_code"
alias to-tmp="cd $_ws_tmp"
alias to-stage="cd $_ws_staged"
alias to-bin="cd $_ws_bin"
alias wsmgr="cd $_ws_mgr"

## List Aliases
alias ws-bin="ls -la $_ws_bin"
alias check-stage="ls -la $_ws_staged"
alias ll="ls -la"

## Random
alias gh="history | grep "
alias git-cfg="git config --list"
alias tedit="open -a 'Sublime Text'"

# Simplifying Windows Transitions
alias dir="ls -la"

## Python Aliases
function _start_env() {
  ## Wrapper to allow sourcing of pyton
	source $_ws_py_env_bin/$1
}
alias start-env="_start_env"
