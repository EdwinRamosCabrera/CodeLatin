from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio','disponible', 'categoria', 'fecha_creacion')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion')
    list_filter = ('disponible', 'categoria__nombre')
    ordering = ('nombre',)
    list_per_page = 10
