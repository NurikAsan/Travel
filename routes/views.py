from django.forms import ValidationError
from django.shortcuts import render
from .forms import RouteForm
from django.contrib import messages
from .utils import get_routes


def home(request):
    form = RouteForm()
    return render(request, 'routes/test.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValidationError as er:
                messages.error(request, er)
                return render(request, 'routes/test.html', {'form': form})
            return render(request, 'routes/test.html', context)

        return render(request, 'routes/test.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Not data')
        return render(request, 'routes/test.html', {'form': form})
