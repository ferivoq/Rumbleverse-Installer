@ECHO OFF
py -3 -m pip install pyinstaller --quiet --disable-pip-version-check
py -3 -m pip install -r requirements.txt --quiet --disable-pip-version-check
pyinstaller --onefile --name RumbleVerseInstaller --icon icon.ico main.py