import pytest
from django.contrib.auth.models import User
from .models import Movie, WatchList, Review, UserInteraction, WatchLogging

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def movie():
    return Movie.objects.create(
        name='Test Movie',
        desc='This is a test movie',
        title_image='https://example.com/testtitleimage.jpg',
        image='https://example.com/testimage.jpg',
        category='Test',
        language='English',
        year=2021,
        time='1h 30min',
        video='https://example.com/testvideo.mp4',
        rate=4,
        review_num=10,
        producer='Test Producer'
    )

@pytest.fixture
def watchlist(user):
    return WatchList.objects.create(
        watchlist_name='Test Watchlist',
        user=user,
        active=True
    )

@pytest.fixture
def review(user, movie):
    return Review.objects.create(
        review_user=user,
        rating=4,
        description='This is a test review',
        movie=movie,
        user_like=True,
        active=True,
        public=True
    )

@pytest.fixture
def user_interaction(user, review):
    return UserInteraction.objects.create(
        user=user,
        review=review,
        comments='This is a test comment',
        user_like=True
    )

@pytest.fixture
def watch_logging(movie):
    return WatchLogging.objects.create(
        movie=movie
    )

@pytest.mark.django_db
def test_movie_str_method(movie):
    assert str(movie) == 'Test Movie'

@pytest.mark.django_db
def test_watchlist_str_method(user, watchlist):
    assert str(watchlist) == f'Test Watchlist | {user}'

@pytest.mark.django_db
def test_review_str_method(user, movie, review):
    assert str(review) == f'4 | Test Movie | {user}'

@pytest.mark.django_db
def test_user_interaction_str_method(user_interaction):
    assert str(user_interaction) == f'{user_interaction.user_id} | {user_interaction.review_id} | This is a test comment'

@pytest.mark.django_db
def test_watch_logging_str_method(movie, watch_logging):
    assert str(watch_logging) == str(movie.id)

@pytest.mark.django_db
def test_movie_fields(movie):
    assert movie.name == 'Test Movie'
    assert movie.desc == 'This is a test movie'
    assert movie.title_image == 'https://example.com/testtitleimage.jpg'
    assert movie.image == 'https://example.com/testimage.jpg'
    assert movie.category == 'Test'
    assert movie.language == 'English'
    assert movie.year == 2021
    assert movie.time == '1h 30min'
    assert movie.video == 'https://example.com/testvideo.mp4'
    assert movie.rate == 4
    assert movie.review_num == 10
    assert movie.producer == 'Test Producer'

@pytest.mark.django_db
def test_watchlist_fields(user, watchlist):
    assert watchlist.watchlist_name == 'Test Watchlist'
    assert watchlist.user == user
    assert watchlist.active == True

@pytest.mark.django_db
def test_review_fields(user, movie, review):
    assert review.review_user == user
    assert review.rating == 4
    assert review.description == 'This is a test review'
    assert review.movie == movie
    assert review.user_like == True
    assert review.active == True
    assert review.public == True

@pytest.mark.django_db
def test_user_interaction_fields(user, review, user_interaction):
    assert user_interaction.user == user
    assert user_interaction.review == review
    assert user_interaction.comments == 'This is a test comment'
    assert user_interaction.user_like == True

@pytest.mark.django_db
def test_watch_logging_fields(movie, watch_logging):
    assert watch_logging.movie == movie