from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('day_care/', views.daycare, name='day care'),
    path('training/', views.training, name='training'),
    path('1-2-1_training/', views.training_1_2_1, name='1-2-1 training'),
]
