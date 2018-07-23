import argparse
import csv
import requests
from urllib2 import urlopen
from bs4 import BeautifulSoup

# Function that reads csv file into list
def readCsv(filename):
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		result = list(reader)
	return result

"""
result = readCsv('test_data.csv')
print(result)
"""

# Make function if given playlist link, it will 
# parse all the video links in the playlist to
# a csv file and/or array

def getPlaylist(url):
	sourceCode = requests.get(url).text
	soup = BeautifulSoup(sourceCode, 'html.parser')
	domain = 'https://wwww.youtube.com'
	for link in soup.find_all("a", {"dir": "1tr"}):
		href = link.get('href')
		if href.startswith('/watch?'):
			print(link.string.strip())
			print(domain + href + '\n')

def getPlaylist2(url):
	pageElements = urlopen(url).readlines()
	vidElements = [el for el in pageElements if 'pl-video-title-link' in el]
	for v in  vidElements:
		vidUrls = v.split('href="',1)[1].split('" ',1)[0]
	return ['http://www.youtube.com' + v for v in vidUrls]


result = getPlaylist3("https://www.youtube.com/playlist?list=PLH22-xSMERQpxPaba5cAkc60zWa3AnPKV")
print(result)