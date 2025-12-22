from django.shortcuts import render
from .forms import Register


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration_success.html')
    else:
        form = Register()
    return render(request, 'register.html', {'form': form})
