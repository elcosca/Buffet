from django.db import models
from django.utils import timezone


class Productos (models.Model):
    nombre_del_producto = models.CharField(max_length=200)
    id_del_producto = models.IntegerField()
    precio = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_del_producto


class Cursos (models.Model):
    nombre_del_curso = models.CharField(max_length=15)
    horario_almuerzo = models.DateTimeField(default=timezone.now)
    aula = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_del_curso


class Aula (models.Model):
    piso = models.IntegerField()
    aula = models.CharField(max_length=1)

    def __str__(self):
        return self.aula + " " + str(self.piso)


class Pedido (models.Model):
    id_del_pedido = models.CharField(max_length=20)
    nombre_del_alumno = models.CharField(max_length=20)
    nombre_del_curso = models.ForeignKey('Cursos')
    #nombre_del_producto = models.ForeignKey('Productos')
    milanesaCantidad = models.CharField(max_length=20)
    coca_colaCantidad = models.CharField(max_length=20)
    tartinCantidad = models.CharField(max_length=20)
    laysCantidad = models.CharField(max_length=20)
    horario_de_entrega = models.DateTimeField(default=timezone.now)
    aula_de_entrega = models.ForeignKey('Aula')

    def __str__(self):
        return self.id_del_pedido
