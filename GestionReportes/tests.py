from django.test import TestCase, RequestFactory
from django.urls import reverse
from . import views

class ReportesTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_reporte_pedidos_cliente(self):
        url = reverse('reporte_pedido_cliente')
        request = self.factory.get(url)
        response = views.reporte_pedidos_cliente(request)
        self.assertEqual(response.status_code, 200)
        

    def test_reporte_pedidos_fecha(self):
        url = reverse('reporte_pedido_fecha')
        request = self.factory.get(url)
        response = views.reporte_pedidos_fecha(request)
        self.assertEqual(response.status_code, 200)
       

    def test_reporte_pedidos_mensajero(self):
        url = reverse('reporte_pedido_mensajero')
        request = self.factory.get(url)
        response = views.reporte_pedidos_mensajero(request)
        self.assertEqual(response.status_code, 200)
        

    def test_list_pedidos_clientes_pdf(self):
        url = reverse('reporte_pedido_clientes_pdf')
        request = self.factory.get(url)
        response = views.ListPedidos_clientesPdf.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
       

    def test_list_pedidos_meses_pdf(self):
        url = reverse('reporte_pedido_meses_pdf')
        request = self.factory.get(url)
        response = views.ListPedidos_mesesPdf.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
       

    def test_list_pedidos_mensajero_pdf(self):
        url = reverse('reporte_pedido_mensajero_pdf')
        request = self.factory.get(url)
        response = views.ListPedidos_mensajeroPdf.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
       
