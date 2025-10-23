from django.shortcuts import render
from tienda.models import Producto

# Create your views here.
def home(request):
    productos = Producto.objects.all().filter(activo=True)
    context = {"productos": productos}
    return render(request, 'home/home.html', context)