from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(
            username='saaketh', email='saaketh@gmail.com', password='beehyv123')

    def test_signup(self):
        response = self.client.get(reverse('signup1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_user_registration(self):
        # data ={
        #     'username' : 'saaketh',
        #     'email' : 'saaketh@gmail.com',
        #     'password' : 'beehyv123'

        # }
        # response = self.client.post(reverse('signup1'), data)
        u = User.objects.get(id=1)
        self.assertEqual(u.username, 'saaketh')
