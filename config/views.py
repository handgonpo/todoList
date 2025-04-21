# from django.http.response import HttpResponse

# 127.0.0.1:8000/
from django.views import View
from django.shortcuts import render

# def hello_world(request):
#     return HttpResponse("<h1>Hello, World!</h1>")

class HelloWorld(View):
    
    def get(self, request):
        return render(request, "main.html")