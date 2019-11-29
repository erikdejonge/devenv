# opening and closing windows and popovers
defaults write -g NSAutomaticWindowAnimationsEnabled -bool true

# smooth scrolling
defaults write -g NSScrollAnimationEnabled -bool true

# showing and hiding sheets, resizing preference windows, zooming windows
# float 0 doesn't work
defaults write -g NSWindowResizeTime -float 0.5

# opening and closing Quick Look windows
defaults write -g QLPanelAnimationDuration -float 0.5

# rubberband scrolling (doesn't affect web views)
defaults write -g NSScrollViewRubberbanding -bool true

# resizing windows before and after showing the version browser
# also disabled by NSWindowResizeTime -float 0.001
defaults write -g NSDocumentRevisionsWindowTransformAnimation -bool true

# showing a toolbar or menu bar in full screen
defaults write -g NSToolbarFullScreenAnimationDuration -float 0.5

# scrolling column views
defaults write -g NSBrowserColumnAnimationSpeedMultiplier -float 0.5

# showing the Dock
defaults write com.apple.dock autohide-time-modifier -float 0.5
defaults write com.apple.dock autohide-delay -float 0.5

# showing and hiding Mission Control, command+numbers
defaults write com.apple.dock expose-animation-duration -float 0.5

# showing and hiding Launchpad
defaults write com.apple.dock springboard-show-duration -float 0.5
defaults write com.apple.dock springboard-hide-duration -float 0.5

# changing pages in Launchpad
defaults write com.apple.dock springboard-page-duration -float 0.5

# at least AnimateInfoPanes
defaults write com.apple.finder DisableAllAnimations -bool true

# sending messages and opening windows for replies
defaults write com.apple.Mail DisableSendAnimations -bool true
defaults write com.apple.Mail DisableReplyAnimations -bool true
