# mac_bluetooth_debugger

**Technologies: Python, Terminal, Git (for Installation)**

A simple Python script that automates the deletion of the macOS auto-generated file `com.apple.Bluetooth.plist`, which often causes connection issues (read: mouse lags, inability to pair) between your Mac and its Bluetooth devices. 

In combining the Python script with its accompanying CLI guide, this program aims to automate the tedious process of routinely removing the abovementioned file, which would otherwise be performed via manual GUI interaction. 

[Inspiration](https://www.macbooster.net/how-to/fix-bluetooth-not-available-issue-on-macbook) (refer to point '3: Reset Bluetooth plist') & [Source Code](https://github.com/jinyoungch0i/checkedin.)

## Installation

0-1) Ensure that you have already downloaded `git`, for which the installation for macOS is detailed as: 

```
Installing on macOS
There are several ways to install Git on a Mac [...] On Mavericks (10.9) or above you can do this simply by trying to run git from the Terminal the very first time.
```

`git --version`

`If you don’t have it installed already, it will prompt you to install it.`

Source: [git-scm.com](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

*Side note: macOS comes with Python pre-installed, and there is no need to download Python individually given that this script does not make use of the latest Python 3 syntax.* 

0-2) Open up the Terminal, navigate to a directory that you'd like to save this program within your local machine (e.g. `cd Desktop/`) and clone this remote repository by typing in the following command:

`git clone git@github.com:jinyoungch0i/mac_bluetooth_debugger.git`

## Execution

1) Once successfully cloned, `right-click` on the `mac_bluetooth_debugger`folder icon, and select `New Terminal at Folder` from the dropdown. 

2) Within the Terminal window, type in the following command:

`sudo python bluetooth_debugger.py`<sup>?</sup>

3) Type in your Mac password when prompted, then press `enter (↵)`.

4) To finish the debug, reboot the mac by typing in the following command:

`sudo shutdown -r now`


<sup>?</sup>: *`sudo` is a particular syntax that enables you (the non-Admin user) to perform tasks that, by default, require Admin Permission. `sudo`, which stands for `superuser do`, enables you to bypass the default admin-lock via performing tasks as the root user*
