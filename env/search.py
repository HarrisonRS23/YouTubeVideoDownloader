import functools
import customtkinter as ctk  # custom tkinter library for visuals
from tkinter import ttk
from pytube import YouTube  # library to access youtube videos
from pytube import Search
import os  # place files in system


def search_video():
    searchButton.configure(state=ctk.DISABLED)
    title = userSearch.get()
    s = Search(title)
    count = 0
    for v in s.results:
        if count < 6:
            show_search_results(v)
            count += 1
        else:
            break  # Exit loop once 6 iterations are done


def show_search_results(yt):

    print(yt)
    download_func = functools.partial(download_video, yt=yt)  # Create a function with the fixed 'yt' argument
    videoButton = ctk.CTkButton(
        content_frame,
        text=yt.title,
        command=download_func  # Pass the function to the button command
    )
    videoButton.pack(pady=("10p", "5p"))
    print(yt.title)


def download_video(yt):
    # create results button
    stream = yt.streams.get_highest_resolution()
    os.path.join("downloads", f"{yt.title}.mp4")  # download video into downloads folder with video title
    stream.download(output_path="downloads")
    print("downloading...")


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
searchLabel = ctk.CTkLabel(content_frame, text="Search for a Youtube Video Here: ")
userSearch = ctk.CTkEntry(content_frame, width=400, height=40)
searchLabel.pack(pady=("10p", "5p"))
userSearch.pack(pady=("10p", "5p"))

# create search button
searchButton = ctk.CTkButton(content_frame, text="Search", command=search_video)
searchButton.pack(pady=("10p", "5p"))

# create a status label for when downloaded
statusLabel = ctk.CTkLabel(content_frame, text="")
# statusLabel.pack(pady=("10p", "5p"))

# to start the app
root.mainloop()
