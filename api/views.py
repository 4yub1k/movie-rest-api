from django.shortcuts import render,HttpResponse
from django.http import JsonResponse #FOR JSON response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer,CommentSerializer
from api.models import Movie
from rest_framework import status
from django.shortcuts import get_object_or_404 #USE WITH model.objects.get()
import requests # best way it to, import only get method from requests as it is only used here, or use urllib

"""
FOR HIGH TRAFFIC SITE : I PREFER asyncio or concurrent.futures
"""

"""
FOR:    path('',views.index, name='index'), #redirect to main page
"""
def index(request):
    return render(request,'main.html')

###################################### -API- ######################################################

"""
FOR:    path('api/',views.list_movies, name='list_movies'),
"""
@api_view(['GET'])
def list_movies(request):
    if request.method == 'GET':# THIS LINE IS NOT NEEDED, IT ONLY MAKE THINGS CLEAR
        movies=Movie.objects.all()
        movie_serializer=MovieSerializer(movies, many=True)
        return Response(movie_serializer.data)

"""
FOR:    path('movie/<str:mv>',views.movie, name='movie'),
"""
@api_view(['GET','POST'])
def movie(request, mv):
    if request.method == 'GET':
        try:
            movies=Movie.objects.get(id=mv)
        except: #except Movie.DoesNotExist: #to catch only not found here.
            return Response({"id":"No Movie by this id"}, status=status.HTTP_404_NOT_FOUND) 
        movie_serializer=MovieSerializer(movies, many=False)
        return Response(movie_serializer.data)    
    elif request.method == 'POST':
        url=f'https://www.omdbapi.com/?t={mv}&apikey=b1811c1'
        page=requests.get(url).json()
        if 'Error' in page:
            return Response({"Response":"False","Error":"Movie not found!"}, status=status.HTTP_404_NOT_FOUND) 
        movies=Movie.objects.filter(Title__icontains=mv).exists()
        if not movies:
            serializer = MovieSerializer(data=page)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Warning":"Movie Exists"}, status=status.HTTP_409_CONFLICT) 
        
"""
FOR:    path('comment/<int:id>',views.comment, name='comment'),
"""
@api_view(['GET','POST'])
def comment(request, id):
    if request.method == 'GET':
        try:
            movies=Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({"id":"No Movie by this id"}, status=status.HTTP_404_NOT_FOUND) 
        movie_serializer=MovieSerializer(movies, many=False)
        return Response(movie_serializer.data)

    if request.method == 'POST':
        try:
            movies=Movie.objects.filter(id=id)
        except Movie.DoesNotExist:
            return Response({"id":"No Movie by this id"}, status=status.HTTP_404_NOT_FOUND) 
        movie_serializer=CommentSerializer(data=request.data)
        serializer = movie_serializer
        if serializer.is_valid():
            movies.update(comment=serializer.data.get('comment'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
FOR:    path('comment/',views.all_comment, name='comments'),
"""
@api_view(['GET'])
def all_comment(request):
    if request.method == 'GET':# THIS LINE IS NOT NEEDED, IT ONLY MAKE THINGS CLEAR
        try:
            movies=Movie.objects.values('Title','comment')
        except Movie.DoesNotExist:
            return Response({"id":"No Movie by this id"}, status=status.HTTP_404_NOT_FOUND) 
        return Response(movies)

"""
FOR:    path('comment/movie/<str:mv>',views.movie_comment, name='movie_comment'),
"""
@api_view(['GET'])
def movie_comment(request,mv):
    if request.method == 'GET':# THIS LINE IS NOT NEEDED, IT ONLY MAKE THINGS CLEAR
        data={}
        try:
            movies=Movie.objects.get(Title__icontains=mv)
            data['Movie']=movies.Title
            data['Comment']=movies.comment
        except Movie.DoesNotExist:
            return Response({"Title":f"No Movie by this {mv} "}, status=status.HTTP_404_NOT_FOUND) 
        return Response(data)