from rest_framework import serializers
from movie_app.models import Movie, Review, WatchList



class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    #watchlist = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ['movie']

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only = True)
    # platform = serializers.CharField(source='platform.name')
    class Meta:
        model = Movie
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"
