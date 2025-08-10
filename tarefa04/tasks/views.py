from django.shortcuts import render
from .models import Task
from datetime import date

def task_list(request):
    tasks = Task.objects.all()
    today = date.today()
    context = {
        'tasks': tasks,
        'hoje': today,
    }
    return render(request, 'tasks/listaTarefa.html', context)