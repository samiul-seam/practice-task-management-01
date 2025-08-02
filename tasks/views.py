from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is return http Server.")

def show_task(resquest):
    return HttpResponse("this is show task menu.")

def this(request):
    return render(request , "index.html")

def show_specific_task(request, id):
    print(id)
    print('id type' , type(id))
    return HttpResponse (f"this is specific task id : {id}")