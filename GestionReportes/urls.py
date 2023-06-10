from django.urls import path
from . import views

urlpatterns = [
    path("", views.reporte_pedidos_cliente, name="reporte_pedido_cliente"),
    path("reporte_fecha/", views.reporte_pedidos_fecha, name="reporte_pedido_fecha"),
    path("reporte_mensajero/", views.reporte_pedidos_mensajero, name="reporte_pedido_mensajero"),
    path("reporte_mensajero_pdf/", views.ListPedidos_mensajeroPdf.as_view(), name="reporte_pedido_mensajero_pdf"),
    path("reporte_meses_pdf/", views.ListPedidos_mesesPdf.as_view(), name="reporte_pedido_meses_pdf"),
    path("reporte_clientes_pdf/", views.ListPedidos_clientesPdf.as_view(), name="reporte_pedido_clientes_pdf"),
]