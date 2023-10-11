from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = "bebidas"

urlpatterns = [
    path("", TemplateView.as_view(template_name="bebidas/index.html"), name="index"),
  ]

urlpatterns += [
  path("bebidas/list/",views.bebidaslist.as_view(), name = "bebidas_list"),
  path("bebidas/create/",views.bebidascreate.as_view(), name = "bebidas_create"),
  path("bebidas/detail/<int:pk>",views.bebidasdetail.as_view(), name = "bebidas_detail"),
  path("bebidas/update/<int:pk>",views.bebidasupdate.as_view(), name = "bebidas_update"),
  path("bebidas/delete/<int:pk>",views.bebidasdelete.as_view(), name = "bebidas_delete"),
  ]