from django.urls import path
from .views import MovieListView, MovieDetailView, MovieSeriesDetail

app_name = "movies"

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list"),
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("series/<slug:slug>/", MovieSeriesDetail.as_view(), name="movie_seriya_detail"),
]