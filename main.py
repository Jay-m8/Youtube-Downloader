import os
from tqdm import tqdm
from tkinter import filedialog
from tkinter import *
from pytube import YouTube
import subprocess


def convert_Youtube_to_audio(Url_list, folder_selected):
    try:
        for vid in tqdm(Url_list, desc = "Downloading Video"):
# Get youtube video and store in video 
            video = YouTube(vid)
# Extract only the audio from the video
            audio = video.streams.get_audio_only()
# Download and Save the video to the selected folder
            out_path = audio.download(output_path=folder_selected)
# Gets the path for the MP4 but the file does not include file extension 
            new_name = os.path.splitext(out_path)
# Replace '\' with '/'
            true_path = new_name[0].replace(os.sep, '/')
# Variable that contains only the name of the file and filters out the path to the file
            file_name = true_path.split("/", -1)[-1]            
# Adds the MP4 file extension to the file path 
            default_file_name = true_path + ".mp4"
# Adds the MP3 file extension to a variable that only contains the name of the file to be used in the ffmpeg script
            file_name = file_name + ".mp3"
# Runs 'ffmpeg' command in cmd which I added to %PATH% - Edit the system environment variables and point ffmpeg to the path where the executable is located
# ffmpeg gets the MP4 file path and converts it to a MP3 file with 320kbps bitrate
            subprocess.run(f'ffmpeg -i "{default_file_name}"  -ab 320k "{folder_selected+"/"+file_name}"', shell=False)
# Deletes the MP4 file 
            os.remove(default_file_name)
    except:
        print("Error - URL incorrect, duplicate of files or code broken")

# Ask user for video URLs
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

        print("")
    
        #Youtube to MP3 function
        convert_Youtube_to_audio(Url_list, folder_selected)
        

