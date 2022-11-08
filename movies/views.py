from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieSeries, Genre


class MovieListView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"


class MovieSeriesDetail(DetailView):
    model = Movie
    slug_field = "series__number"
