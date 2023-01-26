from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, CommentSerializer
from api.models import Movie
from rest_framework import status
from requests import get
from django.db.models import F


def index(request):
    return render(request, "main.html")


@api_view(["GET", "POST"])
def movie(request):

    if request.method == "GET":
        mv = request.query_params.get("id", None)
        all = request.query_params.get("list", None)

        if mv:
            try:
                movies = Movie.objects.get(id=mv)
            except:  # Modify it accordingly except Movie.DoesNotExist:
                return Response(
                    {"id": "No Movie by this id"}, status=status.HTTP_404_NOT_FOUND
                )
            movie_serializer = MovieSerializer(movies, many=False)
            return Response(movie_serializer.data)

        if all == "all":
            movies = Movie.objects.all()
            movie_serializer = MovieSerializer(movies, many=True)
            return Response(movie_serializer.data)

    if request.method == "POST":
        mv = request.query_params.get("movie", None)
        url = f"https://www.omdbapi.com/?t={mv}&apikey=b1811c1"
        page = get(url).json()
        # print(page)
        if "Error" in page:
            return Response(
                {"Response": "False", "Error": "Movie not found!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        movies = Movie.objects.filter(Title__icontains=mv).exists()
        # print(movies)
        if not movies:
            serializer = MovieSerializer(data=page)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Warning": "Movie Exists"}, status=status.HTTP_409_CONFLICT)

    data = {
        "command": [
            "/?list=all, to list all comments",
            "/?movie=<movie name>, to add movie",
            "/?id=<movie id>, to search movie by id",
        ]
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def comment(request):

    if request.method == "GET":
        id = request.query_params.get("id", None)
        all = request.query_params.get("list", None)
        movie_name = request.query_params.get("movie", None)

        if id:
            try:
                movies = Movie.objects.filter(id=id)
            except Movie.DoesNotExist:
                return Response(
                    {"id": "No Movie by this id"}, status=status.HTTP_404_NOT_FOUND
                )
            movie = movies.annotate(comments=F("comment__comment")).values(
                "id", "Title", "comments"
            )
            return Response(movie)

        elif all == "all":
            try:
                movies = Movie.objects.annotate(comments=F("comment__comment")).values(
                    "id", "Title", "comments"
                )
            except Movie.DoesNotExist:
                return Response(
                    {"id": "No Movie by this id"}, status=status.HTTP_404_NOT_FOUND
                )
            return Response(movies)

        elif movie_name:
            try:
                # movies=Movie.objects.get(Title__icontains=movie_name)
                movies = Movie.objects.filter(Title__iexact=movie_name)
            except Movie.DoesNotExist:
                return Response(
                    {"Title": f"No Movie by this {movie_name} "},
                    status=status.HTTP_404_NOT_FOUND,
                )
            movies = movies.annotate(comments=F("comment__comment")).values(
                "id", "Title", "comments"
            )
            return Response(movies)

    if request.method == "POST":
        id = request.query_params.get("id", None)

        try:
            movies = Movie.objects.filter(id=id)
        except Movie.DoesNotExist:
            return Response(
                {"id": "No Movie by this id"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = {
        "command": [
            "/?list=all, to list all comments",
            "/?movie_name=<movie name>, to search comment by movie",
        ]
    }
    return Response(data, status=status.HTTP_200_OK)
