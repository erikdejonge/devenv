#!/bin/bash
if [[ "" != $(xrandr | grep connected | grep 3840x1600) ]]; then
	if [[ "" != $(xrandr | grep connected | grep 3840x1600 | puf 'cols[0]'|puf '[x for x in lines if "DP1" == x.strip()]') ]]; then
	    echo 'widescreen'
	    xrandr --output HDMI1 --off --output DP1 --primary --mode 3840x1600 --pos 0x0 --rotate normal --output eDP1 --off --output VIRTUAL1 --off
	    exit
	fi
fi
if [[ "" != $(xrandr | grep connected | grep 3840x1600) ]]; then
	if [[ "" != $(xrandr | grep connected | grep 3840x1600 | puf 'cols[0]'|puf '[x for x in lines if "DP-1-1" == x.strip()]') ]]; then
	    echo 'widescreen nvidia'
	    xrandr --output HDMI-0 --off --output DP-0 --off --output DP-1 --off --output eDP-1-1 --off --output DP-1-1 --mode 3840x1600 --pos 0x0 --rotate normal --output HDMI-1-1 --off
	    exit
	fi
fi
if [[ "" != $(xrandr | grep connected | grep 3840x2160) ]]; then
	if [[ "" != $(xrandr | grep connected | grep 3840x2160 | puf 'cols[0]'|puf '[x for x in lines if "DP1" == x.strip()]') ]]; then
    	echo 'hdscreen'
		xrandr --output HDMI1 --off --output DP1 --primary --mode 3840x2160 --pos 0x0 --rotate normal --output eDP1 --off --output VIRTUAL1 --off
		exit
	fi
fi
#for output in $(xrandr | grep 3840x2160 | puf 'len([x for x in lines if x.startswith(" ")])'); do
#    echo '4k'
#done#
if [[ "" != $(xrandr | grep 'DP1 disconnected') ]]; then
  for output in $(xrandr | grep 1920x180 | puf 'len([x for x in lines if x.startswith(" ")])'); do
    echo 'laptop screen'
    xrandr --output HDMI1 --off --output DP1 --off --output eDP1 --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off
    exit
  done
else
    xrandr --output eDP1 --off --output DP1 --primary --mode 2560x1440 --pos 0x0 --rotate normal --output HDMI1 --off --output VIRTUAL1 --off
    exit
fi
