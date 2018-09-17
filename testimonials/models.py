from django.db import models
from services.models import Service
# Create your models here.

class TestimonialDetail(models.Model):
    sub_title = models.CharField(max_length=100, blank=True)
    header_image_1600x660 = models.ImageField(blank=True)
    image_690x500 = models.ImageField(blank=True)
    body = models.TextField(blank=True)
    body2 = models.TextField(blank=True)

class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, blank=True, null=True)
    body = models.TextField(blank=True)
    image_100x100 = models.ImageField(blank=True)

    def __str__(self):
        return self.name
