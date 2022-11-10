from django.db import models
# Create your models here.
class Entrada(models.Model):
    nombre= models.CharField(max_length=50)
    contenido = models.TextField(max_length=1000)
    imagen=models.URLField()
    autor=models.CharField(max_length=50)

    def __str__(self) :
        return  self.nombre