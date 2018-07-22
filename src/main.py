import sys
import os
from utils import downloadVideo, downloadAudio

while True:
	user = raw_input('Do you want to continue? [y/n] ')
	if user.lower() in ['yes', 'y']:
		url = raw_input('Enter content URL: ')
		# link = YouTube(url)
		form = raw_input('Download video or audio? [v/a] ')
		if form.lower() in ['v', 'video']:
			warn = raw_input('Are you sure? [y/n]')
			if warn.lower() in ['y', 'yes']:
				downloadVideo(url)
				print('Download complete')

		elif form.lower() in ['a', 'audio']:
			warn = raw_input('Are you sure? [y/n]')
			if warn.lower() in ['y', 'yes']:
				downloadAudio(url)
				print('Download complete')
	if user.lower() in ['no', 'n']:
		print('Ending session')
		exit()
