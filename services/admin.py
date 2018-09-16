from django.contrib import admin
from .models import Service, ServicesDetail
# Register your models here.

admin.site.register(ServicesDetail)
admin.site.register(Service)