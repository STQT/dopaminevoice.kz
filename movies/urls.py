from django.urls import path
from .views import MovieListView, MovieDetailView, main_page, dislike, like

app_name = "movies"

urlpatterns = [
    path("", main_page, name="main"),
    path("anime/", MovieListView.as_view(), name="movie_list"),
    path("like_comment/<int:comment_id>/", like, name="like_comment"),
    path("dislike_comment/<int:comment_id>/", dislike, name="dislike_comment"),
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("<slug:slug>/<int:seriya>/", MovieDetailView.as_view(), name="movie_seriya_detail"),
]
