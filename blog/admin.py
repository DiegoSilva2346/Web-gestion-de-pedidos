from django.contrib import admin         
from .models import Post,Categoria

# Register your models here.        
        
class categoriaadmin(admin.ModelAdmin):    
    read_only=('created','updated')         
class postadmin(admin.ModelAdmin):     
    read_only_=('crated','updated')       
admin.site.register(Post,postadmin)        
admin.site.register(Categoria,categoriaadmin)  

