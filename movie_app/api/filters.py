from django_filters import rest_framework as filters
from movie_app.models import Movie, Review, WatchList


class MovieFilter(filters.FilterSet):
    start_year = filters.NumberFilter(field_name="year", lookup_expr='year__gte')
    end_year = filters.NumberFilter(field_name="year", lookup_expr='year__lte')
    category = filters.CharFilter(field_name="category", lookup_expr='iexact')
    start_rating = filters.NumberFilter(field_name="rate", lookup_expr='gte')
    end_rating = filters.NumberFilter(field_name="rate", lookup_expr='lte')
    producer = filters.CharFilter(field_name="producer", lookup_expr='iexact')
    name_contains = filters.CharFilter(field_name="name",lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['year','category','rate','producer','name']