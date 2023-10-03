from django.db import models

# Create your models here.
class Adoptante(models.Model):
  Nombre= models.CharField(max_length=100)
  Apellido= models.CharField(max_length=100)
  Nacimiento=models.DateField(null=True)
  Adoptado=models.CharField(max_length=100)

  def __str__(self)-> str:
    return f"{self.Nombre}({self.Apellido})- mascota:{self.Adoptado}"