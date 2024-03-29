# Youtube-Downloader #

This repository exists to overcome the issues I faced with using default Pytube. 

Author: `https://github.com/pytube/pytube` 

<h2> pytube </h2>
     
    ✅ Great for downloading MP4 files and YouTube video Metadata
    ❌ Bad for downloading MP3 files
    ❌ Downloaded MP3 files can't be play in Spotify or Itunes 
    ❌ Downloaded MP3 files can't be used in video editing software
---
<h2> That's where my solution comes in </h2>
    
    ✅ The script uses ffmpeg to turn the MP4 file downloaded from pytube into an actual MP3
    ✅ Supports submitting multiple URLs to be processed but not in parallel (maybe soon)
    ✅ Has a nice user-friendly GUI to select download destination

<h2> Installation </h2>

>This currently only works on Windows, has not been tested on other platforms

Before beginning you'll need a file archiver utility like 7-zip or WinRAR in order to unzip the ffmpeg zip file which is installed with `setup.py` and if your extra cool, if you add 7-zip to PATH, the ffmpeg zip file will be automatically extracted with `setup.py`.

1. Run `setup.py`
2. Extract ffmpeg.7z with `setup.py` or manually 
3. Navigate to 'Edit the system environment variables ![](https://github.com/Jay-m8/Youtube-MP3-Downloader/blob/41c02578b2c367687d7428249889be771343a772/img/step3.png)
4. In System Properties, go to Advance tab and click `Environment Variables` ![](https://github.com/Jay-m8/Youtube-MP3-Downloader/blob/41c02578b2c367687d7428249889be771343a772/img/step4.png)
5. Go to user variables and click `Path` and click the New button ![](https://github.com/Jay-m8/Youtube-MP3-Downloader/blob/41c02578b2c367687d7428249889be771343a772/img/step5.png)
6. Click new and copy the path to the three main EXE programs from the extracted folder ![](https://github.com/Jay-m8/Youtube-MP3-Downloader/blob/41c02578b2c367687d7428249889be771343a772/img/step6.png)
7. Now open a terminal and type `ffmpeg` and it should look like this ![](https://github.com/Jay-m8/Youtube-MP3-Downloader/blob/41c02578b2c367687d7428249889be771343a772/img/step7.png)

---

<h2> Usage </h2>

Now that everything is installed and pre-configured, you can run `main.py`.

1. Run main.py
2. Paste all the Youtube URLs you want in terminal, seperate URLs with commas and no spaces
3. Select what directory you want the MP3 file/s to be downloaded to
4. Done, type 'quit' once your're finished
