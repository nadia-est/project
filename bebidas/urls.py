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
  
  path("tiposdebebidas/list/",views.tiposdebebidaslist.as_view(), name = "tiposdebebidas_list"),
  path("tiposdebebidas/create/",views.tiposdebebidascreate.as_view(), name = "tiposdebebidas_create"),
  path("tiposdebebidas/detail/<int:pk>",views.tiposdebebidasdetail.as_view(), name = "tiposdebebidas_detail"),
  path("tiposdebebidas/update/<int:pk>",views.tiposdebebidasupdate.as_view(), name = "tiposdebebidas_update"),
  path("tiposdebebidas/delete/<int:pk>",views.tiposdebebidasdelete.as_view(), name = "tiposdebebidas_delete"),
  ]