from django.shortcuts import render

# Create your views here.

def services(request):
    return render(request, 'services.html')

def daycare(request):
    return render(request, 'daycare.html')

def training(request):
    return render(request, 'training.html')

def training_1_2_1(request):
    return render(request, '1-2-1_training.html')