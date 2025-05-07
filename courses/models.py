from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # قیمت دوره

    def __str__(self):
        return self.title


class CourseSubscription(models.Model):
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscription_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.user.full_name} - {self.course.title}"


class Test(models.Model):
    COURSE_SKILLS_CHOICES = (
        ('reading', 'Reading'),
        ('writing', 'Writing'),
        ('speaking', 'Speaking'),
        ('listening', 'Listening'),
    )
    
    course_subscription = models.ForeignKey(CourseSubscription, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    test_date = models.DateTimeField()
    duration_minutes = models.IntegerField()
    skill = models.CharField(max_length=20, choices=COURSE_SKILLS_CHOICES)

    def __str__(self):
        return f"Test: {self.title} ({self.skill})"


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2)
    passed = models.BooleanField(default=False)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result of {self.student.user.full_name} in {self.test.title} ({self.test.skill}): {self.score}/{self.max_score}"


class Progress(models.Model):
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    skill = models.CharField(max_length=20, choices=Test.COURSE_SKILLS_CHOICES)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.full_name}'s progress in {self.language} ({self.skill}): {self.progress_percentage}%"


class AITest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='ai_tests')
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    ai_score = models.DecimalField(max_digits=5, decimal_places=2)
    ai_feedback = models.TextField(blank=True)
    ai_model = models.CharField(max_length=50, default="OpenAI")
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Test for {self.student.user.full_name} - {self.test.title}: {self.ai_score}"
