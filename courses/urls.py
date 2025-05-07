from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, CourseSubscriptionViewSet, TestViewSet,
    TestResultViewSet, ProgressViewSet, AITestViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'subscriptions', CourseSubscriptionViewSet)
router.register(r'tests', TestViewSet)
router.register(r'test-results', TestResultViewSet)
router.register(r'progress', ProgressViewSet)
router.register(r'ai-tests', AITestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
