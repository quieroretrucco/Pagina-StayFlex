from django.contrib import admin
from APP3 import models


# Registramos los modelos


admin.site.register(models.Departamento)
admin.site.register(models.Propietario)
admin.site.register(models.Huesped)
admin.site.register(models.Estadia)