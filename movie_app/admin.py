from django.contrib import admin
from movie_app.models import Movie, Review, WatchList


# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(WatchList)