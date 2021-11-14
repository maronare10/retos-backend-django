from django.contrib import admin

# Register your models here.
from .models import Departamento, Edificio, Propietario

admin.site.register(Propietario)
admin.site.register(Edificio)
admin.site.register(Departamento)
