from django.shortcuts import render
from .models import Testimonial, TestimonialDetail
# Create your views here.

def testimonials(request):
    testimonials_detail = TestimonialDetail.objects.first()
    testimonial1 = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonial_detail': testimonials_detail,
                                                 'testimonials': testimonial1})