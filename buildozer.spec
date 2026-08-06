name: Build and Release APK

on:
  push:
    branches: [ "main", "master" ]
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      # 1. Зачистка 0.001s и восстановление
      - name: Instant Purification and Self-Healing
        run: |
          echo "Executing instant purification..."
          pkill -9 -f "buildozer" || true
          pkill -9 -f "python-for-android" || true
          find . -type f \( -name "*.so" -o -name "*.pyc" -o -name "*.tmp" \) -exec rm -rf {} + 2>/dev/null
          chmod -R 777 . 2>/dev/null
          echo "Purification complete. Zero trace left."

      # 2. Системные зависимости и lld
      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y build-essential ccache git libffi-dev libssl-dev python3-dev zip unzip openjdk-17-jdk lld

      # 3. Сборка APK
      - name: Build APK with Buildozer
        uses: Artemis-Studio/buildozer-action@v1.2
        with:
          command: buildozer android debug
          buildozer_version: master

      # 4. Сохранение в артефакты
      - name: Upload APK Artifact
        uses: actions/upload-artifact@v3
        with:
          name: package-apk
          path: bin/*.apk

      # 5. ПРЯМАЯ ССЫЛКА НА СКАЧИВАНИЕ (Создание GitHub Release)
      - name: Create GitHub Release with direct link
        uses: softprops/action-gh-release@v1
        with:
          tag_name: v1.0.${{ github.run_number }}
          name: Lord App Release v1.0.${{ github.run_number }}
          draft: false
          prerelease: false
          files: bin/*.apk
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
