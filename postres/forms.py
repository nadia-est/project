from django import forms

from . import models


class postresform(forms.ModelForm):
    class Meta:
        model = models.postres
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }
        
        
class tiposdepostresform(forms.ModelForm):
    class Meta:
        model = models.postres
        fields = "__all__"

        widgets = {
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_actualizacion": forms.DateInput(attrs={"class": "form-control"}),
      
        }