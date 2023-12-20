# Youtube Video Downloader

This Python script is a simple YouTube video downloader utilizing the customtkinter library for the user interface and the pytube library to access YouTube videos.

## Prerequisites
Before running the script, ensure you have the necessary libraries installed. You can install the required libraries by running:

pip install -r requirements.txt

The requirements.txt file contains the necessary libraries and their versions needed to run the script.

## Running the Script
To run the script, cd into env then execute the script using python3. Upon execution, a graphical user interface (GUI) will appear, prompting you to enter a YouTube video URL and select the desired resolution for downloading.

### cd env/
### python3 app.py

## The following functionalities are included:

Input field to enter the YouTube URL.
Selection of video resolution (1080p, 720p, 360p, 240p).
Download button to start downloading the video.
Progress bar and labels to display download progress and status.

## Usage Notes

The script downloads the video into a 'downloads' folder within the script directory.
The script will create a 'downloads' folder in working directory if none pre-existing.
In case of errors during the download process, the script displays error messages in the status label.
The progress bar indicates the percentage of download completion.
Potential lag when clicking download button. 
Vidoe will not download again and progress bar will not update if video is already downloaded in directory.
