# mac_bluetooth_debugger

**Technologies: Python, Terminal, Git (for Installation)**

A simple Python program that automates the deletion of the macOS auto-generated file `com.apple.Bluetooth.plist`, which often causes connection issues (**read**: mouse lag, pairing failure) between your Mac and its Bluetooth devices. 

In combining the Python script with its accompanying CLI guide, this program aims to automate the tedious process of routinely removing the abovementioned file, which would otherwise be performed over several stages via manual GUI interaction. 

[Inspiration](https://www.macbooster.net/how-to/fix-bluetooth-not-available-issue-on-macbook) (*refer to '3: Reset Bluetooth plist'*) & [Source Code](https://github.com/jinyoungch0i/mac_bluetooth_debugger/blob/master/bluetooth_debugger.py)

## Pre-Installation

Ensure that you have already downloaded `Git`, for which you could run the following command in the Terminal: 

`git --version`

If you don’t have it installed already, it will prompt you to install it.

With regards to Python, Macs come with it pre-installed and there is no need to download the latest version of Python given that this script can be run on earlier versions. 

## Installation

Open up the Terminal, navigate to a directory that you'd like to save this program within your local machine (e.g. `cd Desktop/`) and clone this remote repository by typing in the following command:

`git clone git@github.com:jinyoungch0i/mac_bluetooth_debugger.git`

## Execution

1) Once the repository is successfully cloned, `right-click` on the `mac_bluetooth_debugger`folder icon, and select `New Terminal at Folder` from the dropdown. 

2) Within the Terminal window, type in the following command:

`sudo python bluetooth_debugger.py`

3) Type in your Mac password when prompted, then press `enter (↵)`.

4) To finish the debug, reboot the mac:

`sudo shutdown -r now`

N.B. Only reboot when the computer does not have any ongoing / unsaved processes! 🙈
