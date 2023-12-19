import customtkinter as ctk  # custom tkinter library for visuals
from tkinter import ttk
from pytube import YouTube  # library to access youtube videos
import os  # place files in system


def download_video():
    print("Downloading...")


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

# create a label and the entry widget for the video url
urlLabel = ctk.CTkLabel(content_frame, text="Enter the Youtube Url Here: ")
userUrl = ctk.CTkEntry(content_frame, width=400, height=40)
urlLabel.pack(pady=("10p", "5p"))
userUrl.pack(pady=("10p", "5p"))

# create download button
downloadButton = ctk.CTkButton(content_frame, text="Download", command=download_video)
downloadButton.pack(pady=("10p", "5p"))

# create a resolution selector box
resolutionList = ["1080px", "720px", "360px", "240px"]
resolutionVar = ctk.StringVar()
# assign selected value to resolution variable
resolutionComboBox = ttk.Combobox(content_frame, values=resolutionList, textvariable=resolutionVar)
resolutionComboBox.pack(pady=("10p", "5p"))
resolutionComboBox.set("720px")

# create progress label
progressLabel = ctk.CTkLabel(content_frame, text="0%")
# progressLabel.pack(pady=("10p", "5p"))

# create progress bar to show download progress
progressBar = ctk.CTkProgressBar(content_frame, width=400)
progressBar.set(0.6)
# progressBar.pack(pady=("10p", "5p"))

# create a status label for when downloaded
statusLabel = ctk.CTkLabel(content_frame, text="Downloaded")
# statusLabel.pack(pady=("10p", "5p"))

# to start the app
root.mainloop()
