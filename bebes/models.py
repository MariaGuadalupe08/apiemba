from django.db import models

class Bebe(models.Model):
    imagenBebe = models.ImageField(upload_to='bebes/', null=True, blank=True)
    descripcionBebe = models.TextField()
    imagenFruta = models.ImageField(upload_to='frutas/', null=True, blank=True)
    descripcionFruta = models.TextField()

    def __str__(self):
        return self.descripcionBebe
