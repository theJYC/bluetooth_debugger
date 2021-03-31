import os

path = "/Library/Preferences/"

os.chdir(path)

for i in os.listdir(path):
    if (i == 'com.apple.Bluetooth.plist'):
        os.unlink(i)
    else:
        pass
