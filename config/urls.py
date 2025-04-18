from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # 첫페이지 추가
    path("", views.hello_world), # 127.0.0.1:8000/

    path('admin/', admin.site.urls),
    path("todo/", include("todo.urls")), # 127.0.0.1:8000/todo/
]
