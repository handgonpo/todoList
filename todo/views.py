from django.shortcuts import render
from .models import Todo


def todo_list(request):
    # return HttpResponse("Todo list")
    todos = Todo.objects.all()

    return render(request, "todo/todo.html", {"todos": todos})