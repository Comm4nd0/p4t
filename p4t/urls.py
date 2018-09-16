from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from paws4thought import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('The Company/', views.company, name='company'),
                  path('The Team/', views.team, name='team'),
                  path('services/', include('services.urls')),
                  path('gallery/', include('gallery.urls')),
                  path('contact_form/', views.contact_form, name='contact_form'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
