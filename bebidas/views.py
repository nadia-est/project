from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

class bebidaslist(ListView):
    model = models.bebidas
    
    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.bebidas.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.bebidas.objects.all()
        return object_list


class bebidasdetail(DetailView):
    model = models.bebidas


class bebidascreate(CreateView, LoginRequiredMixin):
    model = models.bebidas
    form_class = forms.bebidasform
    success_url = reverse_lazy("bebidas:bebidas_list")


class bebidasupdate(UpdateView, LoginRequiredMixin):
    model = models.bebidas
    form_class = forms.bebidasform
    success_url = reverse_lazy("bebidas:bebidas_list")


class bebidasdelete(DeleteView, LoginRequiredMixin):
    model = models.bebidas
    success_url = reverse_lazy("bebidas:bebidas_list")
    
