# debug_bluetooth.py

# a simple automation script
# that debugs the bluetooth connectivity issue
# with mac OS and bluetooth devices (esp. logitech mice)

import os

path = "/Library/Preferences/"

os.chdir(path)

print(os.getcwd())
# returns: /Library/Preferences

for i in os.listdir(path):
    if (i == 'com.apple.Bluetooth.plist'):
        os.unlink(i)
    else:
        pass
