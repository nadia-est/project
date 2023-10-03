from django.db import models

# Create your models here.
class veterinario(models.Model):
  Nombre= models.CharField(max_length=100)
  Apellido= models.CharField(max_length=100)
  Nacimiento=models.DateField(null=True)
  Especialidad=models.CharField(max_length=100)
  Paciente=models.CharField(max_length=100)
  
  def __str__(self)-> str:
    return f"{self.Nombre} {self.Apellido} - paciente: {self.paciente}"