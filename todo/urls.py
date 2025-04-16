from django.urls import path
from .apis import *
from . import views  # views 모듈을 통째로 임포트

# 127.0.0.1:8000/todo/
urlpatterns = [
    # Django 뷰(View), or 템플릿 렌더링(template randering)
    # path("list/", views.todo_list), # 127.0.0.1:8000/todo/list/

    # APIView
    path("create/", TodoCreateAPI.as_view()),
    path("list/", TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", TodoRetrieveAPI.as_view()),
    path("update/<int:pk>/", TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", TodoDeleteAPI.as_view()),

    # GenericAPIView 
    path("generics/create/", TodoGenericsCreateAPI.as_view()),
    path("generics/list/", TodoGenericsListAPI.as_view()),
    path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view()),
    path("generics/update/<int:pk>/", TodoGenericsUpdateAPI.as_view()),
    path("generics/delete/<int:pk>/", TodoGenericsDeleteAPI.as_view()),
]