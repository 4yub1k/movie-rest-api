import factory
from api.models import Movie, Comment


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    # Default parameters:
    id = 1,
    Title = "Oscar",
    Year = "1991",
    Rated = "PG",
    Released = "26 Apr 1991",
    Runtime = "109 min",
    Genre = "Comedy, Crime",
    Director = "John Landis",


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    movie_id = factory.SubFactory(MovieFactory)   # Foreign Key
    comment = "excellent movie"
