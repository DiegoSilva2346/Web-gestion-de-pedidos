from django.shortcuts import render      
from .models import Post,Categoria

# Create your views here.
def  Blog(request):       
                
    posts=Post.objects.all()          
          
     
        


     
    return render(request,"blog/Blog.html",{"posts":posts})             


def  programacion(request):       
    posts=Post.objects.filter(categoria=Categoria.objects.get(nombre='programacion'))            
             
    

          

    return render(request,"blog/programacion.html",{"posts":posts})                 
def  nacionales(request):       
    posts=Post.objects.filter(categoria=Categoria.objects.get(nombre='Nacionales'))  
       
    
          

    return render(request,"blog/nacionales.html",{"posts":posts})            
def  internacionales(request):       
    posts=Post.objects.filter(categoria=Categoria.objects.get(nombre='Internacionales'))         
      
    

          

    return render(request,"blog/internacionales.html",{"posts":posts})            
             
