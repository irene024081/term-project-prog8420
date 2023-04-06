from movie_app.models import Movie, Review, WatchList
from rest_framework import generics, viewsets
from movie_app.api.serializers import (MovieSerializer, ReviewSerializer, WatchListSerializer)
from rest_framework.response import Response
from django.contrib.auth.models import User
from movie_app.api.filters import MovieFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MovieVS(viewsets.ModelViewSet):
    """
        POST: create a new movie
        GET: list all movies with /movie/
        GET: get a specific movie with /movie/<pk>
        PUT: update a movie 
        DELETE: delete a movie
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter
    #permission_class = [IsAdminOrReadOnly]
    def list(self, request, *args, **kwargs):
        show_number = 1

        new = request.query_params.get('new')
        featured = request.query_params.get('featured')

        if not new and not featured:
            return super().list(request)
        if new:
            movie_queryset = Movie.objects.all().order_by(('-release_date'))[:show_number]
            serializer = self.get_serializer(movie_queryset, many = True)
            return Response(serializer.data)
        if featured:
            movie_queryset = Movie.objects.all().order_by(('-avg_rating'))[:show_number]
            serializer = self.get_serializer(movie_queryset, many = True)
            return Response(serializer.data)
            
class UserReview(generics.ListCreateAPIView):
    """
        GET: retrieve all movies created by a user
    """
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [ReviewListThrottle]


    def get_queryset(self):
        user = self.request.user
        movie_id = self.kwargs['pk']
        movie = Movie.objects.get(id=movie_id)
        if not user.id:
            return Review.objects.none()
        return Review.objects.filter(movie=movie,review_user=user)

class ReviewList(generics.ListCreateAPIView):
    """
        GET: list all reviews of a specific movie whose id is <pk>
        POST: create new review for a movie whose id is <pk>
    """
    queryset = Review.objects.all()

    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [ReviewListThrottle]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['review_user__username', 'active']
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(movie=pk)
    
    def perform_create(self, serializer):
        movie_id = self.kwargs['pk']
        movie = Movie.objects.get(id=movie_id)
        user = self.request.user
        if user.id:
            serializer.save(movie=movie, review_user = user)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        GET: retrieve a specific review with review id <pk>
        PUT: update a specific review with review id <pk>
        DELETE: update a specific review with review id <pk>
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsReviewUserOrReadOnly]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'review_detail'
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(id=pk)


class UserWatchList(generics.ListCreateAPIView):
    """
        GET: retrieve all watchlists created by a user whose username is <username>
        POST: create new watchlist by a user whose username is <username>
    """
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [ReviewListThrottle]

    def get_queryset(self):
        user = self.request.user
        if not user.id:
            return WatchList.objects.none()
        return WatchList.objects.filter(user=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.id:
            serializer.save(user.user)

    
class WatchListDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        GET: retrieve a specific watchlist with watchlist id <pk>
        PUT: update a specific watchlist with watchlist id <pk>
        DELETE: delete a specific watchlist with watchlist id <pk>
    """
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    # permission_classes = [IsReviewUserOrReadOnly]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'review_detail'


