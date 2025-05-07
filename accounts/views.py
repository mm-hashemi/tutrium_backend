from rest_framework import generics
from .models import User, TeacherProfile, StudentProfile
from .serializers import UserSerializer, TeacherProfileSerializer, StudentProfileSerializer,UserRegistrationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer  # بساز یا ساده تعریف کن

from rest_framework import generics, serializers, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import TeacherProfile, StudentProfile
from .serializers import UserSerializer, TeacherProfileSerializer, StudentProfileSerializer, UserRegistrationSerializer






class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # این خط رو اضافه کن

class TeacherProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [IsAuthenticated]  # فقط کاربران وارد شده می‌توانند پروفایل استاد را مشاهده، ویرایش یا حذف کنند

class StudentProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]  # فقط کاربران وارد شده می‌توانند پروفایل استاد را مشاهده، ویرایش یا حذف کنند


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'full_name', 'role']  # فیلدهای مورد نیاز رو انتخاب کن


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # برای دسترسی باید کاربر وارد شده باشد

    def get(self, request):
        # گرفتن کاربر فعلی
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "ثبت‌نام با موفقیت انجام شد."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# accounts/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # اضافه کردن اطلاعات اضافی کاربر در پاسخ (اختیاری)
        data['full_name'] = self.user.full_name
        data['role'] = self.user.role
        return data

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# accounts/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
