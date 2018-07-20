# api/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
]

# api/urls.py
from django.urls import path

from . import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TodoViewSet, base_name='todos')
urlpatterns = router.urls
