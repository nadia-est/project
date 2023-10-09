from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from . import forms


# Create your views here.
def index(request):
  return render (request,"home/index.html")

def about(request): 
  return render(request,"home/about.html")


def login_request(request):
  if request.method == "POST":
    form= forms.CustomAuthenticationForm(request, data= request.POST)
    if form.is_valid():
      usuario = form.cleaned_data.get("username")
      contraseña = form.cleaned_data.get("password")
      
      user = authenticate(username=usuario,password=contraseña)
      if user is not None:
        
        login(request,user)
        return render (request,"home/index.html", {"mensaje": f"se ha logueado correctamente"})
  else:
     form= AuthenticationForm()
     return render (request, "home/login.html", {"form": form})
     


      
    
  