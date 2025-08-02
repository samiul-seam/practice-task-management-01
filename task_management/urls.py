
from django.contrib import admin
from django.urls import path, include
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home),
    path("tasks/", include("tasks.urls")),
    path('this/', this),
    path('show-task/<int:id>/', show_specific_task)
]
