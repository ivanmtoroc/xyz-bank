# Django
from django.db import models

class AdModel(models.Model):
    name = models.CharField(max_length = 100, null = True)
    description = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'ads/')
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
