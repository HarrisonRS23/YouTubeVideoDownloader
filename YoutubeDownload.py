from pytube import YouTube
from sys import argv

# link = argv[1]  # add link in command line
#yt = YouTube(link)
yt = YouTube('https://www.youtube.com/watch?v=lbzMUiR6MRI')

print("Title: " + yt.title)
print("Description: " + yt.description)
print("Views: " + str(yt.views))
