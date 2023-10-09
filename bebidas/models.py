
from django.db import models
from django.utils import timezone

class bebidas(models.Model):
  nombre = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=250, null=True, blank = True, verbose_name= "descripcion")

class Meta:
  verbose_name = "panificacion"
  verbose_name_plural = "panificacion"
        
def __str__(self)-> str:
        return self.nombre