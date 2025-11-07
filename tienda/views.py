from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Producto
from categorias.models import Categoria

def tienda(request):
    productos = Producto.objects.all().filter(disponible=True)
    conteo_productos = productos.count()
    categorias = Categoria.objects.all()
    
    context = {
        "productos": productos, 
        "categorias": categorias,
        "conteo_productos": conteo_productos,
        }
    return render(request, 'tienda/tienda.html', context)

def productos_por_categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    productos = Producto.objects.filter(categoria=categoria, disponible=True)
    categorias = Categoria.objects.all()
    conteo_productos = productos.count()

    context = {
        "productos": productos,
        "categorias": categorias,
        "categoria_seleccionada": categoria_slug,
        "conteo_productos": conteo_productos,
    }
    return render(request, 'tienda/tienda.html', context)

def detalle_producto(request, producto_slug):
    producto = get_object_or_404(Producto, slug=producto_slug)
    context = {
        "producto": producto,
    }
    return render(request, 'tienda/detalle_producto.html', context)