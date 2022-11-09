from django.urls import path
from .views import MovieListView, MovieDetailView, main_page

app_name = "movies"

urlpatterns = [
    path("", main_page, name="main"),
    path("anime/", MovieListView.as_view(), name="movie_list"),
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("<slug:slug>/<int:seriya>/", MovieDetailView.as_view(), name="movie_seriya_detail"),
]