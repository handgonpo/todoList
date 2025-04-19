from django.urls import path, include
from .apis import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TodoViewSet)

# 127.0.0.1:8000/todo/
urlpatterns = [
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

    # Viewsets_Test
    path("viewsets/", include(router.urls)), # 127.0.0.1:8000/todo/viewsets/
]