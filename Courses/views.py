from django.shortcuts import render,redirect ,HttpResponse
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def instructorList(request):
    instructors=Instructor.objects.all()
    pk=request.GET.get('pk','')
    detail=''
    if pk:
        detail=Instructor.objects.get(pk=pk)
    context={'instructors':instructors,'detail':detail}
    return render(request,'instructor.html',context)

@login_required
def studentList(request):
    students=Student.objects.all()
    pk=request.GET.get('pk','')
    detail=''
    if pk:
        detail=Student.objects.get(pk=pk)
    context={'students':students,'detail':detail}
    return render(request,'student.html',context)

def courseList(request):
    courses=Course.objects.all()
    pk=request.GET.get('pk','')
    detail=''
    if pk:
        detail=Course.objects.get(pk=pk)
    context={'courses':courses,'detail':detail}
    return render(request,'course.html',context)

def profile(request):
    user=request.user
    if user.is_staff:
        user=Instructor.objects.get(name=user.username)
        context={"profile":user,"is_staff":True}
        return render(request,'profile.html',context)
    student, created=Student.objects.get_or_create(name=user.username,email=user.email)    
    if created:
        profile= Profile.objects.create(student=student,bio=None,age=None)
        profile.save()
    else:
        profile=Profile.objects.get(student__name=student)
    context={"profile":profile}
    return render(request,'profile.html',context)

@staff_member_required(login_url='adminLogout')
def addInstructor(request):
    form=InstructorForm()
    msg=""
    if request.method=="POST":
        form=InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='instructors')
        else:  
            msg='Invalid mail domain'
    context={'form':form,'title':"Add Instructor",'msg':msg}
    return render(request,'form.html',context)

@staff_member_required(login_url='adminLogout')
def addStudent(request):
    form=StudentForm()
    msg=""
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='students') 
        else:  
            msg='Invalid mail domain'
    context={'form':form,'title':"Add Student",'msg':msg}
    return render(request,'form.html',context)

@staff_member_required(login_url='adminLogout')
def addCourse(request):
    form=CourseForm()
    msg=""
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='courses')
        else:  
            msg='Invalid mail domain'
    context={'form':form,'title':"Add Course",'msg':msg}
    return render(request,'form.html',context)

@staff_member_required(login_url='adminLogout')
def editInstructor(request,pk):
    item=Instructor.objects.get(pk=pk)
    form=InstructorForm(instance=item)
    msg=""
    if request.method=="POST":
        print(request.POST)
        form=InstructorForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect(to='instructors')
        else:  
            msg='Invalid mail domain'
    context={'form':form,'title':"Edit Instructor",'id':pk,'msg':msg}
    return render(request,'form.html',context)

@staff_member_required(login_url='adminLogout')
def editStudent(request,pk):
    item=Student.objects.get(pk=pk)
    form=StudentForm(instance=item)
    msg=""
    if request.method=="POST":
        form=StudentForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect(to='students')
        else:  
            msg='Invalid field domain'
    context={'form':form,'title':"Edit Student",'id':pk,'msg':msg}
    return render(request,'form.html',context)

@staff_member_required(login_url='adminLogout')
def editCourse(request,pk):
    item=Course.objects.get(pk=pk)
    form=CourseForm(instance=item)
    msg=""
    if request.method=="POST":
        form=CourseForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect(to='courses')
        else:  
            msg='Invalid field data'
    context={'form':form,'title':"Edit Course",'id':pk,'msg':msg}
    return render(request,'form.html',context)

@staff_member_required(login_url='adminLogout')
def deleteInstructor(request,pk):
    item=Instructor.objects.get(pk=pk)
    if request.method=="POST":
        Instructor.objects.get(pk=pk).delete()
        return redirect(to='instructors')
    context={'title':"Delete Instructor",'id':pk,'item':item}
    return render(request,'delete.html',context)

@staff_member_required(login_url='adminLogout')
def deleteStudent(request,pk):
    item=Student.objects.get(pk=pk)
    if request.method=="POST":
        Student.objects.get(pk=pk).delete()
        return redirect(to='students')    
    context={'title':"Delete Student",'id':pk,'item':item}
    return render(request,'delete.html',context)

@staff_member_required(login_url='adminLogout')
def deleteCourse(request,pk):
    item=Course.objects.get(pk=pk)
    if request.method=="POST":
        Course.objects.get(pk=pk).delete()
        return redirect(to='courses')
    context={'title':"Delete Course",'id':pk,'item':item}
    return render(request,'delete.html',context)

def signupAdmin(request):
    form=AdminSignUpForm()    
    if request.method!="POST":
        context={'form':form}
        return render(request,'signup.html',context)
    form=AdminSignUpForm(request.POST)
    if not form.is_valid():
        context={'form':form}
        return render(request,'signup.html',context)
    username=form.cleaned_data['username']
    email=form.cleaned_data['email']
    user=form.save(commit=False)
    if Instructor.objects.filter(email=email).exists() and Instructor.objects.filter(name=username).exists():
        user.is_staff=True
        print("Staff User Created")
    user.set_password(form.cleaned_data['password'])
    user.save()
    return redirect(to='adminLogin')

def loginAdmin(request):
    form=AdminLoginForm()
    next=request.GET.get('next','/')
    if request.method=="POST":
        form=AdminLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(to=request.POST.get('next',''))
            messages.warning(request,"Invalid Username or Password")
    context={'form':form,'next':next}
    return render(request,'login.html',context)

def logoutAdmin(request):
    logout(request)
    return redirect(to='adminLogin')