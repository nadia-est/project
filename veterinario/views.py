from django.shortcuts import redirect, render
from . import models, forms 

def index(request):
  veterinario= models.veterinario.objects.all()
  return render (request,"veterinario/index.html",{"veterinario":veterinario})
# Create your views here.

def crear(request):
    if request.method == "POST":
        form = forms.veterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("veterinario:index")
    else:
        form = forms.veterinarioForm()
    return render(request, "veterinario/crear.html", {"form": form})