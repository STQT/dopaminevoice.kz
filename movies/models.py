from admin_async_upload.models import AsyncFileField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup

User = get_user_model()


class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name="Жанр аты")

    def __str__(self):
        return self.title


class Movie(models.Model):
    status_choices = (
        (0, "Онгоинг"),
        (1, "Аяқталған")
    )
    img = models.ImageField(verbose_name="Сурет", upload_to="anime/%y/%m/%d")
    title = models.CharField(max_length=255, verbose_name="Атау")
    original_title = models.CharField(max_length=255, verbose_name="Түпнұсқа атау")
    description = models.TextField(verbose_name="Сипаттама")
    studia = models.CharField(max_length=50, verbose_name="Студия")
    status = models.IntegerField(choices=status_choices, default=0)
    genre = models.ManyToManyField(Genre, blank=True, verbose_name="Жанр")
    prokat = models.DateField(verbose_name="Прокат")
    duration = models.IntegerField(default=24, verbose_name="Уақыты")
    max_series = models.IntegerField(default=12, verbose_name="Жалпы бөлім саны")
    url = models.SlugField(max_length=130, unique=True)
    continued = models.BooleanField(default=True, verbose_name="Жалғасуда")
    full_length = models.BooleanField(default=False, verbose_name="Фильм")
    landscape_photo = models.ImageField(upload_to="anime/%y/%m/%d",
                                        verbose_name="Пейзаждық фото",
                                        default="landscape_photo.jpg")
    banner = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = _("Аниме")
        verbose_name_plural = _("Анимелер")

    def __str__(self):
        return self.title


class MovieSeries(models.Model):
    movie = models.ForeignKey(Movie, related_name="series", on_delete=models.CASCADE)
    number = models.IntegerField(default=1, verbose_name="Бөлім")
    iframe_link = models.CharField(verbose_name="OK.ru LINK",
                                   max_length=255, blank=True, null=True)
    video_file = AsyncFileField(null=True, blank=True)

    def get_episode_url(self):
        return reverse('movies:movie_seriya_detail', kwargs={"slug": self.movie.url, "seriya": self.number})

    class Meta:
        verbose_name = _("Аниме сериясы")
        verbose_name_plural = _("Аниме сериялары")

    def __str__(self):
        return "{} | Қисм: {} | {}".format(self.id, self.number, self.movie.title)

    def clean(self):
        if self.iframe_link:
            soup = BeautifulSoup(self.iframe_link, 'html.parser')
            if soup.find('iframe'):
                try:
                    self.iframe_link = soup.find('iframe')['src']
                except KeyError:
                    raise ValidationError(_("iframe ссылкасынде src деген тэг жоқ"))

            elif soup.text.find('//') != -1:
                pass
            else:
                raise ValidationError(_("iframe_link қате жаздіңіз"))
        super().clean()


class MovieComments(models.Model):
    episode = models.ForeignKey(MovieSeries, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user_likes = models.ManyToManyField(User, related_name="user_likes", blank=True)
    user_dislikes = models.ManyToManyField(User, related_name="user_dislikes", blank=True)

    class Meta:
        verbose_name = _("Пікір")
        verbose_name_plural = _("Пікірлер")

    def __str__(self):
        return "{} | {} | {} ".format(self.episode.movie.title, self.episode.number, self.author.get_short_name())
