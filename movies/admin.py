from django.contrib import admin
from .models import Movie, MovieSeries, Genre


class MovieSeriesInline(admin.TabularInline):
    model = MovieSeries
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieSeriesInline]


@admin.register(MovieSeries)
class MovieSeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
