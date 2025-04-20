from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # 첫페이지 추가
    path("", views.hello_world, name='base'), # 127.0.0.1:8000/

    path('admin/', admin.site.urls),

    # /todo/는 HTML 렌더링(템플릿용)
    path("todo/", include("todo.urls")), # 127.0.0.1:8000/todo/

    # /api/todo/는 데이터 처리(API 전용)
    path("api/todo/", include("todo.api_urls")), # 127.0.0.1:8000/api/todo/
    # 둘 다 각자의 역할을 하며 동시에 작동합니다.
]
