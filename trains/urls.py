from django.urls import path
from . import views

app_name = 'train'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.TrainCreateView.as_view(), name='add'),
    path('<int:pk>/', views.TrainDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.TrainUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TrainDeleteView.as_view(), name='delete'),
]