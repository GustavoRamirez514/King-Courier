from django.test import TestCase, Client
from .models import Mensajeros
from django.urls import reverse
from user.models import User

class MensajeroTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.mensajero = Mensajeros.objects.create(
            identificacion="123456789",
            nombre="Mensajero 1",
            direccion="Dirección 1",
            ciudad="Ciudad 1",
            email="mensajero1@example.com",
            telefono="1234567",
            vehiculo="Vehículo 1",
            activo=True
        )

    def test_mensajero(self):
        url = reverse('mensajeros')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mensajeros/index.html')
        self.assertContains(response, self.mensajero.nombre)

    def test_mensajero_sin_registros(self):
        Mensajeros.objects.all().delete()
        url = reverse('mensajeros')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mensajeros/index.html')
        self.assertContains(response, "No hay mensajeros registrados")

    def test_create_mensajero_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create_mensajeros'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mensajeros/create.html')
        self.assertContains(response, '<form')

    def test_create_mensajero_post_valid(self):
        self.client.force_login(self.user)
        data = {
            'identificacion': '9876543210',
            'nombre': 'Jane Doe',
            'direccion': '456 Elm St',
            'ciudad': 'City',
            'email': 'jane@example.com',
            'telefono': '9876543210',
            'vehiculo': 'Bike',
        }
        response = self.client.post(reverse('create_mensajeros'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('mensajeros'))

    def test_create_mensajero_post_invalid(self):
        self.client.force_login(self.user)
        data = {}
        response = self.client.post(reverse('create_mensajeros'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mensajeros/create.html')
        self.assertContains(response, 'Datos inválidos')

    def test_detalle_mensajero(self):
        response = self.client.get(reverse('detalle_mensajero', args=[self.mensajero.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mensajeros/detail.html')
        self.assertEqual(response.context['mensajero'], self.mensajero)

    def test_editar_mensajero_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('editar_mensajero', args=[self.mensajero.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mensajeros/edit.html')
        self.assertContains(response, '<form')

    def test_editar_mensajero_post_valid(self):
        self.client.force_login(self.user)
        data = {
            'identificacion': '9876543210',
            'nombre': 'Jane Doe',
            'direccion': '456 Elm St',
            'ciudad': 'City',
            'email': 'jane@example.com',
            'telefono': '9876543210',
            'vehiculo': 'Bike',
        }
        response = self.client.post(reverse('editar_mensajero', args=[self.mensajero.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('detalle_mensajero', args=[self.mensajero.id]))

    def test_eliminar_mensajero(self):
        response = self.client.get(reverse('eliminar_mensajero', args=[self.mensajero.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('mensajeros'))
        self.mensajero.refresh_from_db()
        self.assertFalse(self.mensajero.activo)