from django.db import models

# Create your models here.
class Parroquia(models.Model):
    options = (("tipo", "Rural"), ("tipo", "Úrbano"))
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=options)

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"

class Barrio(models.Model):  
    nombre = models.CharField(max_length=100)
    numero_viviendas=models.IntegerField()
    numero_parques=models.IntegerField()
    numero_edificios=models.IntegerField()
    parroquia=models.ForeignKey(Parroquia,on_delete=models.CASCADE, related_name="barrios")

    def __str__(self):
        return  f"{self.nombre} - {self.parroquia}"
   

