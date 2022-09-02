from django.db import models

class Autos(models.Model):
    marca = models.CharField(max_length=50)
    anio_salida = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.marca+" "+str(self.anio_salida)+" "+self.color


class Motos(models.Model):
    marca = models.CharField(max_length=50)
    anio_salida = models.IntegerField()
    color = models.CharField(max_length=50)

def __str__(self):
        return self.marca+" "+str(self.anio_salida)+" "+self.color

class Bicicletas(models.Model):
    marca = models.CharField(max_length=50)
    anio_salida = models.IntegerField()
    color = models.CharField(max_length=50)

def __str__(self):
        return self.marca+" "+str(self.anio_salida)+" "+self.color