from django.shortcuts import render
from .models import Producto

def tienda(request):
    productos = Producto.objects.all().filter(activo=True)
    conteo_productos = productos.count()
    context = {
        "productos": productos, 
        "conteo_productos": conteo_productos
        }
    return render(request, 'tienda/tienda.html', context)

