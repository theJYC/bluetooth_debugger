/*
navigate to the project directory in Terminal,
and run command `sudo node bluetoothDebugger.js`.
*/

const fs = require("fs")

const path = "/Library/Preferences/"
const corruptFile = "com.apple.Bluetooth.plist"

const absolutePath = `${path}${corruptFile}`
console.log(absolutePath)

if (fs.existsSync(absolutePath)) {
    fs.unlink(absolutePath, err => {
        if (err) {
            return console.log(err)
        }
        console.log("file deleted. Restart your computer")
    })
}
