from django.db import models
from django.utils import timezone

class postres(models.Model):
  nombre = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=250, null=True, blank = True, verbose_name= "descripcion")

class Meta:
  verbose_name = "postre"
  verbose_name_plural = "postres"
        
def __str__(self)-> str:
        return self.nombre
      
class tiposdepostres(models.Model):
  categoria = models.ForeignKey( postres, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoría")
  nombre = models.CharField(max_length=50)
  cantidad = models.FloatField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
  fecha_actualizacion = models.DateTimeField( default=timezone.now, editable=False, verbose_name="fecha de actualización")
  
  class Meta:
        verbose_name = "tipo de postre"
        verbose_name_plural = "tipos de postres"
  def __str__(self)-> str:
        return f"{self.nombre} ({self.cantidad})- ${self.precio}"