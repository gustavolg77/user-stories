from django.db import models

# Create your models here.
class Usuario(models.Model):
    cod_usu = models.IntegerField(primary_key=True,null=False,auto_created=True)
    nombre_usu = models.CharField(null=False,max_length=20)
    clave_usu = models.CharField(null=False,max_length=20)

class Proyecto(models.Model):
    cod_pro = models.IntegerField(primary_key=True,null=False,auto_created=True)
    nombre_pro = models.CharField(null=False,max_length=20)
    cantidad_pro = models.IntegerField(default=0,null=False)
    usuario_pro = None

class Historia_Usuario(models.Model):
    cod_his_usu = models.IntegerField(primary_key=True,null=False,auto_created=True)
    numero_his_usu = models.IntegerField(default=0,null=False)
    titulo_his_usu = models.CharField(null=False,max_length=20)

class Version(models.Model):
    cod_ver = models.IntegerField(primary_key=True,null=False,auto_created=True)
    role_ver = models.CharField(null=False,max_length=20)
    objetivo_ver = models.CharField(null=False,max_length=20)
    motivo_ver = models.CharField(null=False,max_length=40)
    codiciones_ver = models.CharField(null=False,max_length=250)
    nro_ver = models.IntegerField(null=False,auto_created=True)
    historia_usuario_ver = None
