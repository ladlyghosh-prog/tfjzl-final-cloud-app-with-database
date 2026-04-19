from django.contrib import admin
# Ensure all 7 models are imported here
from .models import Question, Choice, Submission, Lesson, Course, Instructor

# 1. ChoiceInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 2. QuestionInline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# 3. QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

# 4. LessonAdmin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

# Register your models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course)
admin.site.register(Instructor)
