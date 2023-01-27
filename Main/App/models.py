from django.db import models

# Create your models here.

class Sclass(models.Model):
    c_name = models.CharField(max_length=16)
    c_tutor = models.CharField(max_length=16)
    class Meta:
        db_table = 'Class'

class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_sage = models.IntegerField(default=1)
    s_class = models.ForeignKey(Sclass,default=1,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Student'

class isdeletemanager(models.Manager):
    def get_queryset(self):
        return super(isdeletemanager,self).get_queryset().filter(is_delete=False)

class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=18, db_column='age')
    p_sex = models.BooleanField(default=False,db_column='sex')
    p_hobby = models.CharField(max_length=32,null=True,blank=True)
    is_delete = models.BooleanField(default=False)
    class Meta:
        db_table = 'People'
    objects = isdeletemanager()

    @classmethod
    def create(cls,p_name,p_age=100,p_sex=True,p_hobby='gaming'):
        return cls(p_name=p_name,p_age=p_age,p_sex=p_sex,p_hobby=p_hobby)





    
    
