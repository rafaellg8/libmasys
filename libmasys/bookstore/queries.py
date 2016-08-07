from bookstore.models import *

def search(string):
    stringparts = string.split()
    for value in stringparts or querie.count()>0:
        querie = Recurso.objects.filter(titulo__contains=value) or Recurso.objects.filter(autor__contains=value) or Recurso.objects.filter( genero__nombre__contains=value)
    return querie

def searchTitle(string):
    querie = Recurso.objects.filter(titulo__contains=string)
    return querie

def searchAutor(string):
    querie =  Recurso.objects.filter(autor__contains=string)
    return querie

def searchCategory(string):
    querie = Recurso.objects.filter( genero__nombre__contains=string)
    return querie
