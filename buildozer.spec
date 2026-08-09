[app]

title = Lord App
package.name = lordapp
package.domain = org.lord
source.dir = .
version = 0.1
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy,cython==0.29.37
orientation = portrait
arch = arm64-v8a

# Полные параметры SDK и API для автоматической загрузки всех инструментов (включая aidl и build-tools)
android.api = 33
android.min_api = 21
android.sdk = 33
android.ndk = 25.2.9519653
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
