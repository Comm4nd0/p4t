from django.db import models

# Create your models here.


class Overview(models.Model):
    sub_heading = models.CharField(max_length=100, blank=True)
    header_image_1600x660 = models.ImageField(blank=True)
    image_800x800 = models.ImageField(blank=True)
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
    header_image_1600x660 = models.ImageField(blank=True)
    main_image_500x400 = models.ImageField(blank=True)
    sub_title = models.CharField(max_length=100, blank=True)
    intro_bold_text = models.TextField(blank=True)
    body = models.TextField(blank=True)

    bullet_title = models.CharField(max_length=100, blank=True)
    bullets1 = models.CharField(max_length=100, blank=True)
    bullets1_body = models.TextField(blank=True)
    bullets2 = models.CharField(max_length=100, blank=True)
    bullets2_body = models.TextField(blank=True)
    bullets3 = models.CharField(max_length=100, blank=True)
    bullets3_body = models.TextField(blank=True)
    bullets4 = models.CharField(max_length=100, blank=True)
    bullets4_body = models.TextField(blank=True)
    bullets5 = models.CharField(max_length=100, blank=True)
    bullets5_body = models.TextField(blank=True)
    bullets6 = models.CharField(max_length=100, blank=True)
    bullets6_body = models.TextField(blank=True)
    bullets7 = models.CharField(max_length=100, blank=True)
    bullets7_body = models.TextField(blank=True)
    bullets8 = models.CharField(max_length=100, blank=True)
    bullets8_body = models.TextField(blank=True)
    bullets9 = models.CharField(max_length=100, blank=True)
    bullets9_body = models.TextField(blank=True)
    bullets10 = models.CharField(max_length=100, blank=True)
    bullets10_body = models.TextField(blank=True)

    def __str__(self):
        return self.title