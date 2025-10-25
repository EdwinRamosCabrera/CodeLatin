from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('<slug:categoria_slug>/', views.tienda, name='productos_por_categoria'),
]