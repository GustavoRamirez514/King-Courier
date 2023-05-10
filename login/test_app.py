from django.test import TestCase, Client
from user.models import User
from user.forms import UserForm
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


class LoginTestCase(TestCase):
    def setUp(self):
        # Creamos un usuario de prueba
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_login_home(self):
        # Obtenemos la URL de inicio de sesión utilizando la función 'reverse' de Django
        url = reverse('login')

        # Enviamos una solicitud GET a la URL de inicio de sesión y verificamos que el código de estado de la respuesta sea 200
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Enviamos una solicitud POST a la URL de inicio de sesión con credenciales de usuario válidas y verificamos que se redirige correctamente a la URL de bienvenida
        response = self.client.post(
            url, {'username': 'testuser', 'password': 'testpass'})
        self.assertRedirects(response, reverse('welcome'))

        # Enviamos una solicitud POST a la URL de inicio de sesión con credenciales de usuario inválidas y verificamos que el código de estado de la respuesta sea 200 y que el mensaje de error se muestra en la respuesta
        response = self.client.post(
            url, {'username': 'wronguser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'usuario o contraseña incorrectos')

    def test_log_out(self):
        # Iniciar sesión para probar el cierre de sesión
        self.client.login(username='testuser', password='testpass')

        # Hacer una solicitud de cierre de sesión y verificar que se redirige a la página de inicio
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

        # Verificar que no se puede acceder a una página autenticada después del cierre de sesión
        response = self.client.get(reverse('perfil'))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('perfil'))