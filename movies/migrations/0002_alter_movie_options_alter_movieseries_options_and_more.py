# Generated by Django 4.1.3 on 2022-11-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="movie",
            options={"verbose_name": "Аниме", "verbose_name_plural": "Анимелер"},
        ),
        migrations.AlterModelOptions(
            name="movieseries",
            options={
                "verbose_name": "Аниме сериясы",
                "verbose_name_plural": "Аниме сериялары",
            },
        ),
        migrations.AlterField(
            model_name="movie",
            name="prokat",
            field=models.DateField(verbose_name="Прокат"),
        ),
    ]
