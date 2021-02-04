from django.db import models


# Create your models here.
class Modulo(models.Model):
    titulo = models.CharField(max_length=64)

    def __str__(self):
        return self.titulo