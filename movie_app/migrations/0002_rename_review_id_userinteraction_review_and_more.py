# Generated by Django 4.1.7 on 2023-03-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinteraction',
            old_name='review_id',
            new_name='review',
        ),
        migrations.RenameField(
            model_name='userinteraction',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='watchlogging',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='watchlist_id',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='movie',
            field=models.ManyToManyField(related_name='watchlist', to='movie_app.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_like',
            field=models.BooleanField(default=False),
        ),
    ]