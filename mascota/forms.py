from django import forms

from . import models


class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = ["Nombre", "Raza", "Nacimiento", "Titular"]
