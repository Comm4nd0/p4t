from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from services.models import Service, ServicesDetail
from .models import Feature, CompanyDetail, TeamMember, TeamDetail, Banner
from contact.models import ContactDetail
import json

# Create your views here.
def home(request):
    services = Service.objects
    try:
        overview = ServicesDetail.objects.first()
    except ServicesDetail.DoesNotExist:
        overview = ''
    try:
        company = CompanyDetail.objects.first()
    except CompanyDetail.DoesNotExist:
        company = ''

    features = Feature.objects

    contact_details = ContactDetail.objects.first()

    banners = Banner.objects
    return render(request, 'home.html', {'overview': overview,
                                         'services': services,
                                         'company': company,
                                         'features': features,
                                         'contact_detail': contact_details,
                                         'banners': banners})

def company(request):
    services = Service.objects
    try:
        company = CompanyDetail.objects.first()
    except CompanyDetail.DoesNotExist:
        company = ''

    features = Feature.objects
    return render(request, 'company.html', {'services': services,
                                            'company': company,
                                            'features': features})

def team(request):
    services = Service.objects
    members = TeamMember.objects
    try:
        teampage = TeamDetail.objects.first()
    except TeamDetail.DoesNotExist:
        teampage = ''
    return render(request, 'team.html', {'services': services,
                                         'members': members,
                                         'teampage': teampage})

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