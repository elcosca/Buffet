from django import forms
#from .models import Productos
#from .models import Cursos
#from .models import Aula
from .models import Pedido


class PedidoForm(forms.ModelForm):

        class Meta:
            model = Pedido
            fields = ('id_del_pedido', 'nombre_del_alumno', 'nombre_del_curso', 'milanesaCantidad', 'coca_colaCantidad', 'tartinCantidad', 'laysCantidad', 'horario_de_entrega', 'aula_de_entrega')


