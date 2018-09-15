from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from services.models import Service, Overview
import json

# Create your views here.
def home(request):
    services = Service.objects
    try:
        overview = Overview.objects.get()
    except Overview.DoesNotExist:
        overview = ''
    return render(request, 'home.html', {'overview': overview,
                                         'services': services})

def about(request):
    services = Service.objects
    return render(request, 'about.html', {'services': services})

def team(request):
    services = Service.objects
    return render(request, 'team.html', {'services': services})

def contact_form(request):
    if request.POST:

        email = EmailMessage(
            request.POST.get('subject'),
            "{}, {}".format(request.POST.get('message'), request.POST.get('message')),
            'contact@cmdlb.com',
            ['claire@paws4thoughtdogs.com'],
            reply_to=[request.POST['email']],
        )
        try:
            email.send(fail_silently=False)
            message = {'message': "Thank you for your email, we'll be in touch soon!"}
        except:
            message = {'message': "Something went wrong, but we're working on it!"}

        return HttpResponse(json.dumps(message), content_type='application/json')