# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
# make movie models

class Movie(models.Model):
	actor = models.CharField(max_length=30)
	actor_movies = models.CharField(max_length=50)
	genre = models.CharField(max_length=50)
	movie_logo = models.CharField(max_length=100)

	def __str__(self):
		return self.actor


class Song(models.Model):
	movie = models.ForeignKey(Movie, on_delete =models.CASCADE)
	file_type = models.CharField(max_length=50)
	song_name = models.CharField(max_length=100)

	def __str__(self):
		return self.song_name

class Singer(models.Model):
	movie = models.ForeignKey(Movie, on_delete =models.CASCADE)
	song = models.ForeignKey(Song, on_delete =models.CASCADE)
	name = models.CharField(max_length=100)
	city = models.CharField(max_length=200)

	def __str__(self):
		return self.name




		

