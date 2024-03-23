from django.shortcuts import render
from .forms import RouteForm
from django.contrib import messages


def home(request):
    form = RouteForm()
    return render(request, 'routes/test.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
    else:
        form = RouteForm()
        messages.error(request, 'Not data')
        return render(request, 'routes/test.html', {'form': form})