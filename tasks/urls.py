from django.urls import path
from tasks.views import *

urlpatterns = [
    path("show-task/", show_task),
    path("user-web/", user_web),
    path("admin-web/", admin_web),
    path("test/", test)
]
