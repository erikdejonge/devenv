# Tested on OSX Yosemite 10.10.4
# there is also an updated version (work in progress) for El Capitan here https://gist.github.com/guycalledseven/31ffe35eca056838b06b

# XXX TODO
# should I disable com.google.Keystone.Agent ??
# http://applehelpwriter.com/2014/07/13/how-to-remove-googles-secret-update-software-from-your-mac/


# Stop DS_Store file creation on network connections
# restart Finder afterwards
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
killall Finder

# Disable / Enable Dashboard
# Settings / Mission control / Dashboard (selector) - Off
# or
# completely disable:
defaults write com.apple.dashboard mcx-disabled -boolean YES; killall Dock
# enable again:
#defaults write com.apple.dashboard mcx-disabled -boolean NO; killall Dock



# remove adobe auto update helper (i only have acrobat installed, so running this on adobe cc instalation could damage it)
# not tested
cd /Library/LaunchDaemons
launchctl remove `basename com.adobe.ARM* .plist`
sudo rm com.adobe.ARM*

cd /Library/LaunchAgents
launchctl remove `basename com.adobe.ARM* .plist`
sudo rm com.adobe.ARM*


# disable sending of crash reports to Apple (SubmitDiagInfo)
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.SubmitDiagInfo.plist

# disable photolibraryd
# com.apple.photomoments.xpc tries to access the internet without any reason and authorisation
# photos.app stops working after this
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.photolibraryd
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.cloudphotosd
# after restart they show up here
sudo launchctl unload -w /System/Library/LaunchAgents/com.apple.photolibraryd.plist
sudo launchctl unload -w /System/Library/LaunchAgents/com.apple.cloudphotosd.plist

# disable Apple Push Notification Service (apsd)
# FaceTime could complain
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.apsd.plist

# disable gamed
# make sure to log out from game center
sudo defaults write /System/Library/LaunchAgents/com.apple.gamed Disabled -bool true
# reset spotlight position
defaults delete com.apple.Spotlight userHasMovedWindow
# ... or reset spotlight position and size
defaults delete com.apple.Spotlight userHasMovedWindow;defaults delete com.apple.Spotlight windowHeight;killAll Spotlight


# disable gamed
launchctl unload -w /System/Library/LaunchAgents/com.apple.gamed.plist

