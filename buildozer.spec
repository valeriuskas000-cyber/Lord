[app]
title = Lord
package.name = lordapp
package.domain = org.lord
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.10.12,kivy==2.2.1
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
