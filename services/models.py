from django.db import models

# Create your models here.


class Overview(models.Model):
    sub_heading = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True)
    body = models.TextField(blank=True)
    bullets1 = models.CharField(max_length=100, blank=True)
    bullets2 = models.CharField(max_length=100, blank=True)
    bullets3 = models.CharField(max_length=100, blank=True)
    bullets4 = models.CharField(max_length=100, blank=True)
    bullets5 = models.CharField(max_length=100, blank=True)
    bullets6 = models.CharField(max_length=100, blank=True)
    bullets7 = models.CharField(max_length=100, blank=True)
    bullets8 = models.CharField(max_length=100, blank=True)
    bullets9 = models.CharField(max_length=100, blank=True)
    bullets10 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.sub_heading

class Service(models.Model):
    title = models.CharField(max_length=100, blank=True)
    sub_title = models.CharField(max_length=100, blank=True)
    header_image = models.ImageField(blank=True)
    body = models.TextField(blank=True)

    bullets1 = models.CharField(max_length=100, blank=True)
    bullets2 = models.CharField(max_length=100, blank=True)
    bullets3 = models.CharField(max_length=100, blank=True)
    bullets4 = models.CharField(max_length=100, blank=True)
    bullets5 = models.CharField(max_length=100, blank=True)
    bullets6 = models.CharField(max_length=100, blank=True)
    bullets7 = models.CharField(max_length=100, blank=True)
    bullets8 = models.CharField(max_length=100, blank=True)
    bullets9 = models.CharField(max_length=100, blank=True)
    bullets10 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title