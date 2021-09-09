# bluetooth_debugger

**Technologies: Bash, Node.js, Python**

A simple automation script that removes the macOS system-generated `com.apple.Bluetooth.plist` file, which causes connection issues (**read**: mouse lag, pairing failure) between Mac computers and its paired Bluetooth devices. 

This program aims to automate the tedious process of manually removing the abovementioned file via the GUI, which takes several additional steps due to the file being admin-locked by default. 

[Context](https://stackoverflow.com/questions/20553957/how-can-i-clear-the-corebluetooth-cache-on-macos) & [Source Code](https://github.com/jinyoungch0i/mac_bluetooth_debugger/blob/master/bluetooth_debugger.py)

## Pre-Installation

Ensure that you have already downloaded `Git`, for which you could run the following command in the Terminal: 

`git --version`

If you don’t have it installed already, it will prompt you to install it.

With regards to Python, Macs come with it pre-installed and there is no need to download the latest version of Python given that this script can be run on earlier versions. 

Finally, Node.js can be installed at this [official link](https://nodejs.org/en/download/).

## Installation

Open up the Terminal, navigate to a directory that you'd like to save this program within your local machine (e.g. `cd Desktop/`) and clone this remote repository by typing in the following command:

`git clone git@github.com:jinyoungch0i/bluetooth_debugger.git`

## Execution

1. Once the repository is successfully cloned, `right-click` on the `bluetooth_debugger`folder icon, and select `New Terminal at Folder` from the dropdown. 

Since this script is implemented in three different options:
- Bash: `./bluetooth-debug.sh`
- Node.js: `./bluetoothDebugger.js`
- Python: `./bluetooth_debugger.py`

2. Within the Terminal window, type in **one** of the following commands:

- a) `sudo ./bluetooth-debug.sh`
- b) `sudo node ./bluetoothDebugger.js`
- c) `sudo python ./bluetooth_debugger.py`

N.B. Since each of the files are just different ways of implementing the same functionality, there is no need to run all three commands. 

3. Type in your Mac password when prompted, then press `enter (↵)`.

4. If either the JavaScript or Python files were executed, be sure to reboot the mac to finish the debug:

`sudo shutdown -r now`

N.B. Ensure that you don't have any ongoing/unsaved processes when rebooting your computer.

## Credits

All credits go to [./missing-semester](https://missing.csail.mit.edu/) for allowing me to get more comfortable with bash scripting, [Corey Schafer](https://www.youtube.com/watch?v=ve2pmm5JqmI&ab_channel=CoreySchafer) for the Python tutorial on the os module, and [NetNinja](https://www.youtube.com/watch?v=U57kU311-nE&t=367s&ab_channel=TheNetNinja) for his equivalent Node.js tutorial.
