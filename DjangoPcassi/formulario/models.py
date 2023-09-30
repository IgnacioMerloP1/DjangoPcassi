from django.db import models
from django.utils import timezone
# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    producto = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    insumo_instalado = models.CharField(max_length=255)
    so = models.CharField(max_length=255)
    memoria = models.CharField(max_length=255)
    procesador = models.CharField(max_length=255)
    antivirus = models.CharField(max_length=255)
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    vence = models.DateTimeField()
    
    def __str__(self):
        return self.empresa
    