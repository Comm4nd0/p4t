from django.shortcuts import render
from .models import Image, GalleryDetail
from services.views import Service
# Create your views here.

def gallery(request):
    images = Image.objects
    detail = GalleryDetail.objects.first()
    services = Service.objects
    return render(request, 'gallery.html', {'images': images,
                                            'detail': detail,
                                            'services': services})