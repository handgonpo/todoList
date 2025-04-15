from django.urls import path
from .apis import *
from . import views  # views 모듈을 통째로 임포트

# 127.0.0.1:8000/todo/
urlpatterns = [
    # Django 뷰(View), or 템플릿 렌더링(template randering)
    # path("list/", views.todo_list), # 127.0.0.1:8000/todo/list/

    # RESTful API
    path("create/", TodoCreateAPI.as_view()),
    path("list/", TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", TodoRetrieveAPI.as_view()),
    path("update/<int:pk>/", TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", TodoDeleteAPI.as_view()),
]