from django.shortcuts import render
from .models import ServicesDetail, Service
from contact.models import ContactDetail
import gallery.models

# Create your views here.

def services(request):
    services = Service.objects
    # try:
    overview = ServicesDetail.objects.first()
    # except ServicesDetail.DoesNotExist:
    #     overview = ''
    service = Service.objects
    contact_details = ContactDetail.objects.first()
    return render(request, 'services.html', {'services': services,
                                             'overview': overview,
                                             'service': service,
                                             'contact_detail': contact_details,})

def service(request, service_title):
    services = Service.objects
    service = Service.objects.get(title=service_title)
    images = gallery.models.Image.objects.filter(service__title=service_title)
    contact_details = ContactDetail.objects.first()
    return render(request, 'service.html', {'services': services,
                                            'service': service,
                                            'images': images,
                                            'contact_detail': contact_details,})
