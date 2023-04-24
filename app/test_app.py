from django.test import TestCase
from user.models import User
from app.forms import UserForm
from django.urls import reverse

class tests_forms(TestCase):

# Verificar que el formulario sea válido cuando se ingresan dos contraseñas iguales
    def test_passwords_match(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'num_phone': '123456789',
            'address': '123 St',
            'city': 'Anytown',
            'password1': 'password',
            'password2': 'password',
        }
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

# Verificar que el formulario sea inválido cuando se ingresan dos contraseñas distintas
    def test_passwords_not_match(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'num_phone': '123456789',
            'address': '123 St',
            'city': 'Anytown',
            'password1': 'password',
            'password2': 'differentpassword',
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())


class ViewsTestCase(TestCase):
    
    def test_perfil_view(self):
        url = reverse('perfil')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil.html')
        
    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        
        # prueba de solicitud POST con credenciales incorrectas
        response = self.client.post(url, {'username': 'usuario_incorrecto', 'password': 'contraseña_incorrecta'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'usuario o contraseña incorrectos')
        
        # prueba de solicitud POST con credenciales correctas
        user = User.objects.create_user(username='usuario_prueba', password='contraseña_prueba')
        response = self.client.post(url, {'username': 'usuario_prueba', 'password': 'contraseña_prueba'})
        self.assertRedirects(response, reverse('welcome'))
        
    def test_register_view(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        
    def test_logout_view(self):
        # prueba de cierre de sesión
        user = User.objects.create_user(username='usuario_prueba', password='contraseña_prueba')
        self.client.login(username='usuario_prueba', password='contraseña_prueba')
        url = reverse('logout')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))
        self.assertFalse('_auth_user_id' in self.client.session)