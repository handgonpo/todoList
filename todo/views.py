from __future__ import annotations
from django.shortcuts import render
from .models import Todo

# view 모듈 추가
from django.views import View

def todo_list(request):
    todos = Todo.objects.all()

    return render(request, "todo/todo.html", {"todos": todos})


# Todo 생성 폼 페이지를 보여주는 클래스 기반 뷰
class TodoCreateView(View):

    def get(self, request):
        return render(request, "todo/create.html")


class TodoListView(View):

    def get(self, request):
        # todos = Todo.objects.all()
        return render(request, "todo/list.html")
    

class TodoDetailView(View):

    def get(self, request, pk):
        return render(request, "todo/detail.html")
    

class TodoUpdateView(View):

    def get(self, request, pk):
        return render(request, "todo/update.html")