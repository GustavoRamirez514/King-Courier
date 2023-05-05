from django.test import TestCase
from core.user.models import User
from core.user.forms import UserForm
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
