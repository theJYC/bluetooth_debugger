# mac_bluetooth_debugger

**Technologies: Python, Terminal, Git (for Installation)**

A simple Python program that automates the deletion of the macOS system-generated `com.apple.Bluetooth.plist` file, which causes connection issues (**read**: mouse lag, pairing failure) between your Mac and its Bluetooth devices. 

This program aims to automate the tedious process of manually removing the abovementioned file via the GUI, which takes several additional steps due to the file being admin-locked by default. 

[Inspiration](https://stackoverflow.com/questions/20553957/how-can-i-clear-the-corebluetooth-cache-on-macos) & [Source Code](https://github.com/jinyoungch0i/mac_bluetooth_debugger/blob/master/bluetooth_debugger.py)

## Pre-Installation

Ensure that you have already downloaded `Git`, for which you could run the following command in the Terminal: 

`git --version`

If you don’t have it installed already, it will prompt you to install it.

With regards to Python, Macs come with it pre-installed and there is no need to download the latest version of Python given that this script can be run on earlier versions. 

## Installation

Open up the Terminal, navigate to a directory that you'd like to save this program within your local machine (e.g. `cd Desktop/`) and clone this remote repository by typing in the following command:

`git clone git@github.com:jinyoungch0i/mac_bluetooth_debugger.git`

## Execution

1. Once the repository is successfully cloned, `right-click` on the `mac_bluetooth_debugger`folder icon, and select `New Terminal at Folder` from the dropdown. 

2. Within the Terminal window, type in the following command:

`sudo python bluetooth_debugger.py`

3. Type in your Mac password when prompted, then press `enter (↵)`.

4. To finish the debug, reboot the mac:

`sudo shutdown -r now`

N.B. Only reboot if/when the computer does not have any ongoing or unsaved processes! 🙈

## Afterthought

Thinking of ways to optimise `mac_bluetooth_debugger`, I was made aware that you can do everything that this Python script does directly on Terminal in just one line!:

`sudo rm /Library/Preferences/com.apple.Bluetooth.plist && sudo shutdown -r now`

All credits go to [./missing-semester](https://missing.csail.mit.edu/) for allowing me to get more comfortable with bash scripting and letting me eventually find a super streamlined solution! 😅
