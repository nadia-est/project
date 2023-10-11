from django.contrib import admin
from . import models



@admin.register(models.bebidas)
class bebidas(admin.ModelAdmin):
  
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
    
# Register your models here.
