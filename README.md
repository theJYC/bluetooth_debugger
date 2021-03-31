# mac_bluetooth_debugger

**Technologies: Python, Terminal**

A simple CLI script that automates the deletion of the macOS auto-generated file `com.apple.Bluetooth.plist`, which often causes a corruption in the connection between macOS machines and its paired Bluetooth devices. 

This Python script of 8 lines and its accompanying CLI guide aims to automate the tedius process of routinely removing the abovementioned file via manual GUI interaction. 

Upon running `sudo python bluetooth_debugger.py`, the user will only be required to reboot their machine to complete the debug process.

[Inspiration](https://discussions.apple.com/thread/4969915?answerId=22070560022#22070560022) & [Source Code](https://github.com/jinyoungch0i/checkedin.)

## Installation

0-1) Ensure that you have already downloaded `git`, for which the installation for macOS is given: 

```
Installing on macOS
There are several ways to install Git on a Mac. The easiest is probably to install the Xcode Command Line Tools. On Mavericks (10.9) or above you can do this simply by trying to run git from the Terminal the very first time.
```

`git --version`

```
If you don’t have it installed already, it will prompt you to install it.

If you want a more up to date version, you can also install it via a binary installer. A macOS Git installer is maintained and available for download at the Git website, at https://git-scm.com/download/mac.
```
Source: [git-scm.com](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

*Side note: macOS comes with Python pre-installed, and there is no need to download Python given that this script does not make use of the latest Python 3 syntax.* 

0-2) Navigate to a desired directory within your local machine (e.g. `Desktop/`) and clone this repository by typing in the command in the Terminal window:

`git clone git@github.com:jinyoungch0i/mac_bluetooth_debugger.git`

## Execution

1) Once successfully cloned, `right-click` on the `mac_bluetooth_debugger`folder icon, and select `New Terminal at Folder` from the dropdown. 

2) Within the Terminal window, type in the following command:

`sudo python bluetooth_debugger.py`

*Side note: `sudo` is a particular syntax that enables you (non-admin user) to perform tasks that are admin-locked by default; `sudo`, standing for `superuser do`, enables the bypass of admin permission via performing the tasks as the root user*

3) When prompted to type in `Password:`, type in the `password` for the mac and press `enter`.

4) reboot the mac by typing in the following command:

`sudo shutdown -r now`


