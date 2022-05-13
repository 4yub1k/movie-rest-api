from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from api.models import Movie

"""
This is my first test case i never wrote one before except unittest for python long ago, 
Learned from REST framework documentation for this this project.
"""

class Testmovie(APITestCase):

    def test_movie_all(self):
        
        """
        POST request fetch from external APi and add data to database
        """
        response1 = self.client.post('/api/movie/morbius')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().Title, 'Morbius') #api return with capital first
        #self.assertEqual(Movie.objects.get().id, 1)
        
        """
        GET Check the movies list contains the response data
        """
        #TEST list is empty or not
        response = self.client.get('/api/')
        #print(response.data,"get_movies")
        self.assertEqual(response.json()[0], response1.json())

        """
        GET Check to get movie by ID
        """
        #TEST movie get by id
        response = self.client.get('/api/movie/1')
        #print(response.data,"movie_id")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """
        POST Add comment to the movie
        """
        #Add comment
        data={'comment' : 'This is Vampire of Batman'}
        response = self.client.post('/api/comment/1',data, format='json')
        #print(response.data,"comment Added")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.get().comment,data['comment'])

        """
        GET Check if the comment is added
        """
        #Comment added
        response = self.client.get('/api/comment/')
        #print(response.json(),"comments list")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['Title'],'Morbius')
        self.assertEqual(response.json()[0]['comment'],data['comment'])