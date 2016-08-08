import django

from bookstore.models import *


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
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Telefono debe ser: 123456789.")
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

    def __unicode__(self):
            return self.titulo

class Prestamo(models.Model):

    fechaInicio = models.DateField(default=datetime.datetime.today)
    fechaFin = models.DateField(default=datetime.datetime.today()+datetime.timedelta(days=7)) #por defecto 7 dias despues de la creacion
    Recurso = models.OneToOneField(Recurso,unique=True)
    usuarioPrestamo = models.OneToOneField(Usuario,unique=True)

    def __unicode__(self):
        return self.fechaFin.strftime("%Y-%m-%d")+" "+self.Recurso.__unicode__()+" "+self.usuarioPrestamo.__unicode__()
