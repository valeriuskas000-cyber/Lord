[app]

# (str) Title of your application
title = Lord 0.001

# (str) Package name
package.name = lordapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.lord

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Все задействованные модули: 4 канала сокетов, QR, графика Kivy
requirements = python3,kivy,qrcode,pillow,websocket-client

# (list) Permissions
# Разрешения для работы 4-канальной сети с биржей и записи QR
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) If True, then skip try to update the code
android.skip_update = False

# (bool) If True, the application will be accept incoming connections
android.accept_sdk_license = True

# (str) The orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0
