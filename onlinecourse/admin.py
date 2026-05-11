from django.contrib import admin
# Import all models including new ones
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# ChoiceInline for Question admin
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# CourseAdmin with LessonInline
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# LessonAdmin (no inline needed)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# QuestionAdmin with ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'grade']

# Register all models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)