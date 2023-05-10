from django.test import TestCase, Client
from .models import Mensajeros
from django.urls import reverse

class MensajeroTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.mensajero1 = Mensajeros.objects.create(
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
        self.assertContains(response, self.mensajero1.nombre)

    def test_mensajero_sin_registros(self):
        Mensajeros.objects.all().delete()
        url = reverse('mensajeros')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mensajeros/index.html')
        self.assertContains(response, "No hay mensajeros registrados")
