from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.movie, name="movie"),
    path("comment/", views.comment, name="comment"),
]
