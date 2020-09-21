from django.shortcuts import render,HttpResponse             
from django.conf import settings     
from django.core.mail import send_mail 


# Create your views here.

def  Home(request):          
    return render(request,"ProyectoWebApp/Home.html")




#def  Blog(request):          
   # return render(request,"ProyectoWebApp/Blog.html")
def  Contacto(request):         
    if request.method == "POST":           
        subject=request.POST["nombre"]   
        message= request.POST["nombredelacaja"] + " " + request.POST["email"]      
        email_from= settings.EMAIL_HOST_USER     
        recipient_list=["diego_241192@hotmail.com"]    
        send_mail(subject,message,email_from,recipient_list)

    return render(request,"ProyectoWebApp/Contacto.html")
