from django.urls import path        
from . import views        
#from django.conf import settings
#from django.conf.urls.static import static
urlpatterns = [
              
    path('',views.Blog,name="Blog"),          
            
    path('programacion/',views.programacion,name="programacion"),       
    path('Nacionales/',views.nacionales,name="Nacionales"),       
    path('Internacionales/',views.internacionales,name="Internacionales"),             
   
      
      
       
   
]
