from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_task(resquest):
    return HttpResponse("this is show task menu.")

def user_web(request):
    return render(request , "dashboard/user_dashboard.html")

def admin_web(request):
    return render(request , "dashboard/admin_dashboard.html")

def test(request):
    return render(request, 'test.html')
