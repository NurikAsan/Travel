from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Train
from .forms import TrainForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 2)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html',{'objects_list': trains})


class TrainListView(generic.ListView):
    model = Train
    template_name = 'trains/home.html'
    paginate_by = 3
    context_object_name = 'objects_list'


class TrainDetailView(generic.DetailView):
    model = Train
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, generic.CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_message = 'Поезд создан!'
    success_url = reverse_lazy('train:home')


class TrainUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_message = 'Поезд обновлен!'
    success_url = reverse_lazy('train:home')
    

class TrainDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_message = 'Поезд удален!'
    success_url = reverse_lazy('train:home')
