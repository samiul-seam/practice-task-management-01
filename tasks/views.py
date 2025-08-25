from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm , TaskModelForm
from tasks.models import *

# Create your views here.
def show_task(request):
    return HttpResponse("this is show task menu.")

def user_web(request):
    return render(request , "dashboard/user_dashboard.html")

def admin_web(request):
    return render(request , "dashboard/admin_dashboard.html")

def test(request):
    return render(request, 'test.html')

def creat_task(request):
    employees = Employee.objects.all()
    form = TaskModelForm()

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():

            """ for model form data """
            form.save()
            return render(request, 'task_form.html' , {"form" : form , "message": "Task Added Successfully"} )

            return HttpResponse("Task Sdded Successfully")

    context = {"form": form}
    return render(request, 'task_form.html' , context)


def view_task(request):
    # select_related (ForeignKey, OneToOneField)
    # tasks = Task.objects.select_related('details').all()
    # tasks = TaskDetail.objects.select_related('task').all()
    # tasks = Task.objects.select_related('project').all()
    """ prefetch_related (reverse Foreignkey, manytomany)"""
    # tasks = Project.objects.all()
    tasks = Task.objects.prefetch_related("assigned_to").all()
    return render(request, "show_task.html", {"tasks": tasks})