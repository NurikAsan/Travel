from django.contrib import admin
from django.urls import path
from . import views

app_name = 'city'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.CityCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.CityUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CityDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.CityDetailView.as_view(), name='detail'),
]
