from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_title = "pan"
admin.site.site_header = "panaderia"


@admin.register(models.panificacion)
class panificacion(admin.ModelAdmin):
  
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
    
@admin.register(models.tiposdepan)
class tiposdepan(admin.ModelAdmin):
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
