# debug_bluetooth.py

# once initial steps from README.md are observed,
# this simple script consisting of 8 lines of code
# will automatically remove a specific file, "com.apple.Bluetooth.plist",
# that seems to cause the bluetooth connection issues on mac OS.


import os

# this is where our desired file is automatically generated via mac OS:
path = "/Library/Preferences/"

os.chdir(path)

for i in os.listdir(path):
    if (i == 'com.apple.Bluetooth.plist'):
        os.unlink(i)
    else:
        pass
