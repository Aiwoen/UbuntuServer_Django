from django.http import HttpResponse
from django.shortcuts import render
from App.models import Student
import random

# Create your views here.
def hello(request):
    return HttpResponse("<h1>test<h1>")
def home(request):
    return render(request, 'home.html')
def add_student(request):

    student = Student()
    student.s_name = 'Jerry%d' % random.randrange(100)
    student.save()
    
    return HttpResponse("Add Success %s" % student.s_name)
def get_students(request):
    
    students = Student.objects.all()
    for student in students:
        print(student.s_name)
    
    context = {
        "hobby" : "testcontext",
        "students" : students
    }
    
    return render(request, 'home.html',context=context)
def update_student(request):

    student = Student.objects.get(pk=2)
    student.s_name = 'Jack'
    student.save()

    return HttpResponse("Student Upate Success")
    
def delete_student(request):

    student = Student.objects.get(pk=3)
    student.delete()
    

    return HttpResponse("Student delete success")