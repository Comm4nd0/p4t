from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('<str:service_title>', views.service, name='service'),
]
