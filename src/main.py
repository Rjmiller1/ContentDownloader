import sys
import os
from pytube import YouTube

while True:
	user = raw_input('Do you want to continue? [y/n] ')
	if user.lower() in ['yes', 'y']:
		url = raw_input('Enter content URL: ')
		link = YouTube(url)
		form = raw_input('Download video or audio? [v/a] ')
		if form.lower() in ['v', 'video']:
			warn = input('Are you sure? [y/n]')
			if warn.lower() in ['y', 'yes']:
				download_video = link.streams.first()
				# Look to put in progress bar
				print('Download Started!')
				download_video.download()

		elif form.lower() in ['a', 'audio']:
			warn = input('Are you sure? [y/n]')
			if warn.lower() in ['y', 'yes']:
				download_audio = link.streams.filter(only_audio=True).first()
				print('Download Started!')
				download_audio.download('audio/')
	if user.lower() in ['no', 'n']:
		print('Ending session')
		exit()
