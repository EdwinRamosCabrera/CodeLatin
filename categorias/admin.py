from django.contrib import admin
from django.urls import reverse
from .models import Categoria

#admin.site.register(Categoria, CategoriaAdmin)
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'descripcion', 'activo', 'fecha_creacion', 'fecha_modificacion')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre',)
    ordering = ('nombre',)
    list_per_page = 5

    
