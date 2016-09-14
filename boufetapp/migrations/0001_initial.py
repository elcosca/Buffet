# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre_del_curso', models.CharField(max_length=15)),
                ('horario_almuerzo', models.DateTimeField(default=django.utils.timezone.now)),
                ('aula', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('id_del_pedido', models.IntegerField()),
                ('nombre_del_alumno', models.CharField(max_length=20)),
                ('nombre_del_curso', models.ForeignKey(to='boufetapp.Cursos')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre_del_producto', models.CharField(max_length=200)),
                ('id_del_producto', models.IntegerField()),
                ('precio', models.CharField(max_length=200)),
                ('stock', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='nombre_del_producto',
            field=models.ForeignKey(to='boufetapp.Productos'),
        ),
    ]
