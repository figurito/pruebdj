from django.db import models

class Personas(models.Model):
    nombre = models.CharField(max_length=15)
    telefono = models.CharField(max_length=12)
    fecha_n = models.DateField()
    email = models.EmailField(max_length=254)
