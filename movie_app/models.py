from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Movie(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    title_image = models.URLField(null = True, blank=True)
    image = models.URLField(null = True, blank=True)
    category = models.CharField(max_length=300)
    language = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    video = models.URLField(max_length=500, null = True, blank=True)
    rate = models.FloatField(default= 0)
    review_num = models.IntegerField(default= 0)
    producer = models.CharField(max_length=200)    
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    watchlist_name = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    movie = models.ManyToManyField(Movie, related_name="watchlist")
    def __str__(self) -> str:
        return str(self.watchlist_name)  + " | " + str(self.user)
    

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews_movie")
    user_like = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default= True) # if not valid review manually turn off
    public = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.rating) + " | " + str(self.movie.movie_name) + " | " + str(self.review_user)

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500)
    user_like = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.user_id)  + " | " + str(self.review_id) + " | " + str(self.comments)

class WatchLogging(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.movie_id)
    