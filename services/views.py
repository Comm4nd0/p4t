from django.shortcuts import render
from .models import Overview, Service
import gallery.models

# Create your views here.

def services(request):
    services = Service.objects
    main = Overview.objects.get()
    service = Service.objects
    return render(request, 'services.html', {'services': services,
                                             'main': main,
                                             'service': service})

def service(request, service_title):
    services = Service.objects
    service = Service.objects.get(title=service_title)
    images = gallery.models.Image.objects.filter(service__title=service_title)
    return render(request, 'service.html', {'services': services,
                                            'service': service,
                                            'images': images})
