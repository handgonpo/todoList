from django.urls import path, include # include 추가
# from . import views  # views.todo_list() ← 접두어 붙여서 사용해야 함
from .views import * # todo_list() ← 이름만 써도 바로 사용 가능


# 127.0.0.1:8000/todo/
urlpatterns = [
    # Django 뷰(View), or 템플릿 렌더링(template randering)
    # path("list/", views.todo_list), # 127.0.0.1:8000/todo/list/

    path("list/", todo_list), # views. 접두어 생략

    # create Test
    path("create/", TodoCreateView.as_view()),
]