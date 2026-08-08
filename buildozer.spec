[app]

# (str) Title of your application
title = Lord App

# (str) Package name
package.name = lordapp

# (str) Package domain
package.domain = org.lord

# (list) Source files
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,cython==0.29.37

# (str) Supported orientations
orientation = portrait

# (list) The Android archs to build for
arch = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
