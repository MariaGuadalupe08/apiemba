from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='exercises/', null=True, blank=True)

    def __str__(self):
        return self.name
