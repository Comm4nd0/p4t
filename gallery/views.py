from django.shortcuts import render
from .models import Image, GalleryDetail
from contact.models import ContactDetail
from services.views import Service
# Create your views here.

def gallery(request):
    images = Image.objects
    detail = GalleryDetail.objects.first()
    services = Service.objects
    contact_details = ContactDetail.objects.first()
    return render(request, 'gallery.html', {'images': images,
                                            'detail': detail,
                                            'services': services,
                                            'contact_detail': contact_details,})