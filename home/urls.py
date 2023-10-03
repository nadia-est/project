from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("dueño/", views.index, name="dueño"),
]
urlpatterns += staticfiles_urlpatterns()