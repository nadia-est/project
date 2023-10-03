from django.urls import path

from . import views

app_name = "veterinario"

urlpatterns = [
    path("", views.index, name="index"),
  path("crear/", views.crear, name="crear"),
]
