[app]

# (str) Title of your application
title = Lord 0.001

# (str) Package name
package.name = lordapp

# (str) Package domain
package.domain = org.lord

# (str) Source code location
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (БЕЗ РЕШЕТКИ В НАЧАЛЕ!)
version = 0.1

# (list) Application requirements
requirements = python3==3.10.12,kivy==2.3.0,qrcode,pillow,websocket-client

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Skip update
android.skip_update = False

# (bool) Accept SDK license
android.accept_sdk_license = True

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Architectures to build for
android.archs = arm64-v8a
