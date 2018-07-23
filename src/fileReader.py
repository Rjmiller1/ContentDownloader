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
    domain = 'https://www.youtube.com'
    result = ''
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            # print(link.string.strip())
            result += domain + href + '\n'
    return result

result = getPlaylist("https://www.youtube.com/playlist?list=PLH22-xSMERQpxPaba5cAkc60zWa3AnPKV")
print(result)