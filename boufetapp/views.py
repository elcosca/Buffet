from django.shortcuts import render
from .models import Productos
#from .models import Cursos
from .models import Pedido
from django.shortcuts import redirect
from .forms import PedidoForm
from django.utils import timezone



def vistainicio(request):
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
        if form.is_valid():
                Pedido = form.save(commit=False)
                Pedido.author = request.user
                Pedido.published_date = timezone.now()
                Pedido.save()
                return redirect('buffetapp.views.nuevopedido', pk=Pedido.pk)
        else:
            form = PedidoForm()
        return render(request, 'buffetapp/inicio.html', {'form': form})