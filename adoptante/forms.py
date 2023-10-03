from django import forms

from . import models


class AdoptanteForm(forms.ModelForm):
    class Meta:
        model = models.Adoptante
        fields = ["Nombre", "Apellido", "Nacimiento", "Adoptado"]
