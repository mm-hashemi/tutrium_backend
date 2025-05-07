from rest_framework import serializers
from .models import User, TeacherProfile, StudentProfile
from rest_framework import serializers
from .models import User





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'role', 'is_active', 'is_staff']

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ['user', 'bio', 'languages', 'is_verified']

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['user', 'interests']


    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'role']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

