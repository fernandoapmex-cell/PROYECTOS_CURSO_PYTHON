from django.contrib import admin

from personas.models import Persona, Domicilio

# Register your models here.
#registramos la persona para que se vea en la consola
admin.site.register(Persona)
admin.site.register(Domicilio)
