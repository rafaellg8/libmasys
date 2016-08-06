from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
import datetime
from django.core.validators import RegexValidator


class Genero(models.Model):
    nombre = models.CharField(blank=False, max_length=10)

    def get(self):
        return nombre

    def __unicode__(self):
            return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(blank=False, max_length=15)
    apellidos = models.CharField(blank=False, max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telefono = models.CharField(validators=[phone_regex], blank=True,max_length=15) # validators should be a list
    direccion = models.CharField(blank=True,max_length=100)

    def __unicode__(self):
        return self.id_usuario

class Libros(models.Model):
    titulo = models.CharField(blank=False, max_length=100)
    autor = models.CharField(blank=False, max_length=15)
    descripcion = models.CharField(blank=True, max_length=100)
    orden = models.CharField(blank=True, max_length=10)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    edicion = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
            return self.titulo

class Prestamo(models.Model):
    """( Prestamo libros)"""

    fechaInicio = models.DateField(default=datetime.datetime.today)
    fechaFin = models.DateField(default=datetime.datetime.today()+datetime.timedelta(days=7)) #por defecto 7 dias despues de la creacion
    libro = models.ForeignKey(Libros)
    usuarioPrestamo = models.ForeignKey(Usuario)

    def __unicode__(self):
        return self.id_prestamo
