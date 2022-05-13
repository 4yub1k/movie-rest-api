from django.db import models

class Movie(models.Model):
    """
    ADJUST THE FIELD SIZE ACCORDINGLY, I PREFER TO USE VARIABLE NAMES WITH SMALL NOT CAPITAL, BUT
    IT IS ADJUSTED ACCORDING TO THE <https://www.omdbapi.com>
    """
    Title=models.CharField(max_length=200)
    Year=models.CharField(max_length=200)
    Rated=models.CharField(max_length=200)
    Released=models.CharField(max_length=200)
    Runtime=models.CharField(max_length=200)
    Genre=models.CharField(max_length=200)
    Director=models.CharField(max_length=200)
    Writer= models.CharField(max_length=200)
    Actors= models.CharField(max_length=200)
    Plot= models.TextField(max_length=800)
    Language= models.CharField(max_length=200)
    Country= models.CharField(max_length=200)
    Awards=models.CharField(max_length=200)
    Poster= models.CharField(max_length=800,default="http://") #URLField
    Ratings=models.JSONField()
    Metascore= models.CharField(max_length=200)
    imdbRating= models.CharField(max_length=200)
    imdbVotes=models.CharField(max_length=200)
    imdbID= models.CharField(max_length=200)
    Type= models.CharField(max_length=200)
    DVD=models.CharField(max_length=200)
    BoxOffice= models.CharField(max_length=200)
    Production=models.CharField(max_length=200)
    Website= models.CharField(max_length=200)
    Response= models.BooleanField(default=True)
    comment=models.TextField(max_length=800, default="")
    def __str__(self):
        return "Moive : {}".format(self.Title)