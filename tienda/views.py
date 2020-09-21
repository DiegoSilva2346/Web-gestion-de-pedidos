from django.shortcuts import render
from tienda.models import tienda         
from django.core.mail import send_mail    
from django.conf import settings
# Create your views here.
def  Tienda(request):        
    tiendas=tienda.objects.all()                
    if request.method == "POST": 
        subject=request.POST["nombre"]   
        message= request.POST["nombredelacaja"] + " " + request.POST["email"]      
        email_from= settings.EMAIL_HOST_USER     
        recipient_list=["diego_241192@hotmail.com"]    
        send_mail(subject,message,email_from,recipient_list)
  
    return render(request,"tienda/Tienda.html",{"tiendas":tiendas})    