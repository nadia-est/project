from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from . import forms

def index(request):
  return render (request,"home/index.html")

def about(request): 
  return render(request,"home/about.html")

     


      
    
  