from pytube import YouTube


def download_video(url):
	yt = YouTube(url)
	video = yt.streams.get_highest_resolution()
	video.download("C:/Users/Carlos Silva/Downloads")

if __name__ == '__main__':
	download_video()