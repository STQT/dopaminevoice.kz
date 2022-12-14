# Generated by Django 4.1.3 on 2022-11-11 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0008_movie_full_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="MovieComments",
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
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("likes", models.PositiveIntegerField(default=0)),
                ("dislikes", models.PositiveIntegerField(default=0)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="movies.movie",
                    ),
                ),
                (
                    "user_dislikes",
                    models.ManyToManyField(
                        related_name="user_dislikes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user_likes",
                    models.ManyToManyField(
                        related_name="user_likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "??????????",
                "verbose_name_plural": "????????????????",
            },
        ),
    ]
