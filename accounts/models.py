from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def user_profile_image_path(instance, filename):
    return f'profiles/user_{instance.user.id}/{filename}'
# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, role, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, role='teacher', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, full_name, role, password, **extra_fields)

    def get_by_natural_key(self, email):
        # This is required for Django's authentication to work correctly
        return self.get(email=email)

# Custom User Model
class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # Add is_superuser field
    password = models.CharField(max_length=255)  # Make sure password is non-nullable

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'role']  # Additional required fields

    objects = CustomUserManager()  # Assign the custom manager

    def __str__(self):
        return f"{self.full_name} ({self.role})"

    @property
    def is_anonymous(self):
        return not self.is_active  # If the user is inactive, they are anonymous

    @property
    def is_authenticated(self):
        return True  # The user is authenticated if they are active
    def has_perm(self, perm, obj=None):
        # Implement permission checking logic here
        return True  # For now, you can always return True or add custom logic

    def has_module_perms(self, app_label):
        # Implement app module permission logic here
        return True  # You can return True for all modules for now or add custom logic

# Teacher Profile
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    languages = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)

    def __str__(self):
        return f"{self.user.full_name}'s Teacher Profile"

# Student Profile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)

    def __str__(self):
        return f"{self.user.full_name}'s Student Profile"
