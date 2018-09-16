from django.contrib import admin
from .models import Service, ServicesPage
# Register your models here.

admin.site.register(ServicesPage)
admin.site.register(Service)