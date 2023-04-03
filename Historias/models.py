from django.db import models

# Create your models here.
class Tabla(models.Model):#Se herada de models para poder tener todas las caracteristicas de un modelo
    #propiedades asociadas a los campos de una tabla
    #Ejemplos
    #id = models.IntegerField(primary_key=True,null=False,auto_created=True)
    atributo1 = models.CharField(max_length = 60)
    atributo2 = models.CharField(max_length = 60)
    atributo3 = models.IntegerField(default = 0)
    atributo4 = models.IntegerField(default = 0)