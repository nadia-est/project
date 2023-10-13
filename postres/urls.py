from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = "postres"

urlpatterns = [
    path("", TemplateView.as_view(template_name="postres/index.html"), name="index"),
  ]

urlpatterns += [
  path("postres/list/",views.postreslist.as_view(), name = "postres_list"),
  path("postres/create/",views.postrescreate.as_view(), name = "postres_create"),
  path("postres/detail/<int:pk>",views.postresdetail.as_view(), name = "postres_detail"),
  path("postres/update/<int:pk>",views.postresupdate.as_view(), name = "postres_update"),
  path("postres/delete/<int:pk>",views.postresdelete.as_view(), name = "postres_delete"),
  
  path("tiposdepostres/list/",views.tiposdepostreslist.as_view(), name = "tiposdepostres_list"),
  path("tiposdepostres/create/",views.tiposdepostrescreate.as_view(), name = "tiposdepostres_create"),
  path("tiposdepostres/detail/<int:pk>",views.tiposdepostresdetail.as_view(), name = "tiposdepostres_detail"),
  path("tiposdepostres/update/<int:pk>",views.tiposdepostresupdate.as_view(), name = "tiposdepostres_update"),
  path("tiposdepostres/delete/<int:pk>",views.tiposdepostresdelete.as_view(), name = "tiposdepostres_delete"),
]
