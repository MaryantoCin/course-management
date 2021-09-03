from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses_api import views

router = DefaultRouter()
router.register('course', views.CourseViewSet)
router.register('lesson', views.LessonViewSet)
router.register('material', views.MaterialViewSet)

urlpatterns = [
  path('', include(router.urls))
]
