from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from api.models import Movie

class Testmovie(APITestCase):

    def create_db(self):
        return self.client.post('/movies/?movie=morbius')

    def test_movie_create(self):
        
        """
        POST request fetch from external APi and add data to database
        """
        response_created = self.create_db()
        self.assertEqual(response_created.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().Title, 'Morbius') #api return with capital first

    def test_movie_list_check(self):    
        """
        GET Check the movies list contains the response data
        """
        #TEST list is empty or not
        response_created=self.create_db()
        response = self.client.get('/movies/?list=all')
        #print(response.data,"get_movies")
        self.assertEqual(response.json()[0], response_created.json())

    def test_get_by_id(self):
        """
        GET Check to get movie by ID
        """
        #TEST movie get by id
        self.create_db()
        response = self.client.get('/movies/?id=1')
        #print(response.data,"movie_id")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_comment(self):
        """
        POST Add comment to the movie
        """
        #Add comment
        self.create_db()
        data={'movie_id':1,'comment' : 'This is Vampire of Batman'}
        response = self.client.post('/comment/',data, format='json')
        #print(response.data,"comment Added")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['comment'],data['comment'])
        self.assertEqual(response.json()['movie_id'],data['movie_id'])

    def test_check_comment_added(self):
        """
        GET Check if the comment is added
        """
        #Comment added
        self.create_db()
        data={'movie_id':'1','comment' : 'This is Vampire of Batman'}
        response = self.client.post('/comment/',data, format='json')
        response = self.client.get('/comment/?list=all')
        #print(response.json(),"comments list")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['Title'],'Morbius')
        self.assertEqual(response.json()[0]['comments'],data['comment'])