exports.options = {
    desiredCapabilities: {
        "platformName": "android",
        "platformVersion": "8.0",
        "appPackage": "com.android.chrome",
        "appActivity": "com.google.android.apps.chrome.Main",
        "unicodeKeyboard": false,
        "app": "E:\\Freelance\\christianvondru\\chrome.apk",
        "deviceName": "Emulator",
        "nativeInstrumentsLib": true
    },
    local: {
        host: "localhost",
        port: 4723
    }
}