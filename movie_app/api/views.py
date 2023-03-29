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
        username = self.kwargs['username']
        return Review.objects.filter(review_user__username=username)

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


class UserWatchList(generics.ListCreateAPIView):
    """
        GET: retrieve all watchlists created by a user whose username is <username>
        POST: create new watchlist by a user whose username is <username>
    """
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [ReviewListThrottle]

    def get_queryset(self):
        username = self.kwargs['username']
        return WatchList.objects.filter(user__username=username)
    
    def perform_create(self, serializer):
        # self.request.user
        # username = self.kwargs['username']
        # user = User.objects.get(username = username)
 
        serializer.save(user=self.request.user)

    
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


