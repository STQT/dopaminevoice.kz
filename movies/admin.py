from django.contrib import admin
from .models import Movie, MovieSeries, Genre, MovieComments


class MovieSeriesInline(admin.TabularInline):
    model = MovieSeries
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieSeriesInline]
    raw_id_fields = ["genre"]


@admin.register(MovieSeries)
class MovieSeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieComments)
class MovieCommentsAdmin(admin.ModelAdmin):
    pass
