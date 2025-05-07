from django.contrib import admin
from .models import AITest, Course, CourseSubscription, Progress, Test, TestResult

# کلاس‌های ادمین برای هر مدل

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title', 'description')

admin.site.register(Course, CourseAdmin)

class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'subscription_date', 'is_active')
    search_fields = ('student__user__full_name', 'course__title')
    list_filter = ('is_active', 'subscription_date')

admin.site.register(CourseSubscription, CourseSubscriptionAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_subscription', 'test_date', 'skill')
    search_fields = ('title', 'description')
    list_filter = ('test_date', 'skill')

admin.site.register(Test, TestAdmin)

class TestResultAdmin(admin.ModelAdmin):
    list_display = ('test', 'student', 'score', 'passed', 'date_taken')
    search_fields = ('test__title', 'student__user__full_name')
    list_filter = ('passed', 'date_taken')

admin.site.register(TestResult, TestResultAdmin)

class ProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'language', 'skill', 'progress_percentage', 'last_updated')
    search_fields = ('student__user__full_name', 'language')
    list_filter = ('skill', 'last_updated')

admin.site.register(Progress, ProgressAdmin)

class AITestAdmin(admin.ModelAdmin):
    list_display = ('test', 'student', 'ai_score', 'date_taken')
    search_fields = ('test__title', 'student__user__full_name', 'ai_model')
    list_filter = ('date_taken', 'ai_model')

admin.site.register(AITest, AITestAdmin)
