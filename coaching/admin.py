from django.contrib import admin
from . models import Jobseekar,Jobseekerprofile,Job,Apply


@admin.register(Jobseekar)
class JobseekarAdmin(admin.ModelAdmin):
    list_display=['name','email','course','course_type','branch']


@admin.register(Jobseekerprofile)
class Jobseekerprofile(admin.ModelAdmin):
    list_display=['name','email','mobile','dob','resume']
    


@admin.register(Job)
class PostAdmin(admin.ModelAdmin):
    list_display=['job_title','salary','city','end_date','hr_email']

@admin.register(Apply)
class Apply(admin.ModelAdmin):
    list_display=['Jobseekar','job','applied','apply_date']
