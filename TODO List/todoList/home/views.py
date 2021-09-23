from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    if (request.method == "POST"):
        task_name = request.POST['task_name']
        date = request.POST['date']
        desc = request.POST['desc']

        ins = Task(task_name = task_name, date = date, desc = desc)
        ins.save()
        print("Data is save into the database.")

    return render(request, "home.html")

    
def task(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, "task.html", context)