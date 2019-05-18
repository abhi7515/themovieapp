# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
from .models import Movie

# Create your views here.
def results(request):
	m = Movie()
	if request.GET.get('q') is not None:
		searchname = request.GET.get('q')
		movieData = m.getMovieData(searchname)
		return render(request, "movie_search/home.html", {'movieData': movieData, 'search1': True})
	else:
		return render(request, "movie_search/home.html")