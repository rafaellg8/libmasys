from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(User) #quitamos usuarios administracion
admin.site.unregister(Group) #quitamos grupos
# admin.site.unregister(Site)


admin.site.register(Usuario)
admin.site.register(Prestamo)
admin.site.register(Genero)



class RecursoAdmin(admin.ModelAdmin):
    list_display=('titulo','autor','codigo','genero','anio')
    search_fields = ('titulo','autor')


admin.site.register(Recurso,RecursoAdmin)
