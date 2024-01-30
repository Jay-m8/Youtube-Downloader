import subprocess
from urllib.request import urlretrieve
import os

# Download directory for ffmpeg
filepath = os.path.expanduser("~/Desktop")

# Terminal command to install the required python dependencies in order of main.py to work
subprocess.run(f'pip install -r "requirements.txt"')

url = ("https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z")
name = f"{filepath}/" + "ffmpeg.7z"

# Download
urlretrieve(url, name)

# Ask user if they want to automatically extract zip file
question = input("If 7z zip is already installed and accessible via the terminal, do you want to automatically unzip it? Type 'yes' or 'no' ")
#print(bool(question))
if question == "yes":
    # Runs 7z to extract all the files from ffmpeg.7z and places them into a folder on the desktop
    subprocess.run(f'7z e {filepath}/ffmpeg.7z -o{filepath}/ffmpeg')
elif question == "no":
    quit