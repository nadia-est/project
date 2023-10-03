from django import forms

from . import models


class veterinarioForm(forms.ModelForm):
    class Meta:
        model = models.veterinario
        fields = ["Nombre", "Apellido","Nacimiento","Especialidad", "Paciente"]
