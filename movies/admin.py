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
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # if db_field.name == "cars":
        kwargs["queryset"] = MovieComments.objects.filter(author=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        # if db_field.name == "status":
        kwargs['choices'] = (
            ('accepted', 'Accepted'),
            ('denied', 'Denied'),
        )
        if request.user.is_superuser:
            kwargs['choices'] += (('ready', 'Ready for deployment'),)
        return super().formfield_for_choice_field(db_field, request, **kwargs)