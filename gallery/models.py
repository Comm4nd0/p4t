from django.db import models
from services.views import Service
# Create your models here.


class Image(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT, blank=True, null=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return str(self.image)