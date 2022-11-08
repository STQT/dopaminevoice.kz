from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name="Жанр аты")

    def __str__(self):
        return self.title


class Movie(models.Model):
    status_choices = (
        (0, "Онгоинг"),
        (1, "Аяқталған")
    )
    img = models.ImageField(verbose_name="Сурет")
    title = models.CharField(max_length=255, verbose_name="Атау")
    original_title = models.CharField(max_length=255, verbose_name="Түпнұсқа атау")
    description = models.TextField(max_length=255, verbose_name="Сипаттама")
    studia = models.CharField(max_length=50, verbose_name="Студия")
    status = models.IntegerField(choices=status_choices, default=0)
    genre = models.ManyToManyField(Genre, blank=True, verbose_name="Жанр")
    prokat = models.DateField(verbose_name="Прокат")
    duration = models.IntegerField(default=24, verbose_name="Уақыты")
    max_series = models.IntegerField(default=12, verbose_name="Жалпы бөлім саны")
    url = models.SlugField(max_length=130, unique=True)

    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"slug": self.url})

    def get_series_url(self):
        return reverse("movies:movie_series_detail", kwargs={"slug": self.series.number})

    class Meta:
        verbose_name = _("Аниме")
        verbose_name_plural = _("Анимелер")

    def __str__(self):
        return self.title


class MovieSeries(models.Model):
    movie = models.ForeignKey(Movie, related_name="series", on_delete=models.CASCADE)
    number = models.IntegerField(default=1, verbose_name="Бөлім")
    iframe_link = models.CharField(verbose_name="OK.ru LINK",
                                   max_length=255)

    def get_absolute_url(self):
        return reverse("movies:movie_seriya_detail", kwargs={"slug": self.number})

    class Meta:
        verbose_name = _("Аниме сериясы")
        verbose_name_plural = _("Аниме сериялары")
