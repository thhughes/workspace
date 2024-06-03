#!/usr/bin/env zsh


## Keep 
# Location 
defaults write com.apple.dock orientation -string left
# Size of the dock 
defaults write com.apple.dock tilesize -int 36
# Avoids creating a ton of "open window" in the dock from minimization
defaults write com.apple.dock minimize-to-application -bool true
# Can drag an app over the doc and hover to  open with that app
defaults write com.apple.dock enable-spring-load-actions-on-all-items -bool true
# Show indicator lights for open applications in the Dock
defaults write com.apple.dock show-process-indicators -bool true
# Speed up Mission Control animations
defaults write com.apple.dock expose-animation-duration -float 0.1
# disable doc auto hiding 
defaults write com.apple.dock autohide -bool false 
# Don’t show recent applications in Dock
defaults write com.apple.dock show-recents -bool false
# Make Dock icons of hidden applications translucent
defaults write com.apple.dock showhidden -bool true


# Hot corners
# Possible values:
#  0: no-op
#  2: Mission Control
#  3: Show application windows
#  4: Desktop
#  5: Start screen saver
#  6: Disable screen saver
#  7: Dashboard
# 10: Put display to sleep
# 11: Launchpad
# 12: Notification Center
# 13: Lock Screen
# Disable hot corners
defaults write com.apple.dock wvous-tl-corner -int 0
defaults write com.apple.dock wvous-tr-corner -int 0
defaults write com.apple.dock wvous-bl-corner -int 0
defaults write com.apple.dock wvous-br-corner -int 0


if ! command -v dockutil &> /dev/null; then
    echo "[Error] Must Install Dockutil. Visit the Brewery." >&2
    exit 1
fi

## Configure the Dock with Defaults first: 
defaults write com.apple.dock orientation -string left;

applications=(
	"Launchpad"
    "Messages"
    "Safari"
    "Maps"
    "Photos"
    "FaceTime"
    "Contacts"
    "Reminders"
    "Freeform"
    "TV"
    "Music"
    "News"
    "Keynote"
    "Numbers"
    "Pages"
    # Add more applications here
)

for app in $applications; do  
	dockutil --remove "$app" --no-restart
done

# Adds all these items to the dock first, then we reoraganize it 
# Add -> Move pattern simplifies the re-run pattern 
items=( 
	"/Applications/Xcode.app"
	"/Applications/PyCharm CE.app"
	"/Applications/Sublime Text.app" 
	"/Applications/iTerm.app"
	"/Applications/Google Chrome.app"
	"/Applications/Spotify.app"
	
	)

for app in $items; do 
	dockutil --add "$app"
done


# Sets the order of the doc
# anything not on this will just be be "BELOW"
dockOrder=(
	"Google Chrome"
	"Spotify"
	"Calendar"
	"Mail"
	"PyCharm CE"
	"Xcode"
	"Sublime Text"
	"iTerm"
	"System Settings"
	"Notes"
	"App Store"
	)

## Tracks the last "configured" item so that we can add more after if we want 
last=0
for ((i=1; i<=$#dockOrder; i++)); do
    dockutil --move "${dockOrder[$i]}" --position "$i" --allhomes
    last="$i"
done

ALL_HOME="~/Desktop/everything"
if [[ -d "$ALL_HOME" ]]; then
	dockutil --add "$ALL_HOME" --view list --display folder --position "$last"
fi
























killall Dock