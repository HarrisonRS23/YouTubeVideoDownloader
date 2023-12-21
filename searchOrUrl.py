import subprocess
import customtkinter as ctk  # custom tkinter library for visuals
from tkinter import ttk


def start_url():
    # Call the script for URL functionality
    subprocess.run(["python3", "env/app.py"])


def start_search():
    # Call the script for search functionality
    subprocess.run(["python3", "env/search.py"])


# create root window
root = ctk.CTk()

ctk.set_appearance_mode("Dark")  # set to dark mode
ctk.set_default_color_theme("dark-blue")  # set color them to red

# title of window
root.title("Youtube Downloader")

# create small screen
root.geometry("320x280")

# create frame to hold content
content_frame = ctk.CTkFrame(root)  # mount frame onto root
content_frame.pack(fill="both", expand=True, padx=10, pady=10)  # fill the entire root

# create a label and the entry widget for the video url
urlLabel = ctk.CTkLabel(content_frame, text="Select either url or search to download video: ")
urlLabel.pack(pady=("10p", "5p"))

# create search button
downloadButton = ctk.CTkButton(content_frame, text="URL", command=start_url)
downloadButton.pack(pady=("10p", "5p"))
# create url button
downloadButton = ctk.CTkButton(content_frame, text="Search", command=start_search)
downloadButton.pack(pady=("10p", "5p"))

# to start the app
root.mainloop()
