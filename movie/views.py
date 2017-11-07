# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie , Song ,Singer

# Create your views here.

def index(request):
	all_Movie =Movie.objects.all()
	for a in all_Movie:
		print a
		url = str(a.id)+'/'
		Html = '<a href="'+url+'">'+a.actor+'</a>'  
		return HttpResponse(Html)

def detail(request, movie_id):
	return HttpResponse("<h1>Welcome in id :"+str(movie_id)+"</h1>")
