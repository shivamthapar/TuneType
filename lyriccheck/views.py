# coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import LyricFetcher
import re

def index(request):
	title= "String check"
	return render_to_response('lyriccheck/index.html', {'title': title},RequestContext(request))
def lyrics(request, artist, song):
	artist= artist.replace('+',' ')
	song= song.replace('+',' ')
	song_lyrics= LyricFetcher.scrape_lyrics(artist,song)
	song_lyrics=re.sub("’","'",song_lyrics)
	js_lyrics=formatJSLyrics(song_lyrics)
	video=getVideo(artist,song)
	return render_to_response('lyriccheck/lyrics.html', {'artist': artist.replace('+',' '), 'song': song.replace('+',' '), 'lyrics': formatLyrics(song_lyrics), 'js_lyrics': js_lyrics, 'video_id': getVideoId(video), 'video':video.GetSwfUrl(),},RequestContext(request))
def formatJSLyrics(lyr):
	lyr=lyr.lower()
	lyr=re.sub('\n+','|',lyr)
	for ch in ['.',',','!',"'",'?']:
		if ch in lyr:
			lyr=lyr.replace(ch,'')
	return lyr[:-1]
def formatLyrics(lyr):
	lyr=re.sub('\n+','|',lyr)
	return lyr[:-1]
def getVideo(artist, song):
	try:
		import gdata.youtube
		import gdata.youtube.service

		yt_service = gdata.youtube.service.YouTubeService()
		search_terms= song+" "+artist+" official music video"

		# Turn on HTTPS/SSL access.
		# Note: SSL is not available at this time for uploads.
		yt_service.ssl = True
		yt_service.developer_key = 'AI39si7JIjRfBh_5-WURCpWRmNJU5BgGzKVfUjICv1ZYaxzt5b0gs14loDF3S4wwrsWcy0PBsFjgo17SmTDa65lVEjcmwo6iMg'
		query = gdata.youtube.service.YouTubeVideoQuery()
		query.vq = search_terms
		query.orderby = 'relevance'
		query.racy = 'include'
		feed = yt_service.YouTubeQuery(query)
		return feed.entry[0]
	except:
		pass

def getVideoId(vid):
	url=vid.GetSwfUrl()
	video_id = url.split('v/')[1]
	ampersandPosition = video_id.index('&')
	if ampersandPosition != -1:
	  video_id = video_id[:ampersandPosition]
	return video_id
