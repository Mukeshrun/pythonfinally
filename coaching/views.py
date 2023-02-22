from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Job, Jobseekar, Jobseekerprofile,Apply
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate
from datetime import date
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator

def index(request):
    data=Job.objects.all()
    today=date.today()
    for i in data:
        if i.end_date>=today:
            newdata=Job.objects.filter(end_date__gte=today).order_by('-id')[:10]
            return render(request,'coaching/index.html',{'key':newdata})
    else:
        return render(request,'coaching/index.html')
            
def jobseekersignup(request):
    if request.method == 'POST':
        email = request.POST['email']
        check=Jobseekar.objects.filter(email=email).count()
        if check==1:
            return render(request,'coaching/jobseekersignup.html',{"success":"not"})
        else:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            member = request.POST['member']
            course=request.POST['course']
            course_type=request.POST['coursetype']
            branch1=request.POST['branch']
            Jobseekar(name=name,email=email,password=password,member=member,course=course,course_type=course_type,branch=branch1,status='Pending').save()
            return render(request, 'coaching/jobseekersignup.html', {"success": "yes"})
    return render(request, 'coaching/jobseekersignup.html')

def branch(request):
     data="data"
     return render(request,'coaching/branch.html',{"data":data})
def branch1(request):
     data="data"
     return render(request,'coaching/no.html',{"data":data})

def jobseekerlogin(request):
    if request.session.has_key('login1'):
        user1=request.session['login1']
        data=Jobseekar.objects.filter(email=user1)
        return render(request,'coaching/jobseekerhome.html',{"data":data})
    else:
        if request.method=='POST':
            user2=''
            user1=request.POST['login']
            password=request.POST['pass']
            user_login1=Jobseekar.objects.filter(email=user1)
            user_exist=user_login1.count()
            if user_exist==1:
               user_login=Jobseekar.objects.filter(email=user1,password=password)
               check=user_login.count()
               if check==1:
                 for i in user_login:
                    user2+=i.status
                 if user_login is not None and user2!='Pending':
                   request.session["login1"]=request.POST["login"]
                   return render(request,'coaching/jobseekerhome.html',{"data":user_login1})
                 else:
                     return render(request,'coaching/jobseekerlogin.html',{"status":"Pending status"})
               else:
                    return render(request,'coaching/jobseekerlogin.html',{"key":"Invalid"})
            else:
                return render(request,'coaching/jobseekerlogin.html',{"key":"not"})
        return render(request,'coaching/jobseekerlogin.html')

def jobseekerhome(request):
    if request.session.has_key("login1"):
        data=Jobseekar.objects.filter(email=request.session['login1'])
        return render(request,'coaching/jobseekerhome.html',{"data":data})
    else:
        return redirect('jobseekerlogin')

def all_jobseekers(request):
    if request.session.has_key("adminlogin"):
        data=Jobseekar.objects.all()
        return render(request,'coaching/all_jobseekers.html',{"key":data})
    else:
        return redirect('admin_login')
def all_jobseekers1(request):
    if request.session.has_key("adminlogin"):
        data=Jobseekar.objects.filter(member='No')
        return render(request,'coaching/all_jobseekers1.html',{"key":data})
    else:
        return redirect('admin_login')

def jobseekerlogout(request):
    del request.session["login1"]
    return redirect("index")

def delete_jobseekers(request,id):
     if request.session.has_key("adminlogin"):
        Jobseekar.objects.get(id=id).delete()
        return redirect("all_jobseekers")
def delete_jobseekers1(request,id):
     if request.session.has_key("adminlogin"):
        Jobseekar.objects.get(id=id).delete()
        return redirect("all_jobseekers1")

def alljob(request):
    data=Job.objects.all()
    data_list=[]
    today=date.today()
    for i in data:
        if i.end_date>=today:
            newdata=Job.objects.filter(end_date__gte=today).order_by('-id')[:10]
            paginator_obj=Paginator(newdata,2)
            page_number=request.GET.get('page')
            page_obj=paginator_obj.get_page(page_number )
            return render(request,'coaching/alljob.html',{'key':page_obj})
    else:
        return render(request,'coaching/alljob.html')

def oldjob(request):
    data=Job.objects.all()
    today=date.today()
    for i in data:
        if i.end_date<today:
            newdata=Job.objects.filter(end_date__lt=today)
            paginator_obj=Paginator(newdata,2)
            page_number=request.GET.get('page')
            page_obj=paginator_obj.get_page(page_number )
            return render(request,'coaching/oldjob.html',{'key':page_obj})
    else:
        return render(request,'coaching/oldjob.html')

def jobseekerprofile(request):
    if request.session.has_key("login1"):
        check=Jobseekerprofile.objects.filter(email=request.session['login1'])
        jobprofile=Jobseekar.objects.filter(email=request.session['login1'])
        if check.count()==1:
            user_login=Jobseekar.objects.filter(email=request.session['login1'])
            return render(request,'coaching/jobseekerprofile.html',{"key":check,"data":user_login})
        else:
            if request.method=='POST':
                jobprofile=Jobseekar.objects.get(email=request.session['login1'])
                name=request.POST['name']
                email=request.POST['email']
                mobile=request.POST['mobile']
                dob=request.POST['dob']
                photo1=request.FILES['photo']
                resume=request.FILES['resume']
                primary_stream=request.POST['tenstream']
                primary_percentage=request.POST['tenper']
                primary_year=request.POST['tenpass']
                secondary_stream=request.POST['twelvetream']
                secondary_percentage=request.POST['twelveper']
                secondary_year=request.POST['twelevepass']
                graduation_stream=request.POST['gradutionstream']
                graduation_percentage=request.POST['gradutionper']
                graduation_year=request.POST['gradutionpass']
                post_graduation_stream=request.POST['pgradutionstream']
                post_graduation_percentage=request.POST['pgradutionper']
                post_graduation_year=request.POST['pgradutionpass']
                fs=FileSystemStorage()
                fs1=FileSystemStorage()
                photofile=fs.save(photo1.name,photo1)
                resumefile=fs1.save(resume.name,resume)
                data=Jobseekerprofile(jobseeker=jobprofile,photopath=photofile,name=name,email=email,mobile=mobile,dob=dob,resume=resumefile,primary_stream=primary_stream,primary_percentage=primary_percentage,primary_year=primary_year,secondary_stream=secondary_stream,secondary_percentage=secondary_percentage,secondary_year=secondary_year,graduation_stream=graduation_stream,graduation_percentage=graduation_percentage,graduation_year=graduation_year,post_graduation_stream=post_graduation_stream,post_graduation_percentage=post_graduation_percentage,post_graduation_year=post_graduation_year)
                data.save()
                data=Jobseekerprofile.objects.filter(email=email)
                return render(request,'coaching/jobseekerprofile.html',{"key":data})
        return render(request,'coaching/jobseekerprofile.html',{"success":"success","data":jobprofile})
    else:
        return redirect('jobseekerlogin')
    
def jobseekerappliedjob(request):
    if request.session.has_key("login1"):
        jobprofile=Jobseekar.objects.filter(email=request.session['login1'])
        apply=Apply.objects.filter(Jobseekar__email=request.session['login1'])
        if apply.count()>0:
           jobseeker=Jobseekar.objects.filter(email=request.session['login1'])
           return render(request,'coaching/jobseekerappliedjob.html',{"key":apply,"data":jobprofile})
        else:
            return render(request,'coaching/jobseekerappliedjob.html',{"key":apply,"data":jobprofile})


def update_jobseekerprofile(request):
    data=Jobseekerprofile.objects.get(pk=request.GET['q'])
    jobprofile=Jobseekar.objects.filter(email=request.session['login1'])
    if request.method=='POST':
        data.name=request.POST['name']
        data.email=request.POST['email']
        data.mobile=request.POST['mobile']
        data.dob=request.POST['dob']
        
        data.primary_stream=request.POST['tenstream']
        data.primary_percentage=request.POST['tenper']
        data.primary_year=request.POST['tenpass']
        data.secondary_stream=request.POST['twelvetream']
        data.secondary_percentage=request.POST['twelveper']
        data.secondary_year=request.POST['twelevepass']
        data.graduation_stream=request.POST['gradutionstream']
        data.graduation_percentage=request.POST['gradutionper']
        data.graduation_year=request.POST['gradutionpass']
        data.post_graduation_stream=request.POST['pgradutionstream']
        data.post_graduation_percentage=request.POST['pgradutionper']
        data.post_graduation_year=request.POST['pgradutionpass']                
        data.save()
        return redirect('jobseekerprofile') 
    return render(request,'coaching/update_jobseekerprofile.html',{"key":data,"data":jobprofile})
         

def jobdata(request):
    data = request.GET["q"]
    res = Job.objects.filter(job_title__contains=data)
    return render(request,"coaching/data.html",{"key":res})

def city(request):
    data=request.GET['q']
    res=Job.objects.filter(city__contains=data)
    return render(request,"coaching/city.html",{"key3":res})

def jobget(request):
    if request.session.has_key("login1"):
        if request.method=='POST':
            jobdetail=request.POST['jobtitle']
            location=request.POST['city']
            today=date.today()
            user_login1=Jobseekar.objects.filter(email=request.session['login1'])
            data=Job.objects.filter(job_title__contains=jobdetail,city__contains=location,end_date__gte=today)
            return render(request,'coaching/jobseekerhome.html',{"key":data,"data":user_login1})
    else:
        if request.method=='POST':
            jobdetail=request.POST['jobtitle']
            location=request.POST['city']
            today=date.today()
            data=Job.objects.filter(job_title__contains=jobdetail,city__contains=location,end_date__gt=today)
            return render(request,'coaching/index.html',{"key":data})

def jobget1(request):
        if request.method=='POST':
            jobdetail=request.POST['jobtitle']
            location=request.POST['city']
            data=Job.objects.filter(job_title=jobdetail,city=location)
            return render(request,'coaching/index.html',{"key":data})


def pending(request):
    data=Jobseekar.objects.filter(status='Pending')
    return render(request,'coaching/pending.html',{"key":data})

def pending1(request):
    data=Jobseekar.objects.filter(member='No',status='Pending')
    return render(request,'coaching/pending1.html',{"key":data})

def accepted(request):
    data=Jobseekar.objects.filter(status='Accept')
    return render(request,'coaching/pending.html',{"key":data})

def accepted1(request):
    data=Jobseekar.objects.filter(member='No',status='Accept')
    return render(request,'coaching/pending1.html',{"key":data})

def rejected(request):
    data=Jobseekar.objects.filter(status='Reject')
    return render(request,'coaching/pending.html',{"key":data})

def rejected1(request):
    data=Jobseekar.objects.filter(member='No',status='Reject')
    return render(request,'coaching/pending1.html',{"key":data})


def status_post(request):
    if request.method=='POST':
       status=request.POST.get('cid')
       id=request.POST.get('id')
       data=Jobseekar.objects.get(id=id)
       remove=request.POST.get('tr')
       data.status=status
       data.save()
       return JsonResponse({"key":"successfully","id":remove})

def change_password(request):
     if request.session.has_key("login1"):
        if request.method=='POST':
            success=''
            currentpassword=request.POST['cpassword']
            newpassword=request.POST['npassword']
            data=Jobseekar.objects.filter(email=request.session['login1'])
            user=Jobseekar.objects.filter(email=request.session['login1'],password=currentpassword).count()
            if user==1:
                user=Jobseekar.objects.get(email=request.session['login1'],password=currentpassword)
                user.password=newpassword
                user.save()
                success='yes'
            else:
                
                success='no'
            return render(request,'coaching/change_password.html',{"key":success,"data":data})
     data=Jobseekar.objects.filter(email=request.session['login1'])
     return render(request,'coaching/change_password.html',{'data':data})

def admin_login(request):
    if request.session.has_key('adminlogin'):
        username=request.session['adminlogin']
        return render(request,'coaching/admin_home1.html',{"key":username})
    else:
        if request.method=="POST":
           username=request.POST['admin']
           password=request.POST['pass']
           data=authenticate(username=username,password=password)
           if data:
              request.session["adminlogin"]=request.POST["admin"]
              return render(request,'coaching/admin_home1.html',{"key":username})
           else:
              return render(request,'coaching/admin_login.html',{"key":"Invalid login and password"})       
    return render(request,'coaching/admin_login.html')  

       
def admin_home(request):
    if request.session.has_key("adminlogin"):
      return render(request,'coaching/admin_home1.html')
    else:
        return redirect('admin_login')         

def admin_logout(request):
    del request.session["adminlogin"]
    return redirect("index")

def admin_add_jobseekar(request):
    if request.method == 'POST':
        email = request.POST['email']
        check=Jobseekar.objects.filter(email=email).count()
        if check==1:
            return render(request,'coaching/admin_add_jobseekar.html',{"success":"not"})
        else:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            member = request.POST['member']
            course=request.POST['course']
            branch=request.POST['branch']
            Jobseekar(name=name,email=email,password=password,member=member,course=course,branch=branch,status='Accept').save()
            return render(request, 'coaching/admin_add_jobseekar.html', {"success": "yes"})
    return render(request, 'coaching/admin_add_jobseekar.html')

def all(request):
    if request.method=='POST':
        alljobseekers=Jobseekar.objects.all().count()
        python=Jobseekar.objects.filter(course='Python').count()
        java=Jobseekar.objects.filter(course='Java').count()
        php=Jobseekar.objects.filter(course='PHP').count()
        asp=Jobseekar.objects.filter(course='ASP.NET').count()
        web=Jobseekar.objects.filter(course='Web design').count()
        angular=Jobseekar.objects.filter(course='MEAN STACK | ANGULAR').count()
        nodejs=Jobseekar.objects.filter(course='NODE JS').count()
        reactjs=Jobseekar.objects.filter(course='REACT JS').count()
        datascience=Jobseekar.objects.filter(course='Data Science').count()
        c=Jobseekar.objects.filter(course='C & C++').count()
        android=Jobseekar.objects.filter(course='Android/IOS').count()
        testing=Jobseekar.objects.filter(course='Software Testing').count()
        database=Jobseekar.objects.filter(course='Database').count()
        mernstack=Jobseekar.objects.filter(course='MERN STACK').count()
        cloud=Jobseekar.objects.filter(course='Cloud Computing').count()
        cyber=Jobseekar.objects.filter(course='Cyber Security').count()
        block=Jobseekar.objects.filter(course='Block chain').count()
        iot=Jobseekar.objects.filter(course='IOT').count()
        context={'all':alljobseekers,
        'java':java,
        'python':python,
        "net":asp,
        "web":web,
        'php':php,
        "angular":angular,
        'nodejs':nodejs,
        'reactjs':reactjs,
        'datascience':datascience,
        'c':c,
        'android':android,
        'testing':testing,
        'database':database,
        "mernstack":mernstack,
        'cloud':cloud,
        'cyber':cyber,
        'bl':block,
        'iot':iot}
        return render(request,'coaching/alljobseekers.html',context=context)
    alljobseekers=Jobseekar.objects.all().count()
    python=Jobseekar.objects.filter(course='Python').count()
    java=Jobseekar.objects.filter(course='Java').count()
    php=Jobseekar.objects.filter(course='PHP').count()
    asp=Jobseekar.objects.filter(course='ASP.NET').count()
    web=Jobseekar.objects.filter(course='Web design').count()
    angular=Jobseekar.objects.filter(course='MEAN STACK | ANGULAR').count()
    nodejs=Jobseekar.objects.filter(course='NODE JS').count()
    reactjs=Jobseekar.objects.filter(course='REACT JS').count()
    datascience=Jobseekar.objects.filter(course='Data Science').count()
    c=Jobseekar.objects.filter(course='C & C++').count()
    android=Jobseekar.objects.filter(course='Android/IOS').count()
    testing=Jobseekar.objects.filter(course='Software Testing').count()
    database=Jobseekar.objects.filter(course='Database').count()
    mernstack=Jobseekar.objects.filter(course='MERN STACK').count()
    cloud=Jobseekar.objects.filter(course='Cloud Computing').count()
    cyber=Jobseekar.objects.filter(course='Cyber Security').count()
    block=Jobseekar.objects.filter(course='Block chain').count()
    iot=Jobseekar.objects.filter(course='IOT').count()
    context={'all':alljobseekers,
        'java':java,
        'python':python,
        "net":asp,
        "web":web,
        "angular":angular,
        'nodejs':nodejs,
        'reactjs':reactjs,
        'datascience':datascience,
        'c':c,
        'android':android,
        'testing':testing,
        'database':database,
        "mernstack":mernstack,
        'cloud':cloud,
        'php':php,
        'cyber':cyber,
        'bl':block,
        'iot':iot,}
    return render(request,'coaching/alljobseekers.html',context=context)

def applied(request,id):
    if request.session.has_key("login1"):
        if request.method=='POST':
           jobseeker=Jobseekar.objects.get(email=request.session['login1'])
           job=Job.objects.get(id=id)
           applied=request.POST['apply']
           ob=Apply(job=job,Jobseekar=jobseeker,applied=applied,apply_date=date.today())
           ob.save()
           return redirect('jobseekerhome')
        else:
            job=Job.objects.get(id=id)
            jobseeker=Jobseekar.objects.get(email=request.session['login1'])
            apply=Apply.objects.filter(Jobseekar=jobseeker,job=job)
            apply1=apply.count()
            if apply1==1:
                for i in apply:
                  apply2=i.applied
                  return render(request,'coaching/applied.html',{"data1":apply2})
            else:
                return render(request,'coaching/applied.html')
 
def jobapply(request,id):
    if request.session.has_key('adminlogin'):
        job=Job.objects.get(id=id)
        candidate=Apply.objects.filter(job=job)
        return render(request,'coaching/candidate.html',{"key":candidate,"job":job})

def coursejob(request):
    if request.session.has_key('login1'):
        getjobseeker=Jobseekar.objects.get(email=request.session['login1'])
        get=Jobseekar.objects.filter(email=request.session['login1'])
        data=Job.objects.all()
        today=date.today()
        for i in data:
         if i.end_date>today:
            newdata=Job.objects.filter(end_date__gte=today,programming_language__contains=getjobseeker.course)
            paginator_obj=Paginator(newdata,2)
            page_number=request.GET.get('page')
            page_obj=paginator_obj.get_page(page_number )
            return render(request,'coaching/coursejob.html',{'key':page_obj,"data":get})
        else:
            return render(request,'coaching/coursejob.html',{"data":get})

def update_resume(request):
    if request.session.has_key("login1"):
        if request.method=='POST':
            id=request.POST.get('id')
            data=Jobseekerprofile.objects.get(pk=id)
            resume=request.FILES.get('resume')
            fs=FileSystemStorage()
            data.resume=fs.save(resume.name,resume)
            data.save() 
            return JsonResponse({"success":"done"})
def change_photo(request):
    if request.session.has_key("login1"):
        if request.method=='POST':
            id=request.POST.get('id')
            data=Jobseekerprofile.objects.get(pk=id)
            photo=request.FILES.get('image')
            fs=FileSystemStorage()
            data.photopath=fs.save(photo.name,photo)
            data.save()
            return JsonResponse({"success":"done"})
 
def search(request):
    if request.method=='POST':
        detail=request.POST['course']
        data=Jobseekar.objects.filter(course=detail)
        return render(request,'coaching/search.html',{"key":data})
    return render(request,'coaching/search.html')

def userlist(request):
    data=Jobseekar.objects.filter(course=request.GET['q'])
    return render(request,'coaching/userlist.html',{'key':data})
