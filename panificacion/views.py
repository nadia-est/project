from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

class panificacionlist(ListView):
    model = models.panificacion
    
    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.panificacion.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.panificacion.objects.all()
        return object_list


class panificaciondetail(DetailView):
    model = models.panificacion


class panificacioncreate(CreateView, LoginRequiredMixin):
    model = models.panificacion
    form_class = forms.panificacionform
    success_url = reverse_lazy("panificacion:panificacion_list")


class panificacionupdate(UpdateView, LoginRequiredMixin):
    model = models.panificacion
    form_class = forms.panificacionform
    success_url = reverse_lazy("panificacion:panificacion_list")


class panificaciondelete(DeleteView, LoginRequiredMixin):
    model = models.panificacion
    success_url = reverse_lazy("panificacion:panificacion_list")
    
    

class tiposdepanlist(ListView):
  model= models.panificacion
  
  def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.tiposdepan.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.tiposdepan.objects.all()
        return object_list


class tiposdepandetail(DetailView):
    model = models.panificacion


class tiposdepancreate(CreateView, LoginRequiredMixin):
    model = models.tiposdepan
    form_class = forms.tiposdepanform
    success_url = reverse_lazy("tiposdepan:tiposdepan_list")


class tiposdepanupdate(UpdateView, LoginRequiredMixin):
    model = models.tiposdepan
    form_class = forms.tiposdepanform
    success_url = reverse_lazy("tiposdepan:tiposdepan_list")


class tiposdepandelete(DeleteView, LoginRequiredMixin):
    model = models.tiposdepan
    success_url = reverse_lazy("tiposdepan:tiposdepan_list")