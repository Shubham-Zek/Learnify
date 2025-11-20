from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('instructors/',views.instructorList,name='instructors'),
    path('students/',views.studentList,name='students'),
    path('courses/',views.courseList,name='courses'),
    path('addInstructor/',views.addInstructor,name='addInstructor'),
    path('addStudent/',views.addStudent,name='addStudent'),
    path('addCourse/',views.addCourse,name='addCourse'),
    path('editInstructor/<int:pk>',views.editInstructor,name='editInstructor'),
    path('editStudent/<int:pk>',views.editStudent,name='editStudent'),
    path('editCourse/<int:pk>',views.editCourse,name='editCourse'),
    path('deleteInstructor/<int:pk>/',views.deleteInstructor,name='deleteInstructor'),
    path('deleteStudent/<int:pk>/',views.deleteStudent,name='deleteStudent'),
    path('deleteCourse/<int:pk>/',views.deleteCourse,name='deleteCourse'),
    path('profile/',views.profile,name='profile'),
    path('adminSignup/',views.signupAdmin,name='adminSignup'),
    path('adminLogin/',views.loginAdmin,name='adminLogin'),
    path('adminLogout/',views.logoutAdmin,name='adminLogout'),
]
