# Generated by Django 4.1.7 on 2023-03-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_rename_reviews_movie_review_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
