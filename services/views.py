from django.shortcuts import render
from .models import Overview, Service

# Create your views here.

def services(request):
    main = Overview.objects.get()
    service = Service.objects
    return render(request, 'services.html', {'main': main,
                                             'service': service})

def daycare(request):
    return render(request, 'daycare.html')

def training(request):
    return render(request, 'training.html')

def training_1_2_1(request):
    return render(request, '1-2-1_training.html')