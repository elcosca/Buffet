from django.shortcuts import render
from .models import Productos
#from .models import Cursos
from .models import Pedido
from django.shortcuts import redirect
from .forms import PedidoForm
from django.utils import timezone


def vistainicio(request):
    if request.method == "PEDIDO":
        form = PedidoForm(request.PEDIDO)
    if form.is_valid():
                pedido = form.save(commit=False)
                pedido.author = request.user
                pedido.published_date = timezone.now()
                pedido.save()
                return redirect('boufetapp.views.vistainicio', pk=pedido.pk)
    else:
            form = PedidoForm()
    productos = Productos.objects.all()
    return render(request, 'inicio.html', {'productos': productos, 'form' : form})


def vistaproductos(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def vistapedidos(request):
    pedido = Pedido.objects.all()
    return render(request, 'inicio.html', {'pedido': pedido})


def nuevopedido(request):
        form = PedidoForm()
        return render(request, 'inicio.html', {'form': form})
