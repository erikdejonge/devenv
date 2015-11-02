
property theURL : ""
set theURL to "chrome://version/"
set errored to false

tell application "Google Chrome"
	activate
end tell

try
	tell application "System Events"
		tell application "Google Chrome"
			
			set theURL to URL of tab of window 1
			set listSize to count of theURL
			
		end tell
	end tell
	
on error errStr
	display dialog errStr
	set errored to true
end try

if not errored then
tell application "System Events"
	tell process "Google Chrome"
		click menu item "Close All" of menu "File" of menu bar 1
		click menu item "New Incognito Window" of menu "File" of menu bar 1
	end tell
end tell

	repeat with aurl in theURL

tell application "Google Chrome"
	tell window 1
		open location aurl
	end tell
	activate
end tell

	end repeat
end if

