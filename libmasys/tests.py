#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','libmasys.settings')

import django
django.setup()

from bookstore.models import Genero,Recurso,Usuario,Prestamo

g = Genero(nombre="Fantastico")
g.save()

g = Genero(nombre="Histórico")
g.save()

g = Genero(nombre="Novela")
g.save()

g = Genero(nombre="Idiomas")
g.save()

g = Genero(nombre="Infantil")
g.save()

g = Genero(nombre="Adulto")
g.save()

g = Genero(nombre="Ciencia Ficcion")
g.save()

g = Genero(nombre="Documental")
g.save()

g = Genero(nombre="Aventuras")
g.save()

g = Genero(nombre="Acción")
g.save()


"""

usuarios

"""

usuario = Usuario(nombre="Pepito",apellidos="Perez Perez",telefono="123456789",direccion="Calle Hola Mundo")


"""

Recursos

"""

genero = Genero.objects.get(nombre="Novela")
recurso = Recurso(titulo="Don Quijote de la Mancha", autor="Miguel de Cervantes",descripcion="",genero=genero)
recurso.save()



genero = Genero.objects.get(nombre="Infantil")
recurso = Recurso(titulo="Dartacan y los tres mosqueteros", autor="Disney",descripcion="",genero=genero,dvd=True)
recurso.save()

genero = Genero.objects.get(nombre="Infantil")
recurso = Recurso(titulo="Doraemon", autor="Disney",descripcion="",genero=genero,dvd=True)
recurso.save()
"""

class Genero(models.Model):
    nombre = models.CharField(blank=False, max_length=10)

    def get(self):
        return nombre

    def __unicode__(self):
            return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(blank=False, max_length=15)
    apellidos = models.CharField(blank=False, max_length=30)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Telefono debe ser formato: 99911122.")
    telefono = models.CharField(validators=[phone_regex], blank=True,max_length=15) # validators should be a list
    direccion = models.CharField(blank=True,max_length=100)

    def __unicode__(self):
            return self.nombre+" "+self.apellidos

class Recurso(models.Model):
    titulo = models.CharField(blank=False, max_length=100)
    autor = models.CharField(blank=True, max_length=15)
    descripcion = models.CharField(blank=True, max_length=100)
    orden = models.CharField(blank=True, max_length=10)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    edicion = models.IntegerField(blank=True, null=True)
    dvd = models.BooleanField(default=False)
    def __unicode__(self):
            return self.titulo

class Prestamo(models.Model):

    fechaInicio = models.DateField(default=datetime.datetime.today)
    fechaFin = models.DateField(default=datetime.datetime.today()+datetime.timedelta(days=7)) #por defecto 7 dias despues de la creacion
    Recurso = models.OneToOneField(Recurso,unique=True)
    usuarioPrestamo = models.OneToOneField(Usuario,unique=True)

    def __unicode__(self):
        return self.fechaFin.strftime("%Y-%m-%d")+" "+self.Recurso.__unicode__()+" "+self.usuarioPrestamo.__unicode__()
"""
