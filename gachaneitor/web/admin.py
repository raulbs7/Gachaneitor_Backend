from django.contrib import admin
from .models import Receta, Ingrediente, Paso

# Register your models here.
admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(Paso)