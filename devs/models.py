from django.db import models

class Dev(models.Model):
    fotodev = models.ImageField(upload_to='devs/', null=True, blank=True)
    nombredev = models.TextField()
    apellidodev = models.TextField()
    numerodev = models.TextField()
    nocontroldev = models.TextField()
    correoddev = models.TextField()

    def __str__(self):
        return self.nombredev
