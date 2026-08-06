[app]

# (str) Title of your application
title = Lord

# (str) Package name
package.name = lordapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.lord

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3, kivy==2.3.0, cython==0.29.33, qrcode, pillow, websocket-client

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
