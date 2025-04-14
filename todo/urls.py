from django.urls import path
from . import views

# 127.0.0.1:8000/todo/
urlpatterns = [
    path("list/", views.todo_list), # 127.0.0.1:8000/todo/list/
]