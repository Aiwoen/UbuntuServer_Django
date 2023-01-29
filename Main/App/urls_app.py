from django.urls import path, include,re_path
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
    path('classlist/',views.classlist,name='classlist'),
    path('classlists/<int:id>/',views.classstudentlist,name='class_students'),
    path('addcstudent/<int:class_id>',views.class_student_add,name='class_student_add'),
    path('deletecstudent/<int:id>/<int:class_id>/',views.class_student_delete,name='class_student_delete'),
    path('newclass',views.newclass,name='newclass'),
]
