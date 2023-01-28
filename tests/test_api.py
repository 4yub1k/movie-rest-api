# import pytest


# Movie model test
def test_movie(movie_factory):
    movie = movie_factory.build()
    print(movie.Title[0])           # ('Oscar',)[0] -> 'Oscar'

    assert movie.Title[0] == 'Oscar'
    assert movie.id[0] == 1


# Comment model test
def test_comment(comment_factory):
    comment = comment_factory.build()
    print(comment.movie_id.id[0])
    print(comment.movie_id.Title[0])
    print(comment.comment)

    assert comment.movie_id.id[0] == 1
    assert comment.comment == "excellent movie"
