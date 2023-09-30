from django.http import HttpResponse
from django.shortcuts import render
from .models import Registro

# Create your views here.
def index(request):
    registro = Registro.objects.all()
    
    return render(
        request,
        'index.html',
        context={'formulario': registro}
    )

def detalle(request, producto_id):
    return HttpResponse(producto_id)
