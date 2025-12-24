from django.shortcuts import render ,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import Register, NewTask
from .models import Task
from datetime import datetime


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = Register()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == "post" :
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            un = form.cleaned_data.get("username")
            pw = form.cleaned_data.get("password")
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                return render(request, 'message.html', {'message':'logged'})
        else:
            return render(request, 'message.html', {'message':'something bad'})

    else:
        form = AuthenticationForm()
    return render (request, "login.html", {"form": form})
def tasks(request):
    taskss = Task.objects.all()
    ct = {"tasks":taskss}
    return render(request, 'tasks.html',ct)

@login_required
def newTask(request):
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get("title")
            description = data.get("description")
            status = data.get("completed")
            created = datetime.now()
            task = Task(title=title, description=description, completed=status, created=created)
            task.save()
            return redirect("tasks")
        else:
            return render(request, 'nt.html', {'form':form} )


def message(request):
    mj = 'any'
    return render(request, 'message.html', {'message':mj})
