# macOS_bluetooth_debugger

#### Technologies: Python, Terminal

. 

Through the use of `localstorage` and `DOM manipulation`, `checkedin.` enables users to submit a contact that are due for a check-in and, upon page-refresh, update each contact's `daysLeft` variable to indicate whether the check-in is due/past-due, and/or signal how many days are left between the check-in date and the current date of browser session. 

To make the most out of `checkedin.` it is encouraged to bookmark the [URL](https://jinyoungch0i.github.io/checkedin./) for ease of access, and to run it on a Chromium-based browser (such as Google Chrome, Microsoft Edge, or [Brave](https://brave.com/))

[Live Demo](https://jinyoungch0i.github.io/checkedin./) & [Source Code](https://github.com/jinyoungch0i/checkedin.)


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
