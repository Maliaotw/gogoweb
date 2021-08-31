from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.app import views

# viewset 配置路由
router = DefaultRouter()
router.register(r'task', views.TaskModelViewSet)  # Allow: GET, POST, HEAD, OPTIONS

urlpatterns = [
    path('', include(router.urls)),
]
