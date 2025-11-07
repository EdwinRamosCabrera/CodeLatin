from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/<slug:categoria_slug>/', views.productos_por_categoria, name='productos_por_categoria'),
]
