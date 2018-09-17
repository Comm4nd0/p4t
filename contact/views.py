from django.shortcuts import render
from .models import ContactDetail
from services.views import Service


def contact(request):
    contact_details = ContactDetail.objects.first()
    services = Service.objects.all()
    return render(request, 'contact.html', {'contact_detail': contact_details,
                                            'services': services,})