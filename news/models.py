from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

from movies.models import Movie

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Аты")
    description = RichTextUploadingField(verbose_name="Тақырыбы")
    author = models.ForeignKey(User, related_name="news", on_delete=models.CASCADE, verbose_name="Авторы")
    poster = models.ImageField(upload_to="news/%y/%m/%d", verbose_name="Сурет")
    anime = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, blank=True,
                              verbose_name="Аниме ушын сылтеме")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Жаңалық"
        verbose_name_plural = "Жаңалықтар"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:news_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
