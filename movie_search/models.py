# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib
import urllib2
import json
import urlparse  
from django.db import models
from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()

tmdb.api_key = '3ccce087e61d6cabe327758d6d261b3c'

from tmdbv3api import Movie

# Create your models here.
class Movie(models.Model):

	title = models.TextField()


	def getMovieData(self, title):
		#jsonData = urllib.request.urlopen("http://omdbapi.com/?t=%s&y=&tomatoes=true&plot=short&r=json" % title)
		#request = urllib.request.Request("http://omdbapi.com/?t=%s&y=&tomatoes=true&plot=short&r=json" % title)
		#response = urllib.request.urlopen(request)
			title = urllib.quote(title)
			movie = Movie()
			search = movie.search(title)
			self.movieData = {}
			self.movieData['title'] = search[0].title
			self.movieData['year'] = search[0].release_date
			self.movieData['userrating'] = search[0].vote_average
			self.movieData['imdbID'] = search[0].id
			self.movieData['plot'] = search[0].overview
			self.movieData['response'] = 'True'
			self.movieData['posterURL'] = self.generateImageLink(search[0].poster_path)
			return self.movieData

	def generateImageLink(self, imdbid):
			imageURL = 'https://image.tmdb.org/t/p/w500/' + imdbid + '.jpg'
			return imageURL

