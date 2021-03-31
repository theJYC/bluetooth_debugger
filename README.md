# mac_bluetooth_debugger

**Technologies: Python, Terminal, Git (for Installation)**

A simple Python program that automates the deletion of the macOS auto-generated file `com.apple.Bluetooth.plist`, which often causes connection issues (read: mouse lags, inability to pair) between your Mac and its Bluetooth devices. 

In combining the Python script with its accompanying CLI guide, this program aims to automate the tedious process of routinely removing the abovementioned file, which would otherwise be performed over several stages via manual GUI interaction. 

[Inspiration](https://www.macbooster.net/how-to/fix-bluetooth-not-available-issue-on-macbook) (*refer to '3: Reset Bluetooth plist'*) & [Source Code](https://github.com/jinyoungch0i/mac_bluetooth_debugger/blob/master/bluetooth_debugger.py)

## Pre-Installation

0.1) Ensure that you have already downloaded `Git`, for which you could run the following command in the Terminal: 

`git --version`

If you don’t have it installed already, it will prompt you to install it.

0.2) With regards to Python, Macs come with it pre-installed and there is no need to download the latest version of Python given that this script can be run on earlier versions. 

## Installation

0.3) Open up the Terminal, navigate to a directory that you'd like to save this program within your local machine (e.g. `cd Desktop/`) and clone this remote repository by typing in the following command:

`git clone git@github.com:jinyoungch0i/mac_bluetooth_debugger.git`

## Execution

1) Once successfully cloned, `right-click` on the `mac_bluetooth_debugger`folder icon, and select `New Terminal at Folder` from the dropdown. 

2) Within the Terminal window, type in the following command:

`sudo python bluetooth_debugger.py`  <sup>?</sup>

3) Type in your Mac password when prompted, then press `enter (↵)`.

4) To finish the debug, reboot the mac by typing in the following command:

`sudo shutdown -r now`


<sup>?</sup>  *`sudo` is a particular syntax that enables you (the non-Admin user) to perform tasks that, by default, require Admin Permission. `sudo`, which stands for `superuser do`, enables you to bypass the default admin-lock via performing tasks as the root user*
