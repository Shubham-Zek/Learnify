from django import forms
from .models import *
from django.contrib.auth.models import User

class InstructorForm(forms.ModelForm):
    class Meta:
        model=Instructor
        fields=['name','email']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['student','bio','age']

class CourseForm(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model=Course
        fields=['title','description','instructor','students']
        

class LessonForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields=['title','content','course']

class AdminSignUpForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']

class AdminLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
        