from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Movie, MovieComments, MovieSeries
from .forms import MovieCommentsForm
User = get_user_model()


def main_page(request):
    qs = Movie.objects.all()
    banner = Movie.objects.filter(url="chainsawman").first()
    ctx = {"anime": qs, "banner": banner}
    return render(request, 'index.html', ctx)


class MovieListView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data()
        series = self.object.series.select_related("movie")
        if self.kwargs.get('seriya') is None:
            first_episode = series.order_by('number').first()
            if first_episode:
                self.kwargs['seriya'] = first_episode.number
        ctx["current_episode"] = series.filter(number=self.kwargs['seriya']).first()
        if not series:
            ctx["episode"] = dict()
            ctx["many"] = False
        else:
            ctx["episode"] = series
            ctx["many"] = True
        _list = MovieComments.objects.filter(
            episode=self.kwargs['seriya']
        ).order_by("-created_at").select_related("author").prefetch_related("user_likes", "user_dislikes")
        paginator = Paginator(_list, 2)
        page = self.request.GET.get('page')
        ctx['comments'] = paginator.get_page(page)
        ctx['form'] = MovieCommentsForm()
        return ctx

    def post(self, request, *args, **kwargs):
        if isinstance(request.user.id, int) is False:
            return HttpResponseRedirect(reverse("movies:main"))
        user = User.objects.filter(pk=request.user.id).first()
        episode = get_object_or_404(MovieSeries, pk=kwargs.get("seriya"))
        form = MovieCommentsForm(request.POST)
        if form.is_valid():
            MovieComments.objects.create(comment=form.data.get('comment'), episode=episode, author=user)
            return HttpResponseRedirect(reverse("movies:movie_detail", kwargs={"slug": episode.movie.url}))
        return HttpResponseRedirect(reverse("movies:movie_detail", kwargs={"slug": episode.movie.url}))


def like(request, comment_id, *args, **kwargs):
    comment = get_object_or_404(MovieComments, pk=comment_id)  # noqa
    if request.method == "POST":
        user = User.objects.filter(username=request.user.username).first()
        if comment.user_dislikes.filter(pk=user.pk).count() > 0:
            comment.user_dislikes.remove(user)
        if comment.user_likes.filter(pk=user.pk).count() > 0:
            comment.user_likes.remove(user)
        else:
            comment.user_likes.add(user)
    else:
        return HttpResponseRedirect(reverse("movies:main"))
    return HttpResponseRedirect(reverse("movies:movie_detail", kwargs={"slug": comment.episode.movie.url}))


def dislike(request, comment_id, *args, **kwargs):
    comment = get_object_or_404(MovieComments, pk=comment_id)  # noqa
    if request.method == "POST":
        user = User.objects.filter(username=request.user.username).first()
        if comment.user_likes.filter(pk=user.pk).count() > 0:
            comment.user_likes.remove(user)
        if comment.user_dislikes.filter(pk=user.pk).count() > 0:
            comment.user_dislikes.remove(user)
        else:
            comment.user_dislikes.add(user)
    else:
        return HttpResponseRedirect(reverse("movies:main"))
    return HttpResponseRedirect(reverse("movies:movie_detail", args={"slug": comment.episode.movie.url}))


# def add_comment(request, episode_id, *args, **kwargs):
#     episode = get_object_or_404(MovieSeries, pk=episode_id)  # noqa
#     if request.method == "POST":
#         if isinstance(request.user.id, int) is False:
#             return HttpResponseRedirect(reverse("movies:main"))
#         user = User.objects.filter(pk=request.user.id).first()
#         form = MovieCommentsForm(request.POST)
#         if form.is_valid():
#             MovieComments.objects.create(comment=form.data.get('comment'), episode=episode, author=user)
#             return HttpResponseRedirect(reverse("movies:movie_detail", kwargs={"slug": episode.movie.url}))
#         return HttpResponseRedirect(reverse("movies:movie_detail", kwargs={"slug": episode.movie.url}))
#     else:
#         form = MovieCommentsForm()
#         return render(request, 'test.html', {'form': form})
