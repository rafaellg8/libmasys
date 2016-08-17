#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bookstore.models import *

def search(string):
    stringparts = string.split()
    i = 0
    for value in stringparts:
        if (Recurso.objects.filter(titulo__icontains=value) and Recurso.objects.filter(autor__icontains=value)):
            result = Recurso.objects.filter(titulo__icontains=value) and Recurso.objects.filter(autor__icontains=value)
        else:
            result = (Recurso.objects.filter(titulo__icontains=value) or Recurso.objects.filter(autor__icontains=value) or Recurso.objects.filter(genero__nombre__icontains=value) or Recurso.objects.filter(editorial__icontains=value))
    return result

def searchTitle(string):
    result = Recurso.objects.filter(titulo__icontains=string)
    return result

def searchAutor(string):
    result =  Recurso.objects.filter(autor__icontains=string)
    return result

def searchCategory(string):
    result = Recurso.objects.filter( genero__nombre__icontains=string)
    return result
