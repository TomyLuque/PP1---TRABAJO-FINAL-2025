from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from clientes.models import Cliente
from ventas.models import Venta

@login_required
def inicio(request):
    productos_count = Producto.objects.count()
    clientes_count = Cliente.objects.count()
    ventas_count = Venta.objects.count()

    contexto = {
        'productos_count': productos_count,
        'clientes_count': clientes_count,
        'ventas_count': ventas_count,
    }

    return render(request, 'inicio.html', contexto)
