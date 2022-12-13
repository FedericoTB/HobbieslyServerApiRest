import json

from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status
from apirestappserver.models import *


# Create your tests here.
class UserViewSetTestCase(TestCase):

    def setUp(self):
        user = User(
            email='testing_login@cosasdedevs.com',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()

        client = APIClient()
        response = client.post(
            '/api/loginng/', {
                'username': 'testing_login',
                'password': 'admin123',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.access_token = result['access']
        self.user = user

    def test_get_user_not_authorized(self):
        client = APIClient()
        response = client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        response = client.get(f'/api/users/{self.user.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)
        
        self.assertIsInstance(result['id'], int)
        self.assertEqual(result['id'], self.user.id)
        self.assertIsInstance(result['username'], str)
        self.assertEqual(result['username'], self.user.username)
        self.assertIsInstance(result['email'], str)
        self.assertEqual(result['email'], self.user.email)
        self.assertIsInstance(result['first_name'], str)
        self.assertEqual(result['first_name'], self.user.first_name)
        self.assertIsInstance(result['last_name'], str)
        self.assertEqual(result['last_name'], self.user.last_name)
        self.assertIsInstance(result['gender'], str)
        self.assertEqual(result['gender'], self.user.gender)
        self.assertIsInstance(result['birth_date'], str)
        self.assertIsInstance(result['adress'], str)
        self.assertEqual(result['adress'], self.user.adress)
        self.assertIsInstance(result['city'], str)
        self.assertEqual(result['city'], self.user.city)
        self.assertIsInstance(result['country'], str)
        self.assertEqual(result['country'], self.user.country)
        self.assertIsInstance(result['image_url'], str)
        self.assertEqual(result['image_url'], self.user.image_url)
    
    def test_get_user_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.get(f'/api/users/a/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_post_user_not_authorized(self):
        client = APIClient()
        response = client.post(f'/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_post_user_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        usc = {
            "username": "ghjwrfdg123",
            "email": "user124sf@example.com",
            "first_name": "sagdasgasg",
            "last_name": "sadgasassa",
            "gender": "M",
            "birth_date": "2022-12-11",
            "adress": "asdgasdg",
            "city": "asgdsadg",
            "country": "asgdasg",
            "image_url": "http://www.images.url/154664.jpg",
            "password": "oefd5236"
        }

        response = client.post(
            f'/api/users/',
            usc,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result['username'], usc['username'])
        self.assertEqual(result['email'], usc['email'])
        self.assertEqual(result['first_name'], usc['first_name'])
        self.assertEqual(result['last_name'], usc['last_name'])
        self.assertEqual(result['adress'], usc['adress'])
        self.assertEqual(result['city'], usc['city'])
        self.assertEqual(result['country'], usc['country'])

    def test_post_user_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        usc = {
            'username':'testing4',
            'email':'test3@cosasdedevs.com',
            'first_name':'Test32412',
            'last_name':'Test312415',
            'adress':'fasfasd123425',
            'city':'fasfsdd2626',
            'country':'aafqfasfasgf',
            'birth_date':'1988-12-12',
            'gender':'F',
            'image_url':'http:\\\\imageurl.com\\127423.jpg',
            'password':'t65r3rht'
        }

        response = client.post(
            f'/api/users/',
            usc,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_not_authorized(self):
        client = APIClient()
        response = client.put(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_user_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        us = User.objects.create(
            username='testing2',
            email='test2@cosasdedevs.com',
            first_name='Test2',
            last_name='Test34',
            adress='asdasd123',
            city='asdasdd1233',
            country='asfasgag'
        )
        us.set_password('tng1123')

        us_update = {
            'username':'testing1',
            'email':'test1@cosasdedevs.com',
            'first_name':'Test4345',
            'last_name':'Test12345',
        
        }

        response = client.put(
            f'/api/users/{us.id}/',
            us_update,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        us = User.objects.create(
            username='testing1',
            email='test1@cosasdedevs.com',
            first_name='Test1',
            last_name='Test12',
            adress='asdasd',
            city='asdasdd',
            country='asfasgag'
        )
        us.set_password('tng1123')

        us_update = {
            'username':'testing1',
            'email':'test1@cosasdedevs.com',
            'first_name':'Test1234',
            'last_name':'Test12234',
            'adress':'asdasd123',
            'city':'asdasdd123',
            'country':'asfasgag123',
            'password':'tng1123'
        }

        response = client.put(
            f'/api/users/{us.id}/',
            us_update,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(result['username'], us_update['username'])
        self.assertEqual(result['email'], us_update['email'])
        self.assertEqual(result['first_name'], us_update['first_name'])
        self.assertEqual(result['last_name'], us_update['last_name'])
        self.assertEqual(result['adress'], us_update['adress'])
        self.assertEqual(result['city'], us_update['city'])
        self.assertEqual(result['country'], us_update['country'])

    def test_delete_user_not_authorized(self):
        client = APIClient()
        response = client.delete(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_delete_user_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        us = User.objects.create(
            username='testing5',
            email='test5@cosasdedevs.com',
            first_name='Test5',
            last_name='Test52',
            adress='asdasd',
            city='asdasdd',
            country='asfasgag'
        )
        us.set_password('tng1123')

        response = client.delete(
            f'/api/users/{us.pk}/', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        us = User.objects.create(
            username='testing5',
            email='test5@cosasdedevs.com',
            first_name='Test5',
            last_name='Test52',
            adress='asdasd',
            city='asdasdd',
            country='asfasgag'
        )
        us.set_password('tng1123')

        response = client.delete(
            f'/api/users/10000/', 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CategoriesViewSetTestCase(TestCase):

    def setUp(self):
        user = User(
            email='testing_login@cosasdedevs.com',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()

        client = APIClient()
        response = client.post(
            '/api/loginng/', {
                'username': 'testing_login',
                'password': 'admin123',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.access_token = result['access']
        self.user = user

    def test_get_category_not_authorized(self):
        client = APIClient()
        response = client.get(f'/api/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_category_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        cat = Categories.objects.create(
            id=50,
            name="cattest1",
            description="cattest1descr"
        )

        response = client.get(f'/api/categories/{cat.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)
        
        self.assertIsInstance(result['name'], str)
        self.assertEqual(result['name'], cat.name)
        self.assertIsInstance(result['description'], str)
        self.assertEqual(result['description'], cat.description)
    
    def test_get_category_incorrect(self):
        client = APIClient()
        cat = Categories.objects.create(
            id=51,
            name="cattest2",
            description="cattest2descr"
        )
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.get(f'/api/categories/52/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_post_category_not_authorized(self):
        client = APIClient()
        response = client.post(f'/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_post_category_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        cat = {
            'name':'cattest4',
            'description':'cattest4descr'
        }

        response = client.post(
            f'/api/categories/',
            cat,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result['name'], cat['name'])
        self.assertEqual(result['description'], cat['description'])

    def test_post_category_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        cat = {
            'description':'cattest5descr'
        }

        response = client.post(
            f'/api/categories/',
            cat,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_category_not_authorized(self):
        client = APIClient()
        response = client.put(f'/api/categories/50/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_category_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        cat = Categories.objects.create(
            id=59,
            name="cattest2",
            description="cattest2descr"
        )

        cat_update = {
            'description':'cattest7descr'
        }

        response = client.put(
            f'/api/categories/{cat.pk}/',
            cat_update,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_category_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        cat = Categories.objects.create(
            id=57,
            name="cattest8",
            description="cattest8descr"
        )

        cat_update = {
            'name':'cattest814',
            'description':'cattest8descr41'
        }

        response = client.put(
            f'/api/categories/{cat.pk}/',
            cat_update,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['name'], cat_update['name'])
        self.assertEqual(result['description'], cat_update['description'])
     

    def test_delete_category_not_authorized(self):
        client = APIClient()
        response = client.delete(f'/api/categories/78/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_delete_category_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
        cat = Categories.objects.create(
            id=64,
            name="cattest64",
            description="cattest64descr"
        )

        response = client.delete(
            f'/api/categories/{cat.pk}/', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_category_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
        cat = Categories.objects.create(
            id=78,
            name="cattest78",
            description="cattest78descr"
        )

        response = client.delete(
            f'/api/categories/10000/', 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UserGroupsViewSetTestCase(TestCase):

    def setUp(self):
        user = User(
            email='testing3_login@cosasdedevs.com',
            first_name='Testing3',
            last_name='Testing3',
            username='testing_login3'
        )
        user.set_password('admin1233')
        user.save()

        client = APIClient()
        response = client.post(
            '/api/loginng/', {
                'username': 'testing_login3',
                'password': 'admin1233',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.access_token = result['access']
        self.user = user

    def test_get_usergroups_not_authorized(self):
        client = APIClient()
        response = client.get(f'/api/usergroups/10/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_usergroups_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        ug = UsersGroups.objects.create(
            id=50,
            name="ugtest1",
            description="ugtest1descr",
            image_url="http://imageurl.com/127423.jpg",
            owner=self.user
        )

        response = client.get(f'/api/usergroups/{ug.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)
        
        self.assertIsInstance(result['name'], str)
        self.assertEqual(result['name'], ug.name)
        self.assertIsInstance(result['description'], str)
        self.assertEqual(result['description'], ug.description)
        self.assertIsInstance(result['image_url'], str)
        self.assertEqual(result['image_url'], ug.image_url)
    
    def test_get_usergroups_incorrect(self):
        client = APIClient()
        ug = UsersGroups.objects.create(
            id=51,
            name="ugtest2",
            description="ugtest2descr",
            image_url="http://imageurl.com/1274232.jpg",
            owner=self.user
        )
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.get(f'/api/usergroups/52/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_post_usergroups_not_authorized(self):
        client = APIClient()
        response = client.post(f'/api/usergroups/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_post_usergroups_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        ug = {
            'name':'ugtest3',
            'description':'ugtest3descr',
            'image_url':'http://imageurl.com/1274232.jpg'
        }

        response = client.post(
            f'/api/usergroups/',
            ug,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result['name'], ug['name'])
        self.assertEqual(result['description'], ug['description'])
        self.assertEqual(result['image_url'], ug['image_url'])

    def test_post_usergroups_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        ug = {
            'description':"ugtest3descr",
            'image_url':'http://imageurl.com/1274232.jpg'
        }

        response = client.post(
            f'/api/usergroups/',
            ug,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_usergroups_not_authorized(self):
        client = APIClient()
        response = client.put(f'/api/usergroups/50/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_usergroups_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        ug = UsersGroups.objects.create(
            id=55,
            name="ugtest5",
            description="ugtest5descr",
            image_url="http://imageurl.com/1274252.jpg",
            owner=self.user
        )

        ug_update = {
            'description':"ugtest2descr",
        }

        response = client.put(
            f'/api/usergroups/{ug.pk}/',
            ug_update,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_usergroups_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        ug = UsersGroups.objects.create(
            id=56,
            name="ugtest6",
            description="ugtest6descr",
            image_url="http://imageurl.com/1274262.jpg",
            owner=self.user
        )

        ug_update = {
            'name':'ugtest63',
            'description':"ugtest63descr",
            'image_url':"http://imageurl.com/12742623.jpg",
            'owner':self.user.pk
        }

        response = client.put(
            f'/api/usergroups/{ug.pk}/',
            ug_update,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['name'], ug_update['name'])
        self.assertEqual(result['description'], ug_update['description'])
        self.assertEqual(result['image_url'], ug_update['image_url'])
     

    def test_delete_usergroups_not_authorized(self):
        client = APIClient()
        response = client.delete(f'/api/usergroups/78/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_delete_usergroups_correct(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
        ug = UsersGroups.objects.create(
            id=70,
            name="ugtest70",
            description="ugtest70descr",
            image_url="http://imageurl.com/1274270.jpg",
            owner=self.user
        )

        response = client.delete(
            f'/api/usergroups/{ug.pk}/', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_usergroups_incorrect(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
        ug = UsersGroups.objects.create(
            id=71,
            name="ugtest71",
            description="ugtest71descr",
            image_url="http://imageurl.com/1274271.jpg",
            owner=self.user
        )

        response = client.delete(
            f'/api/usergroups/10000/', 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


'''
class TestCase(APITestCase):

    def test_get(self):
        pass

    def test_get_list(self):
        pass

    def test_post(self):
        pass

    def test_put(self):
        pass

    def test_patch(self):
        pass

    def test_delete(self):
        pass
'''