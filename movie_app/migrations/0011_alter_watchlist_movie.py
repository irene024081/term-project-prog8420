# Generated by Django 4.1.7 on 2023-04-05 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='movie',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='movie_app.movie'),
        ),
    ]
