from django.shortcuts import render
from .models import Todo

# view 모듈 추가
from django.views import View

def todo_list(request):
    todos = Todo.objects.all()

    return render(request, "todo/todo.html", {"todos": todos})


# create Test
class TodoCreateView(View):

    def get(self, request):
        return render(request, "todo/create.html")