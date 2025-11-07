from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('categoria/<slug:categoria_slug>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('productos/<slug:producto_slug>/', views.detalle_producto, name='detalle-producto'),
]