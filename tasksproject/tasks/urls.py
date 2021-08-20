from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'todos', views.ToDoViewSet)
router.register(r'users', views.UserViewSet)
