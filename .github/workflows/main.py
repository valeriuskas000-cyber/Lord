name: Build Lord App APK

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Java 17
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Set up Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          sudo apt update
          sudo apt install -y build-essential libssl-dev libffi-dev python3-dev zip unzip openjdk-17-jdk git autoconf libtool pkg-config gettext cmake libltdl-dev
          
          # Лорд зажимает Cython в рамки 0.29.36
          pip install --upgrade pip setuptools "Cython==0.29.36" "buildozer==1.5.0"
          pip cache purge

      - name: Configure & Build APK (Lord Library Harmonizer)
        run: |
          # 1. Очистка старых хвостов
          rm -rf .buildozer bin build
          rm -f buildozer.spec
          
          buildozer init
          
          # 2. Настройка архитектуры и API
          sed -i 's/^android.api = .*/android.api = 33/' buildozer.spec
          sed -i 's/^android.minapi = .*/android.minapi = 24/' buildozer.spec
          sed -i 's/^#\?android.archs = .*/android.archs = arm64-v8a/' buildozer.spec
          
          # 3. Лорд принудительно подгоняет библиотеки троицы
          sed -i 's/^requirements = .*/requirements = python3,kivy/' buildozer.spec
          
          # 4. Запуск сборки
          yes | buildozer -v android debug

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: LordApp-APK
          path: bin/*.apk
