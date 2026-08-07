[app]
title = Lord 0.001
package.name = lordapp
package.domain = org.lord
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

python3==3.10.12,kivy==2.3.0,qrcode,pillow,websocket-client
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
