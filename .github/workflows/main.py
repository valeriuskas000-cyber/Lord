name: Build Lord App APK

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Python 3.10
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install Dependencies & Latest p4a via Git
      run: |
        python -m pip install --upgrade pip
        pip install cython==0.29.33
        pip install --upgrade buildozer
        # Подтягиваем свежий p4a напрямую из Git (чинит баг с 3.14)
        pip install --upgrade git+https://github.com/kivy/python-for-android.git@master

    - name: Install System Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev \
          zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev \
          libreadline-dev libffi-dev libgmp-dev libmpfr-dev libmpc-dev zip unzip ccache

    - name: Build APK with Buildozer
      run: |
        buildozer android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v3
      with:
        name: lord-app-apk
        path: bin/*.apk
