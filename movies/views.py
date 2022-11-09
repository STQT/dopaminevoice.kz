from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object() # noqa
        context = self.get_context_data(object=self.object)
        if kwargs.get('seriya') is None:
            self.kwargs['seriya'] = self.object.series.order_by('number').first().number
        if not self.object.series.all():
            context["episode"] = dict()
            context["many"] = False
        else:
            context["episode"] = self.object.series.all()
            context["many"] = True
        return self.render_to_response(context)

