from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = "bebidas"

urlpatterns = [
    path("", TemplateView.as_view(template_name="bebidas/index.html"), name="index"),
  ]
