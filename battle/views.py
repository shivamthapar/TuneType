# coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from training import views as training

def lyrics(request, artist, song):
	result=training.getVideoAndLyrics(artist,song)
	return render_to_response('battle/lyrics.html', result,RequestContext(request))