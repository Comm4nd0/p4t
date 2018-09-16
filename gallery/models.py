from django.db import models
from services.views import Service
# Create your models here.


class Photo(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT, blank=True, null=True)
    image_800x800 = models.ImageField(blank=True)
    caption = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return str(self.image_800x800)


class GalleryDetail(models.Model):
    page_title = models.CharField(max_length=100, blank=True)
    header_image_1600x660 = models.ImageField(blank=True)

    def __str__(self):
        return self.page_title