from django.db import models

class Movie(models.Model):
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
    #comment=models.CharField(max_length=200, default="")
    def __str__(self):
        return "Moive : {}".format(self.Title)

class Comment(models.Model):
    movie_id=models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment=models.CharField(max_length=200, blank=False)
    def __str__(self):
        return self.comment