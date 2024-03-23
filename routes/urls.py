from django.urls import path
from . import views

app_name = 'router'

urlpatterns = [
    path('', views.home, name='home'),
]
