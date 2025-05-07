from django.contrib import admin
from .models import User, TeacherProfile, StudentProfile

# ثبت مدل User در پنل ادمین
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'full_name')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')

admin.site.register(User, UserAdmin)

# ثبت مدل TeacherProfile در پنل ادمین
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'languages', 'is_verified')
    search_fields = ('user__full_name', 'languages')

admin.site.register(TeacherProfile, TeacherProfileAdmin)

# ثبت مدل StudentProfile در پنل ادمین
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'interests')
    search_fields = ('user__full_name', 'interests')

admin.site.register(StudentProfile, StudentProfileAdmin)
