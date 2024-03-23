from django.shortcuts import render
from django.urls import reverse_lazy
from .models import City
from django.views import generic
from .forms import CityForm
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    cities = City.objects.all()
    paginator = Paginator(cities, 2)
    page = request.GET.get('page')
    cities = paginator.get_page(page)
    return render(request, 'cities/home.html',{'objects_list': cities})


class CityDetailView(generic.DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, generic.CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно создан!'


class CityUpdateView(SuccessMessageMixin ,generic.UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно отредактирован!'


class CityDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно удален!'
