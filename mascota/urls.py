from django.urls import path

from . import views

app_name = "mascota"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear/", views.crear, name="crear"),
]
