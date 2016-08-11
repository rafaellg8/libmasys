from bookstore.models import *

def search(string):
    stringparts = string.split()
    for value in stringparts:
        result = Recurso.objects.filter(titulo__icontains=value) or Recurso.objects.filter(autor__icontains=value) or Recurso.objects.filter( genero__nombre__icontains=value)
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
