from django.shortcuts import get_object_or_404, render
from tienda.models import Producto
from categorias.models import Categoria

# Create your views here.
def home(request):
    productos = Producto.objects.all().filter(disponible=True)
    categoria = Categoria.objects.first()
    print(categoria.get_url())
    context = {"productos": productos}

    return render(request, 'home/home.html', context)
