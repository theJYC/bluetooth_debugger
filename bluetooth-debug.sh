#!/bin/bash

#navigate to the project directory in Terminal,
#and run command "sudo ./bluetooth-debug.sh" [see below]

path=/Library/Preferences/
file=com.apple.Bluetooth.plist

if [$path$file]; then
    rm $path$file
    echo "Corrupt file removed."
    # restarting the computer
    shutdown -r now
else
    # in case the file does not exist upon lookup:
    echo "Corrupt file has not yet been generated."
fi

#alternatively, you can run "sudo bash bluetooth-debug.sh"
#whereby you can omit the relative path and just reference the .sh file
