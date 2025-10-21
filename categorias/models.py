from django.db import models
from django.urls import reverse
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=300, blank=True, null=True)
    imagen = models.ImageField(upload_to='static/images/categoria', blank=True, null=True,)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
    def get_url(self):
        return reverse('producto_por_categoria', args=[self.slug])

