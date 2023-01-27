from django.http import HttpResponse
from django.shortcuts import render
from App.models import Student
from App.models import Person
from App.models import Sclass
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
def test(request):

    person = Person.create('Jack')
    person.save()

    return HttpResponse("創建成功")

def add_persons(request):

    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "Tom%d" %i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()

    return HttpResponse("完成")

def get_persons(request):

    #persons = Person.objects.filter(p_age__gt=50)
    #persons = Person.objects.exclude(p_age__lt=50)
    #persons = Person.objects.filter(is_delete=False)
    persons = Person.objects.all().order_by("p_age")

    context = {
        "persons" : persons
    }
    return render(request,'person_list.html',context=context)

def classlist(request):
    classes = Sclass.objects.all().order_by("c_name")
    context = {
        "classes" : classes
    }
    return render(request,'class.html',context=context)
