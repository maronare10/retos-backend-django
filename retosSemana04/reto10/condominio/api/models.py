from django.db import models

# Create your models here.
class Propietario(models.Model):
  nombre = models.CharField(max_length=200)
  dni = models.CharField(max_length=8)
  telefono = models.CharField(max_length=20)
  email = models.EmailField()

  def __str__(self):
        return self.nombre

class Edificio(models.Model):
  nombre = models.CharField(max_length=200)

  def __str__(self):
        return self.nombre

class Departamento(models.Model):
  numero = models.CharField(max_length=20)

  def __str__(self):
        return self.numero
