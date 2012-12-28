import json, urllib, os, hashlib, time
from bs4 import BeautifulSoup
import re

def _download(args):
    """
        Downloads the json response and returns it
    """
    base = "http://lyrics.wikia.com/api.php?"
    args = urllib.urlencode(args)
    text= _json_formatting(urllib.urlopen(base + args).read())
    return text

def _json_formatting(json):
	json = json[7:]
	json= json.replace("'", '"')
	return json

def _get_lyrics(artist, title):
    args = {
        "artist": artist,
        "song": title,
		"fmt": "json",
    }
    text= json.loads(_download(args))
    return text

def scrape_lyrics(artist, title):
	lyr_json= _get_lyrics(artist, title)
	text= urllib.urlopen(lyr_json["url"]).read()
	soup=BeautifulSoup(text)
	box=soup.find("div", { "class" : "lyricbox" })
	divs=box.find_all("div")
	divs=divs+box.find_all("a")+box.find_all("sup")
	content=str(box)
	for div in divs:
		content= content.replace(str(div), '')
	content=re.sub('\<![ \r\n\t]*(--([^\-]|[\r\n]|-[^\-])*--[ \r\n\t]*)\>', '\n', content)
	content=re.sub('<br/>','\n', content)
	content=re.sub('<[^>]*>', '', content)
	return content
	#print soup.prettify()