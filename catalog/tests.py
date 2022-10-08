# from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.

class TestGetToken(APITestCase):

    token = None

    def set_token(self):
        response = self.client.post('/api/v1/auth/token/login/', data={
            'username': 'test',
            'password': 'testPassword',
        })
        self.token = response.data['auth_token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def get_token(self):
        if self.token is None:
            self.set_token()
        return self.token
    def test_get_token(self):
        response = self.client.post('/api/v1/auth/users/', data={
            'username': 'test',
            'password': 'testPassword',
        })
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/v1/auth/token/login/', data={
            'username': 'test',
            'password': 'testPassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('auth_token', response.data)



class TestCategoryCreate(APITestCase):

    def authenticated_client(self):
        self.client.post('/api/v1/auth/users/', data={
            'username': 'test',
            'password': 'testPassword',
        })

        response = self.client.post('/api/v1/auth/token/login/', data={
            'username': 'test',
            'password': 'testPassword',
        })
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data[ 'auth_token' ])

    def test_category_create_not_authorized(self):
        data = {
            'name': 'Category 1',
            'isActive': True,
        }
        response = self.client.post('/api/v1/category/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_category_create(self):
        self.authenticated_client()
        data = {
            'name': 'Category 1',
            'isActive': True,
        }
        response = self.client.post('/api/v1/category/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data[ 'name' ], 'Category 1')
        self.assertEqual(response.data[ 'isActive' ], True)

    def test_category_get(self):
        self.authenticated_client()
        data = {
            'name': 'Category 1',
            'isActive': True,
        }
        self.client.post('/api/v1/category/', data)
        response = self.client.get('/api/v1/category/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], data['name'])
        self.assertEqual(response.data[0]['isActive'], data['isActive'])


