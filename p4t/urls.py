from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from paws4thought import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('about/', views.about, name='about'),
                  path('team/', views.team, name='team'),
                  path('services/', include('services.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
