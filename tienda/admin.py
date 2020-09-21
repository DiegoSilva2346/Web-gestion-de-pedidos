from django.contrib import admin        
from .models import tienda       


# Register your models here.         
class TiendaAdmin(admin.ModelAdmin) :    
    readonly_fields=('created','updated')     
admin.site.register(tienda,TiendaAdmin)
