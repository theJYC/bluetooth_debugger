# navigate to the project directory in Terminal,
# and run command "sudo python bluetooth_debugger.py".

import os

path = "/Library/Preferences/"

os.chdir(path)

for i in os.listdir(path):
    if (i == 'com.apple.Bluetooth.plist'):
        os.unlink(i)
    else:
        pass
