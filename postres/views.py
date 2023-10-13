from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

class postreslist(ListView):
    model = models.postres
    
    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.postres.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.postres.objects.all()
        return object_list

class postresdetail(DetailView):
    model = models.postres

class postrescreate(CreateView, LoginRequiredMixin):
    model = models.postres
    form_class = forms.postresform
    success_url = reverse_lazy("postres:postres_list")

class postresupdate(UpdateView, LoginRequiredMixin):
    model = models.postres
    form_class = forms.postresform
    success_url = reverse_lazy("postres:postres_list")

class postresdelete(DeleteView, LoginRequiredMixin):
    model = models.postres
    success_url = reverse_lazy("postres:postres_list")
    
class tiposdepostreslist(ListView):
  model= models.postres
  
  def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.tiposdepostres.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.tiposdepostres.objects.all()
        return object_list

class tiposdepostresdetail(DetailView):
    model = models.tiposdepostres

class tiposdepostrescreate(CreateView, LoginRequiredMixin):
    model = models.tiposdepostres
    form_class = forms.tiposdepostresform
    success_url = reverse_lazy("tiposdepostres:tiposdepostres_list")

class tiposdepostresupdate(UpdateView, LoginRequiredMixin):
    model = models.tiposdepostres
    form_class = forms.tiposdepostresform
    success_url = reverse_lazy("tiposdepostres:tiposdepostres_list")

class tiposdepostresdelete(DeleteView, LoginRequiredMixin):
    model = models.tiposdepostres
    success_url = reverse_lazy("tiposdepostres:tiposdepostres_list")