# coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import re

def index(request):
	title= "String check"
	return render_to_response('tunetype/index.html', {'title': title},RequestContext(request))