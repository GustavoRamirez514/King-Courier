# from user.models import User
# from GestionClientes.models import Cliente
# from django.test import TestCase
# from datetime import datetime
# from .models import DetalleEstadoPedido, Pedido, EstadoPedido
# from .views import pedido, create_pedido, detalle_pedido, cancelar_pedido, pedido_mensajero, cambiar_estado_pedido

# class PedidoTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.client.login(username='testuser', password='testpass')

#     def test_pedido_no_registrado(self):
#         response = self.client.get('/pedido/')
#         self.assertContains(response, "No hay pedidos registrados")

#     def test_create_pedido(self):
#         cliente = Cliente.objects.create(user=self.user)  # Crear un objeto Cliente asociado al usuario
#         response = self.client.post('create_pedido', {'fecha_hora': datetime.now(), 'id_cliente': cliente.id})
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Pedido.objects.count(), 1)

#     def test_detalle_pedido(self):
#         cliente = Cliente.objects.create(user=self.user)  # Crear un objeto Cliente asociado al usuario
#         pedido = Pedido.objects.create(id_cliente=cliente)
#         detalle = DetalleEstadoPedido.objects.create(id_pedido=pedido, fecha_hora=datetime.now())
#         response = self.client.get(f'/detalle_pedido/{pedido.id}/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.context['pedido'], detalle)

#     def test_cancelar_pedido(self):
#         cliente = Cliente.objects.create(user=self.user)  # Crear un objeto Cliente asociado al usuario
#         pedido = Pedido.objects.create(id_cliente=cliente)
#         response = self.client.get(f'/cancelar_pedido/{pedido.id}/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(DetalleEstadoPedido.objects.count(), 1)
#         self.assertEqual(DetalleEstadoPedido.objects.first().id_estado.pk, 6)

#     def test_pedido_mensajero_no_registrado(self):
#         response = self.client.get('mensajero_pedidos')
#         self.assertContains(response, "No eres propietario de ningún pedido")

#     def test_cambiar_estado_pedido(self):
#         cliente = Cliente.objects.create(user=self.user)  # Crear un objeto Cliente asociado al usuario
#         pedido = Pedido.objects.create(id_cliente=cliente)
#         estado = EstadoPedido.objects.create(nombre='Estado 1')
#         response = self.client.post(f'/cambiar_estado_pedido/{pedido.id}/', {'estado_seleccionado': estado.id, 'foto': 'test.jpg'})
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(DetalleEstadoPedido.objects.count(), 1)
#         self.assertEqual(DetalleEstadoPedido.objects.first().id_estado, estado)
#         self.assertEqual(DetalleEstadoPedido.objects.first().foto.name, 'test.jpg')