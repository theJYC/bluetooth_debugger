# bluetooth_debugger

#### Technologies: Python, Terminal

A simple CLI script that automates the deletion of the macOS auto-generated file `com.apple.Bluetooth.plist`, which often causes a corruption in the connection between macOS machines and its Bluetooth devices. 

While one can certainly execute the debug manually through the GUI (see [MANUAL_DEBUG_INSTRUCTIONS.md](https://github.com/jinyoungch0i/bluetooth_debugger/blob/master/MANUAL_DEBUG_INSTRUCTIONS.md), this script aims to automate the process so that--upon successfully following the `necessary steps` outlined in the `Installation Guide`-- the only thing that they will have to do is run a single command in the Terminal and reboot their Mac. 

I found out about this tedius problem while working with my daily driver, logitech m557, which would sporadically become laggy after a certain period of bluetooth connection. 

While looking for a problem, I came across this discussion 

[Inspiration](https://discussions.apple.com/thread/4969915?answerId=22070560022#22070560022) & [Source Code](https://github.com/jinyoungch0i/checkedin.)


Preface: This script is going to require you to first enable Full Disk Access to Terminal,
Since this automation script involves operating on a file that can only be removed via admin permission. 

Full Disk Access to Terminal is given via:

System Prefences > Security & Privacy > Full Disk Access > add Terminal (which can be found in the Utilities directory within Applications)


In a nutshell, this script aims to automate the removal of the file ‘com.apple.Bluetooth.plist’ which always solves the sporadic lag issue that arises with bluetooth mice and Mac OS. 

First, click on Finder, and on the top navigation bar, click Go > Go To Folder (shift + command + G)…

In the pop-up window: type in the following path: 

/Library/Preferences

Then, scroll through the list of files (arranged in alphabetical order) and find ‘com.apple.Bluetooth.plist’:

`right click` on the file, click `Get Info`, then scroll to the bottom of the window to find the small lock button on the right.

Click on the lock button, type password / touchID, then within `Sharing & Permissions`, change `everyone`’s `Privilege` from `Read only` to `Read & Write`.

Then, open Terminal (which can either be accessed via ‘Launchpad > Utilities > Terminal’ or ‘Finder > Applications > Utilities > Terminal’)

Navigate to the Preferences directory, via following command:

cd /Library/Preferences

(As an additional step, you could confirm that you are in the correct directory by running the ‘ls’ command, which will return a long list of items among which is ‘com.apple.Bluetooth’)

Since ‘com.apple.Bluetooth.plist’ is locked for admin permission, change file ownership via following command:

sudo chown <username>:admin com.apple.Bluetooth.plist

(To find <username>, you can open a Finder window, then click on Go > Home to see the username on the header of the resulting finder window)

Then, type in password & press `enter`. 

Now, navigate to the address where `debug_bluetooth.py` was installed in your local machine. 
(For example, if you had installed it on Desktop:)

You could do it two ways: 

Type in the following command in the Terminal window (replacing <username> with your username: 

cd ../../Users/<username>/Desktop

Then, run the command:

sudo python debug_bluetooth.py

Enter password when prompted.

Voilá! 
