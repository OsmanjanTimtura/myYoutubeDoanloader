from pytube import YouTube

#Paste the link of the video that needs to be downloaded
videoURL = "youtube link for the video"
#Youtube object is created
myYoutube = YouTube(videoURL)
#Get the highest resolution stream
stream = myYoutube.streams.get_highest_resolution()
#Where do you want to save the video
videoDownloadPath = "path to the storage folder"
#download the video
stream.download(videoDownloadPath)
#printing a message after completion!
print("Video downloaded!")