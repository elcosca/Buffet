from django.shortcuts import render
from .models import Productos
#from .models import Cursos
#from .models import Pedidos
#from django.shortcuts import redirect


def vistainicio(request):
    productos = Productos.objects.all()
    return render(request, 'inicio.html', {'productos': productos})


def vistaproductos(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos})


