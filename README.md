# movie-rest-api
Django REST framework, Django based api to fetch, store and provide details about movies from external api by movie name, you can add comments(or of users) to movies. For more read **Usage**.

![D-version](https://img.shields.io/badge/Django-4.0.4-blue)
![P-version](https://img.shields.io/badge/Python-3.10-green)
![T-version](https://img.shields.io/badge/Testing-Pass-green)

## ENV Variables:
```
CREATE FILE: .env , and add values for following,

POSTGRES_DB=<db_name>
POSTGRES_USER=<db_user>
POSTGRES_PASSWORD=<db_passwird>
DJANGO_DEBUG=False
SECRET_KEY=<your_secret_key>
#ALLOWED_HOSTS=127.0.0.1,172.21.0.2
ALLOWED_HOSTS=<hosts seperated by (,)>
API_KEY=<api_key from omdbapi page>
```

## Build & Run:
```
- docker-compose build
- docker-compose up
```
## Test:
```
- docker exec -it django_container /bin/bash
   - python manage.py test
```
## Usage:

### List all movies -GET
```
- http://127.0.0.1:8000/movies/?list=all
```
### Movie Search by ID -GET
```
- http://127.0.0.1:8000/movies/?id=1
- 127.0.0.1:8000/movies/?id=1
```
### Add movie by Title -POST
```
- http://127.0.0.1:8000/movies/?movie=Oscar
- 127.0.0.1:8000/movies/?movie=(movie name) **(POST this request with name)
```
### List All comments -GET
```
- http://127.0.0.1:8000/comment/?list=all
- 127.0.0.1:8000/comment/?list=all **(Returns all Movies with comments)
```
### Add Comment by ID of Movie -POST
```
- http://127.0.0.1:8000/comment/
- 127.0.0.1:8000/comment/ **(POST to this url with { "movie_id":1, "comment":"movie comments" }) to add comment
```
### Search comment by ID -GET
```
- http://127.0.0.1:8000/comment/?id=1
- 127.0.0.1:8000/comment/?id=1 **(Return the id, Title and comment)
```
### Search comment by Title -GET
```
- http://127.0.0.1:8000/comment/?movie=(movie name)
- 127.0.0.1:8000/comment/?movie=(movie name) **(Return the id, Title and comment)
```
## Main Page:
![image](https://user-images.githubusercontent.com/45902447/169301205-ccf973b9-8191-4975-a23d-6dd40c6ec394.png)

## Example:
```
[
    {
        "id": 1,
        "Title": "Oscar",
        "Year": "1991",
        "Rated": "PG",
        "Released": "26 Apr 1991",
        "Runtime": "109 min",
        "Genre": "Comedy, Crime",
        "Director": "John Landis",
        "Writer": "Claude Magnier, Michael Barrie, Jim Mulholland",
        "Actors": "Sylvester Stallone, Ornella Muti, Peter Riegert",
        "Plot": "A gangster attempts to keep the promise he made to his dying father: that he would give up his life of crime and \"go straight\".",
        "Language": "English, Italian",
        "Country": "United States",
        "Awards": "3 nominations",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMjRhYjg3YWEtOTYzZS00ZWY5LWJkNmEtYWE0YmQ3NDY2OWZlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
        "Ratings": [
            {
                "Value": "6.5/10",
                "Source": "Internet Movie Database"
            },
            {
                "Value": "12%",
                "Source": "Rotten Tomatoes"
            },
            {
                "Value": "47/100",
                "Source": "Metacritic"
            }
        ],
        "Metascore": "47",
        "imdbRating": "6.5",
        "imdbVotes": "31,826",
        "imdbID": "tt0102603",
        "Type": "movie",
        "DVD": "06 May 2003",
        "BoxOffice": "$23,562,716",
        "Production": "N/A",
        "Website": "N/A",
        "Response": true
    }
]
```
