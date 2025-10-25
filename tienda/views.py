from django.shortcuts import get_object_or_404, render
from .models import Producto
from categorias.models import Categoria

def tienda(request, categoria_slug=None):
    if categoria_slug is not None:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = Producto.objects.all().filter(categoria=categoria, disponible=True)
        conteo_productos = productos.count()
    else:
        productos = Producto.objects.all().filter(disponible=True)
        conteo_productos = productos.count()
    
    context = {
        "productos": productos, 
        "conteo_productos": conteo_productos
        }
    return render(request, 'tienda/tienda.html', context)

