from django.test import TestCase, Client
from user.models import User
from user.forms import UserForm
from django.urls import reverse

class UserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.client.login(username='testuser', password='12345')

    def test_users_exist(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/users.html')
        self.assertContains(response, self.user.username)

    def test_no_users_exist(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
    