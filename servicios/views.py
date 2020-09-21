from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.
def  Servicios(request):          
    servicios=Servicio.objects.all()       
    return render(request,"servicios/Servicios.html",{"servicios":servicios})