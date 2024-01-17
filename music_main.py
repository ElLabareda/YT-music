from pytube import YouTube


def download_audio(url):
	yt = YouTube(url)
	audio = yt.streams.filter(only_audio=True)[0]
	audio.download("C:/Users/Carlos Silva/Downloads")

if __name__ == '__main__':
	download_audio()