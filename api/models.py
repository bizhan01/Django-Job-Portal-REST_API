from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,PermissionMixin
from django.contrib.auth.models import User 


class application(models.Model): 
    category = (
        ('Full Time','fulltime'),
        ('Part Time', 'parttime'),
        ('Internship', 'intern'),
        ('Freelancer', 'freelancer'),
    )   
    position = models.CharField(max_length=200,null=True) #varchar
    description = models.CharField(max_length=200,null=True) 
    job_type = models.CharField(max_length=200,null=True, choices= category)
    salary = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    location = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.position
class candidate(models.Model):
    category = (
    ('Male','male'),
    ('Female','female'),
    ('Others','others'),
    )
    name = models.CharField(max_length=200,null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=200,null=True,choices=category)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    job_applied = models.ForeignKey(application,default=1,on_delete=models.SET_DEFAULT)
    resume = models.FileField(null=True)


    def __str__(self):
        return self.name,self.job_applied


