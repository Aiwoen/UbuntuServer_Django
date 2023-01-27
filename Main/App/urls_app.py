from django.urls import path, include
from App import views

urlpatterns=[
    path('home/', views.home),
    path('addstudent', views.add_student),
    path('getstudents', views.get_students),
    path('updatestudent', views.update_student),
    path('deletestudent', views.delete_student),
    path('test',views.test),
    path('addpersons',views.add_persons),
    path('getperson',views.get_persons),
    path('classlist',views.classlist),
]
