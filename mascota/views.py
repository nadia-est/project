from django.shortcuts import redirect,render
from . import models, forms 

def index(request):
  mascota= models.Mascota.objects.all()
  return render (request,"mascota/index.html",{"mascota":mascota})
# Create your views here.

def crear(request):
    if request.method == "POST":
        form = forms.MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mascota:index")
    else:
        form = forms.MascotaForm()
    return render(request, "mascota/crear.html", {"form": form})