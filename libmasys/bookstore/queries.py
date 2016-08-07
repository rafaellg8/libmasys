from bookstore.models import *

def search(string):
    querie = Libro.objects.filter(titulo__contains=string) or Libro.objects.filter(autor__contains=string) or Libro.objects.filter( genero__nombre__contains=string)
    return querie

def searchTitle(string):
    querie = Libro.objects.filter(titulo__contains=string)
    return querie

def searchAutor(string):
    querie =  Libro.objects.filter(autor__contains=string)
    return querie

def searchCategory(string):
    querie = Libro.objects.filter( genero__nombre__contains=string)
    return querie
