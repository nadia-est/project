from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_title = "postre"
admin.site.site_header = "postres"

@admin.register(models.postres)
class postres(admin.ModelAdmin):
  
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
    
@admin.register(models.tiposdepostres)
class tiposdepostres(admin.ModelAdmin):
    list_display = (
        "nombre",
        "cantidad",
        "precio",
        "descripcion",
        "fecha_actualizacion",
    ) 
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("categoria","nombre",)
    list_filter = ("categoria",)
    date_hierarchy = ("fecha_actualizacion")
