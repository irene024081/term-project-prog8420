from django.urls import path, include
from movie_app.api.views import (  MovieVS, UserReview, 
                                 ReviewList, ReviewDetail, 
                                 UserWatchList, WatchListDetail)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MovieVS, basename='movie')
urlpatterns = [
    path('watchlists/', UserWatchList.as_view(), name='user_watchlists'),
    path('<int:pk>/review/', UserReview.as_view(), name='user_review_details'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name = 'review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_details'),
    path('watchlist/<int:pk>/', WatchListDetail.as_view(), name='watchlist_details'),
    path('',include(router.urls)),



    #path('', MovieDetail.as_view(), name = 'movie_details'),
    #path('list/', MovieDetail.as_view(), name = 'watch_list')
    
]
