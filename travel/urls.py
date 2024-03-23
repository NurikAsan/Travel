from django.contrib import admin
from django.urls import path, include
from . import views
from routes.views import find_routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cities/', include('cities.urls', 'city')),
    path('trains/', include('trains.urls', 'train')),
    path('find/', find_routes, name='find_routes'),
]
