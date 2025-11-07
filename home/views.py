from django.shortcuts import get_object_or_404, render
from tienda.models import Producto
from categorias.models import Categoria

# Create your views here.
def home(request):
    productos = Producto.objects.all().filter(disponible=True)
    context = {"productos": productos}
    return render(request, 'home/home.html', context)

def productos_por_categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    productos = Producto.objects.filter(categoria=categoria, disponible=True)
    categorias = Categoria.objects.all()
    context = {
        "productos": productos,
        "categoria_seleccionada": categoria_slug,
        "categorias": categorias
    }
    return render(request, 'home/home.html', context)