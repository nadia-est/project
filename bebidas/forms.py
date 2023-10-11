from django import forms

from . import models


class bebidasform(forms.ModelForm):
    class Meta:
        model = models.bebidas
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }