# Generated by Django 4.1.7 on 2023-03-26 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_rename_movie_category_movie_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='reviews',
            new_name='review_num',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='titleImage',
            new_name='title_image',
        ),
    ]
