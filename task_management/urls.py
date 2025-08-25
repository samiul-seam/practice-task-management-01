
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/", include("tasks.urls")),
    path("creat-task/", creat_task),
    path('view-task/', view_task)
] + debug_toolbar_urls()
