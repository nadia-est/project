from django.db import models

# Create your models here.
class Mascota(models.Model):
  Nombre= models.CharField(max_length=100)
  Raza= models.CharField(max_length=100)
  Nacimiento=models.DateField(null=True)
  Titular=models.CharField(max_length=100)

  def __str__(self)-> str:
    return f"{self.Nombre}({self.Raza})- Dueño:{self.Titular}"