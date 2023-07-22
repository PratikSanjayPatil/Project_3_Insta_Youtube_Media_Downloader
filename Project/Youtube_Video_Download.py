from pytube import YouTube

def download_youtube_video(Link, save_path=None):
    try:
        Youtube_Download = YouTube(Link)

        #For Highest Resulation
        stream = Youtube_Download.streams.get_highest_resolution()
        print("Downloading...")


        save_path = save_path or "./"
        stream.download(save_path)

        print("Download complete!")

    except Exception as error:
        print("An error occurred:", str(error))


Link = input("Enter the YouTube video Link: ")
download_youtube_video(Link)
