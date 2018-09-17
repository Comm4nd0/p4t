from django.shortcuts import render
from .models import Testimonial, TestimonialDetail
from contact.models import ContactDetail
from services.views import Service
# Create your views here.

def testimonials(request):
    testimonials_detail = TestimonialDetail.objects.first()
    testimonial1 = Testimonial.objects.all()
    contact_details = ContactDetail.objects.first()
    services = Service.objects.all()
    return render(request, 'testimonials.html', {'testimonial_detail': testimonials_detail,
                                                 'testimonials': testimonial1,
                                                 'contact_detail': contact_details,
                                                 'services': services,})