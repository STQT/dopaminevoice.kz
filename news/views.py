from django.views.generic import DetailView, ListView
from .models import News


class NewsListView(ListView):
    model = News


class NewsDetailView(DetailView):
    model = News
    slug_field = 'slug'
