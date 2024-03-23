from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cities/', include('cities.urls', 'city')),
    path('trains/', include('trains.urls', 'train')),
    path('routes/', include('routes.urls', 'router')),
]
