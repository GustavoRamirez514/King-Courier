from django.urls import path
from . import views

urlpatterns = [
    path("", views.pedido, name="pedidos"),
    path("create/", views.create_pedido, name="create_pedido"),
    path('pedidos/pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/pedido/<int:pedido_id>/cancelar', views.cancelar_pedido, name='cancelar_pedido'),
]
