from django.urls import path, include # include 추가
# from . import views  # views.todo_list() ← 접두어 붙여서 사용해야 함
from .views import * # todo_list() ← 이름만 써도 바로 사용 가능


# 127.0.0.1:8000/todo/
urlpatterns = [
    # Django 뷰(View), or 템플릿 렌더링(template randering)
    # path("list/", views.todo_list), # 127.0.0.1:8000/todo/list/

    # path("list/", todo_list), # views. 접두어 생략

    # views
    path("create/", TodoCreateView.as_view(), name="create"), # 127.0.0.1:8000/todo/create/
    path("list/", TodoListView.as_view(), name="list"), # 127.0.0.1:8000/todo/list/
    path("update/<int:pk>/", TodoUpdateView.as_view()), # 127.0.0.1:8000/todo/update/<pk>/
    path("<int:pk>/", TodoDetailView.as_view()), # retrieve lits에서 글자를 클릭하면 127.0.0.1:8000/todo/<pk>
]