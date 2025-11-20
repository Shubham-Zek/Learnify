from django.contrib import admin
from .models import *

# Register your models here.

class InstructorAdmin(admin.ModelAdmin):
    list_display=['name','email']
admin.site.register(Instructor,InstructorAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email']
admin.site.register(Student,StudentAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display=['student','bio','age']
admin.site.register(Profile,ProfileAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=['title','description','instructor']
admin.site.register(Course,CourseAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display=['title','content','course']
admin.site.register(Lesson,LessonAdmin)