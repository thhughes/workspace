# Workspace 
Toolset for creating a standardized workspace for any system in use. Similar to the "dotfiles" idea that many repo's have but I wanted to include more than just configurations. Looking to standardize and simplify: 
* Ways to add tools to bin without needing to update dotfiles 
* Management of file structure patterns I like
* Making it easily extendable for personal vs. work outcomes. 

You may find this an over-complication of the problem, but I had fun doing it and I think that's what matters. 

# Link Units 
Each of the directories in the workspace can be linked into the config by adding them under `workspace/structure.json` by including the field `"link-repo": true`. This field means that at construction the directory will not be created until the repo is installed properly. The installation will match a repo directory name to the workspace configured file path. It will then link the directory so it can be used. Each linked directory should have a readme section below to track anything needed/used in creation, along with thought process for when I forget and come back years from now. 

## .bin
Any tools to be packaged with the workspace. Auto-sourced by the workspace after build/installation. 

## Cron
Documentation: https://crontab.guru/
### Recommended: 
Should be a full path to script requiring no arguments 

## dotfiles
Standard catchall for the "dotfile" paradigm. 

### ZSH
Documentation: https://zsh.sourceforge.io/Doc/Release/Files.html 
* `.zshenv` 
    * Available to _all_ (including non-interactive) 
* `.zprofile` 
    * `PATH` and `EDITOR`
    * Environment variables to beh shared. 
* `.zshrc`
    * Appearance
    * aliases
    * interactive user only 

## image
Any non-dotfile scripts for imaging a base machine. These are less likely to be polished, play with care. 

## resources 
Any data files to be carried onto the box. 

# utility
Sourced tooling content intended to be available without inclusion.  

# Future Todo
* Tool to make a python environment. When you make the environment, it creates a sourced wrapper script that can activate and deactivate 

## Tools Worth Reading About 
* diff-so-fancy: Good-lookin' diffs with diff-highlight and more
* sip: Tool to create Python bindings for C and C++ libraries
* mas: https://github.com/mas-cli/mas
* zero: https://github.com/zero-sh/zero.sh



# Getting this done 
- There are 2 things to do: 
    - Setup the base structure of the system 
    - Link all the files for dot

- Structure Thoughts: 
    - Structure outlines the "structure" 
    - We have "hardcoded" directories that are in the repo that we link to the parent files 
        - This way the "strucuture" is set but we're also aligning the paths 
        - 