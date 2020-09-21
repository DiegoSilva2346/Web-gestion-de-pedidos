from django.db import models

# Create your models here.
class tienda(models.Model):   
    producto=models.CharField(max_length=20)         
    descripcion_producto=models.CharField(max_length=120)            
    foto=models.ImageField(upload_to='tienda')         
    created=models.DateTimeField(auto_now_add=True)   
    updated=models.DateTimeField(auto_now_add=True)           
    class Meta:    
        verbose_name='tienda'   
        verbose_name_plural='tiendas'     
    def ___str___(self):    
        return self.producto    
     
  