from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from tkinter import *
from tkinter import filedialog
import subprocess

def download_audio(yt,folder_selected):
    try:
    # Filter all the audio files
        print("\nTitle:",yt.streams[0].title)
        my_streams = yt.streams.filter(only_audio=True)
        for streams in my_streams:
        # print audio quality/itag/codec 
            print(f"Audio itag : {streams.itag} Quality : {streams.abr} ACodec : {streams.codecs[0]}")
        # Allow user to select the quality/bitrate - Higher the better
        input_itag = input("Enter itag Value : ")
        audio = yt.streams.get_by_itag(input_itag)
        out_path = audio.download(output_path=folder_selected)
# Ask user what the extension of the file they downloaded is
        extension = os.path.splitext(out_path)[-1]
# Gets the path for the MP4 but the file does not include file extension 
        new_name = os.path.splitext(out_path)
# Replace '\' with '/'
        true_path = new_name[0].replace(os.sep, '/')
# Variable that contains only the name of the file and filters out the path to the file
        file_name = true_path.split("/", -1)[-1]            
# Adds the initial file extension to the file path 
        default_file_name = true_path + extension
# Adds the MP3 file extension to a variable that only contains the name of the file to be used in the ffmpeg script
        file_name = file_name + ".mp3"
# Runs 'ffmpeg' command in cmd which I added to %PATH% - Edit the system environment variables and point ffmpeg to the path where the executable is located
# ffmpeg gets the initial file path and converts it to a MP3 file with 320kbps bitrate
        subprocess.run(f'ffmpeg -i "{default_file_name}"  -ab 320k "{folder_selected+"/"+file_name}"', shell=False)
# Deletes the initial file 
        os.remove(default_file_name)
    except:
        print("Error - URL incorrect, duplicate of files or code broken")

while True:
    User_input = input("\nHey, paste your URLs here, separate each URL with a comma and type 'quit' to exit: ")
# Store each URL in one list 
    Url_list = User_input.split(",")
# If user enters quit, then stop the script
    if User_input == "quit":
        break
    else:
# Select a directory to download too
        root = Tk()
        root.lift()
        root.attributes("-topmost", True)
        root.withdraw()
        folder_selected = filedialog.askdirectory()
# Iterate through songs in Url_list
    for track in Url_list: 
        yt = YouTube(track, on_progress_callback = on_progress)
        download_audio(yt,folder_selected)
