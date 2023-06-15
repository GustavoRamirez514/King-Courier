from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import ExtractMonth
import json
from .utils import render_to_pdf
from django.views.generic import View
from django.http import HttpResponse
from GestionPedidos.models import Pedido

# Create your views here.

def reporte_pedidos_cliente(request):
    # Obtener todos los pedidos con la cantidad de pedidos por cliente
    pedidos_por_mensajero = Pedido.objects.values('id_cliente', 'id_cliente__nombre').annotate(cantidad_pedidos=Count('id_cliente'))

    # Convertir pedidos_por_mensajero a una lista de diccionarios
    pedidos_por_mensajero_list = list(pedidos_por_mensajero)

    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()
    return render(request, 'reportes/reportes_cliente.html', {
        'pedidos': pedidos,
        'pedidos_cliente': json.dumps(pedidos_por_mensajero_list)
    })

class ListPedidos_clientesPdf(View):
    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.all()
        data = {
            'pedidos': pedidos,
        }
        pdf = render_to_pdf('reportes/reportes_cliente.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def reporte_pedidos_fecha(request):
     # Obtener los pedidos agrupados por mes de creación
    pedidos_por_mes = Pedido.objects.annotate(mes_creacion=ExtractMonth('created')) \
        .values('mes_creacion') \
        .annotate(cantidad_pedidos=Count('id'))
    
    # Convertir pedidos_por_mensajero a una lista de diccionarios
    pedidos_por_mes_list = list(pedidos_por_mes)

    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()

    return render(request, 'reportes/reportes_mes.html', {'pedidos': pedidos, 'pedidos_mes': json.dumps(pedidos_por_mes_list)})

class ListPedidos_mesesPdf(View):
    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.all()
        data = {
            'pedidos': pedidos,
        }
        pdf = render_to_pdf('reportes/reportes_mes.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def reporte_pedidos_mensajero(request):
    # Obtener todos los pedidos con la cantidad de pedidos por cliente
    pedidos_por_mensajero = Pedido.objects.values('id_mensajero', 'id_mensajero__nombre').annotate(cantidad_pedidos=Count('id_mensajero'))

    # Convertir pedidos_por_mensajero a una lista de diccionarios
    pedidos_por_mensajero_list = list(pedidos_por_mensajero)

    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()
    return render(request, 'reportes/reportes_mensajero.html', {
        'pedidos': pedidos,
        'pedidos_mensajero': json.dumps(pedidos_por_mensajero_list)
    })

class ListPedidos_mensajeroPdf(View):
    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.all()
        data = {
            'pedidos': pedidos,
        }
        pdf = render_to_pdf('reportes/reportes_mensajero.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
