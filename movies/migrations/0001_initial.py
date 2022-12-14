# Generated by Django 4.1.3 on 2022-11-08 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Жанр аты")),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Атау")),
                (
                    "original_title",
                    models.CharField(max_length=255, verbose_name="Түпнұсқа атау"),
                ),
                (
                    "description",
                    models.TextField(max_length=255, verbose_name="Сипаттама"),
                ),
                ("studia", models.CharField(max_length=50, verbose_name="Студия")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Онгоинг"), (1, "Аяқталған")], default=0
                    ),
                ),
                ("prokat", models.DateField(auto_now_add=True, verbose_name="Прокат")),
                ("duration", models.IntegerField(default=24, verbose_name="Уақыты")),
                (
                    "genre",
                    models.ManyToManyField(
                        blank=True, to="movies.genre", verbose_name="Жанр"
                    ),
                ),
            ],
            options={
                "verbose_name": ("Аниме",),
                "verbose_name_plural": ("Анимелер",),
            },
        ),
        migrations.CreateModel(
            name="MovieSeries",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(default=1, verbose_name="Бөлім")),
                (
                    "iframe_link",
                    models.CharField(max_length=255, verbose_name="OK.ru LINK"),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="series",
                        to="movies.movie",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Аниме сериясы",),
                "verbose_name_plural": ("Аниме сериялары",),
            },
        ),
    ]
