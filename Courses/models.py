from django.db import models

# Create your models here.

class Instructor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,default='')

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,default='')
    
    def __str__(self):
        return self.name

# One to One relation
class Profile(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    bio=models.TextField(null=True)
    age=models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.student.name


# One to Many and Many to Many
class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name='courses')
    students=models.ManyToManyField(Student,related_name='courses')
    
    def __str__(self):
        return self.title


# One to Many
class Lesson(models.Model):
    title=models.CharField(max_length=50)
    content=models.TimeField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')

    def __str__(self):
        return self.title
