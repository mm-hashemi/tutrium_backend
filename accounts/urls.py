from django.urls import path
from . import views
from .views import RegisterView,CustomLoginView,MeView

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('teacher-profile/<int:pk>/', views.TeacherProfileDetailView.as_view(), name='teacher-profile-detail'),
    path('student-profile/<int:pk>/', views.StudentProfileDetailView.as_view(), name='student-profile-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('me/', MeView.as_view(), name='me'),
]
