from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

# home page


def index(request):
    # Task is the class created in Models.py which is used to store different tasks
    tasks = Task.objects.all()

    form = TaskForm()  # TaskForm is the class created in forms.py which is used to create a form
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


# update page
def updateTask(request, pk):  # here,pk is the primary key we use for id
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):

    Item = Task.objects.get(id=pk)

    if request.method == 'POST':
        Item.delete()
        return redirect('/')

    context = {'Item': Item}
    return render(request, 'tasks/delete.html', context)
