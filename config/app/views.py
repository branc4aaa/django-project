from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import Register, NewTask, UpdateTask
from .models import Task
from datetime import datetime
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration_success.html')
    else:
        form = Register()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST" :
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            un = form.cleaned_data.get("username")
            pw = form.cleaned_data.get("password")
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                return redirect('tasks')
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
    else:
        form = NewTask()
        return render(request, 'nt.html', {'form':form} )


def message(request):
    mj = 'any'
    return render(request, 'message.html', {'message':mj})

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def updateTask_view(request, tid):
    task = get_object_or_404(Task, id=tid)
    if request.method == "POST":
        form = UpdateTask(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task.title = data.get("title")
            task.description = data.get("description")
            task.completed = data.get("completed")
            task.save()
            return redirect("tasks")
        else:
            return render(request, 'update_task.html', {'form':form, 'task':task, 'message':"error"} )
    else:
        form = UpdateTask(initial={
            'title': task.title,
            'description': task.description,
            'completed': task.completed
        })
        return render(request, 'update_task.html', {'form':form, 'task':task} )
    

@login_required
def deleteTask_view(request, tid):
    task = get_object_or_404(Task, id=tid)
    task.delete()
    return redirect("tasks")