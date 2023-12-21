import functools
import customtkinter as ctk  # custom tkinter library for visuals
from tkinter import ttk
from pytube import YouTube  # library to access youtube videos
from pytube import Search
import os  # place files in system

def download_video():
    downloadButton.configure(state=ctk.DISABLED)
    url = userUrl.get()
    resolution = resolutionVar.get()

    progressLabel.pack(pady=("10p", "5p"))
    progressBar.pack(pady=("10p", "5p"))
    statusLabel.pack(pady=("10p", "5p"))

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()  # only fetch video from url if valid
        # download video into a specific place
        os.path.join("downloads", f"{yt.title}.mp4")  # download video into downloads folder with video title
        stream.download(output_path="downloads")
        statusLabel.configure(text="Downloaded", text_color="white", fg_color="green")

    except Exception as e:
        statusLabel.configure(text=f"Error {str(e)}", text_color="white", fg_color="red")
    downloadButton.configure(state=ctk.NORMAL)


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = (bytes_downloaded / total_size) * 100
    print(f"{percent_completed}% complete")

    progressLabel.configure(text=str(int(percent_completed)) + "%")
    progressLabel.update()
    progressBar.set(float(percent_completed) / 100)


def construct_screen():



    # create a label and the entry widget for the video url
    urlLabel = ctk.CTkLabel(content_frame, text="Enter the Youtube Url Here: ")
    userUrl = ctk.CTkEntry(content_frame, width=400, height=40)
    urlLabel.pack(pady=("10p", "5p"))
    userUrl.pack(pady=("10p", "5p"))

    # create download button
    downloadButton = ctk.CTkButton(content_frame, text="Download", command=download_video)
    downloadButton.pack(pady=("10p", "5p"))

    # create a resolution selector box
    resolutionList = ["1440p", "1080p", "720p", "360p", "240p"]
    resolutionVar = ctk.StringVar()
    # assign selected value to resolution variable
    resolutionComboBox = ttk.Combobox(content_frame, values=resolutionList, textvariable=resolutionVar)
    resolutionComboBox.pack(pady=("10p", "5p"))
    resolutionComboBox.set("720p")

    # create progress label
    progressLabel = ctk.CTkLabel(content_frame, text="0%")
    # progressLabel.pack(pady=("10p", "5p"))

    # create progress bar to show download progress
    progressBar = ctk.CTkProgressBar(content_frame, width=400)
    progressBar.set(0)
    # progressBar.pack(pady=("10p", "5p"))

    # create a status label for when downloaded
    statusLabel = ctk.CTkLabel(content_frame, text="")
    # statusLabel.pack(pady=("10p", "5p"))


# create root window
root = ctk.CTk()

ctk.set_appearance_mode("Dark")  # set to dark mode
ctk.set_default_color_theme("dark-blue")  # set color them to red

# title of window
root.title("Youtube Downloader")

# restrict minimize and maximize size
root.geometry("720x480")
root.minsize(width=720, height=480)
root.maxsize(width=1080, height=720)

# create frame to hold content
content_frame = ctk.CTkFrame(root)  # mount frame onto root
content_frame.pack(fill="both", expand=True, padx=10, pady=10)  # fill the entire root

# to start the app
root.mainloop()
