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
	return render_to_response('lyriccheck/lyrics.html', {'artist': artist.replace('+',' '), 'song': song.replace('+',' '), 'lyrics': song_lyrics, 'js_lyrics': js_lyrics,},RequestContext(request))
def formatJSLyrics(lyr):
	lyr=lyr.lower()
	lyr=re.sub('\n+','|',lyr)
	for ch in ['.',',','!',"'",'?']:
		if ch in lyr:
			lyr=lyr.replace(ch,'')
	return lyr[:-1]