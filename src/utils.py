from pytube import YouTube

def downloadVideo(url):
	link = YouTube(url)
	download_video = link.streams.first()
	print('Download Started!')
	return download_video.download()

def downloadAudio(url):
	link = YouTube(url)
	download_audio = link.streams.filter(only_audio=True).first()
	print('Download Started!')
	return download_audio.download('audio/')
