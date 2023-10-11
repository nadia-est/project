from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = "panificacion"

urlpatterns = [
    path("", TemplateView.as_view(template_name="panificacion/index.html"), name="index"),
  ]

urlpatterns += [
  path("panificacion/list/",views.panificacionlist.as_view(), name = "panificacion_list"),
  path("panificacion/create/",views.panificacioncreate.as_view(), name = "panificacion_create"),
  path("panificacion/detail/<int:pk>",views.panificaciondetail.as_view(), name = "panificacion_detail"),
  path("panificacion/update/<int:pk>",views.panificacionupdate.as_view(), name = "panificacion_update"),
  path("panificacion/delete/<int:pk>",views.panificaciondelete.as_view(), name = "panificacion_delete"),
  
  path("tiposdepan/list/",views.tiposdepanlist.as_view(), name = "tiposdepan_list"),
  path("tiposdepan/create/",views.tiposdepancreate.as_view(), name = "tiposdepan_create"),
  path("tiposdepan/detail/<int:pk>",views.tiposdepandetail.as_view(), name = "tiposdepan_detail"),
  path("tiposdepan/update/<int:pk>",views.tiposdepanupdate.as_view(), name = "tiposdepan_update"),
  path("tiposdepan/delete/<int:pk>",views.tiposdepandelete.as_view(), name = "tiposdepan_delete"),
]
