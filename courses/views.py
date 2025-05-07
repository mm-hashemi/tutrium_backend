from rest_framework import viewsets, permissions
from .models import Course, CourseSubscription, Test, TestResult, Progress, AITest
from .serializers import (
    CourseSerializer, CourseSubscriptionSerializer, TestSerializer,
    TestResultSerializer, ProgressSerializer, AITestSerializer
)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

class AITestViewSet(viewsets.ModelViewSet):
    queryset = AITest.objects.all()
    serializer_class = AITestSerializer
    permission_classes = [permissions.IsAuthenticated]
