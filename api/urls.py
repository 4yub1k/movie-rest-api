from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('api/',views.list_movies, name='list_movies'),
    path('movie/<str:mv>',views.movie, name='movie'),
    path('comment/<int:id>',views.comment, name='comment'),
    path('comment/movie/<str:mv>',views.movie_comment, name='movie_comment'),
    path('comment/',views.all_comment, name='comments'),
]
