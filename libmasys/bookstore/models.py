#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
import datetime
from django.core.validators import RegexValidator

class Genero(models.Model):
    nombre = models.CharField(blank=False, max_length=100,primary_key=True,unique=True)

    def get(self):
        return nombre

    def __unicode__(self):
            return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(blank=False, max_length=15)
    apellidos = models.CharField(blank=False, max_length=30)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Telefono debe ser: 123456789.")
    telefono = models.CharField(validators=[phone_regex], blank=True,max_length=15) # validators should be a list
    direccion = models.CharField(blank=True,max_length=100)

    def __unicode__(self):
            return self.nombre+" "+self.apellidos

class Recurso(models.Model):
    titulo = models.CharField(blank=False, max_length=100)
    autor = models.CharField(blank=False, max_length=100)
    descripcion = models.CharField(blank=True, max_length=250)
    codigo = models.CharField(blank=True, max_length=10,unique=True)
    estanteria = models.CharField(blank=True, max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    anio = models.IntegerField(blank=True, null=True)
    editorial = models.CharField(blank=True, max_length=250)
    dvd = models.BooleanField(default=False)

    def __unicode__(self):
            return self.titulo


class Prestamo(models.Model):
    """( Prestamo Recursos)"""
    fechaInicio = models.DateField(default=datetime.datetime.today)
    fechaFin = models.DateField(default=datetime.datetime.today()+datetime.timedelta(days=7)) #por defecto 7 dias despues de la creacion
    Recurso = models.OneToOneField(Recurso,unique=True)
    usuarioPrestamo = models.OneToOneField(Usuario,unique=True)

    def __unicode__(self):
        return self.fechaFin.strftime("%Y-%m-%d")+" "+self.Recurso.__unicode__()+" "+self.usuarioPrestamo.__unicode__()
