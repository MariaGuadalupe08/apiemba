from django.db import models

class Mama(models.Model):
    descripcionMama = models.TextField()
    imagenSintoma = models.ImageField(upload_to='sintomas/', null=True, blank=True)
    descripcionSintoma = models.TextField()

    def _str_(self):
        return self.descripcionMama