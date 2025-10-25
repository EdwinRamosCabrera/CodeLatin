from .models import Categoria

def menu_links(request):
    links = Categoria.objects.all()
    return dict(links=links) # Devuelve un diccionario con las categorías cuya clave es 'links' y valor son las categorias obtenidas