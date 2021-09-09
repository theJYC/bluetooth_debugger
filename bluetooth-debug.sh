#!/bin/bash

#navigate to project dir in Terminal,
#and run command "sudo ./bluetooth-debug.sh"

path=/Library/Preferences/
file=com.apple.Bluetooth.plist

if [$path$file]; then
    rm $path$file
    echo "Corrupt file removed."
    echo "Restarting your computer..."
    # shutdown -r now
else
    echo "Corrupt file has not yet been generated."
fi
