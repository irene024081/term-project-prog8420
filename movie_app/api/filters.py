from django_filters import rest_framework as filters
from movie_app.models import Movie, Review, WatchList


class MovieFilter(filters.FilterSet):
    start_year = filters.NumberFilter(field_name="release_date", lookup_expr='year__gte')
    end_year = filters.NumberFilter(field_name="release_date", lookup_expr='year__lte')
    category = filters.CharFilter(field_name="movie_category", lookup_expr='iexact')
    start_rating = filters.NumberFilter(field_name="avg_rating", lookup_expr='gte')
    end_rating = filters.NumberFilter(field_name="avg_rating", lookup_expr='lte')
    producer = filters.CharFilter(field_name="producer", lookup_expr='iexact')
    name_contains = filters.CharFilter(field_name="movie_name",lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['release_date','movie_category','avg_rating','producer','movie_name']