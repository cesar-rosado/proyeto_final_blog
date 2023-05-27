from django.db import models
from django.contrib.auth.models import User

from datetime  import datetime

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(default=datetime.now)
    contenido = models.TextField(editable=True,)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='img_articulos', null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo} {self.autor}"