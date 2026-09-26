name: Build EXE
on: [push]
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install pyinstaller
      - run: pyinstaller --onefile --windowed --name DAVIER_NC main.py
      - uses: actions/upload-artifact@v4
        with:
          name: DAVIER-NC-EXE
          path: dist/DAVIER_NC.exe
