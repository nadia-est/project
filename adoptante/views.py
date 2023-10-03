from django.shortcuts import redirect,render
from . import models, forms 

def index(request):
  adoptante= models.Adoptante.objects.all()
  return render (request,"adoptante/index.html",{"adoptante":adoptante})
# Create your views here.
def crear(request):
    if request.method == "POST":
        form = forms.AdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adoptante:index")
    else:
        form = forms.AdoptanteForm()
    return render(request,"adoptante/crear.html", {"form": form})