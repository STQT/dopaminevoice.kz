# Generated by Django 4.1.3 on 2022-11-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="slug",
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
