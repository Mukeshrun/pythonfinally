from django.db import models
from django.contrib.auth.models import User
import datetime
class Jobseekar(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    course=models.CharField(max_length=50,default="")
    course_type=models.CharField(max_length=50,default="")
    member=models.CharField(max_length=50,default="")
    status=models.CharField(max_length=50,default="")
    branch=models.CharField(max_length=50,default="")
    def __str__(self):
        return f'{self.name} {self.email} {self.password} {self.member}{self.status}'
class Jobseekerprofile(models.Model):
    jobseeker=models.ForeignKey(Jobseekar,on_delete=models.CASCADE,null=True)
    photopath=models.ImageField(default="none")
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100)
    mobile=models.IntegerField(default="")
    dob=models.DateField()
    primary_stream=models.CharField(max_length=50,null=True,blank=True)
    primary_percentage=models.IntegerField(null=True,blank=True)
    primary_year=models.IntegerField(null=True,blank=True)
    secondary_stream=models.CharField(max_length=50,null=True,blank=True)
    secondary_percentage=models.IntegerField(null=True,blank=True)
    secondary_year=models.IntegerField(null=True,blank=True)
    graduation_stream=models.CharField(max_length=50,null=True,blank=True)
    graduation_percentage=models.IntegerField(null=True,blank=True)
    graduation_year=models.IntegerField(null=True,blank=True)
    post_graduation_stream=models.CharField(max_length=50,null=True,blank=True,default=None)
    post_graduation_percentage=models.CharField(max_length=50,null=True,blank=True,default=None)
    post_graduation_year=models.CharField(max_length=50,null=True,blank=True,default=None)
    resume=models.FileField(default="")
    def __str__(self):
        return f'{self.jobseeker}{self.name}{self.email}{self.mobile}{self.dob}{self.resume}'
class Job(models.Model):
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    job_title=models.CharField(max_length=100)
    job_detail=models.TextField(max_length=500)
    salary=models.IntegerField()
    education=models.CharField(max_length=200)
    experience=models.CharField(max_length=25,null=True)
    vacancy=models.CharField(max_length=200,default="")
    city=models.CharField(max_length=100)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    company=models.CharField(max_length=100)
    logo=models.ImageField(default='/media/download.png')
    company_address=models.CharField(max_length=100,default="")
    hr_email=models.CharField(max_length=50)
    programming_language=models.CharField(max_length=50,default="")
    posted_date=models.DateField(default=datetime.date.today())
    def __str__(self):
        return f'{self.job_title} End date{self.end_date}'

class Apply(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    Jobseekar=models.ForeignKey(Jobseekar,on_delete=models.CASCADE)
    applied=models.CharField(max_length=50)
    apply_date=models.DateField(null=True)
    def __str__(self):
        return f'{self.job},{self.Jobseekar},{self.applied}'