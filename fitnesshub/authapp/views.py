from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment


# Create your views here.

def Home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        first_name=request.POST.get("first_name")
        middle_name=request.POST.get("middle_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>11 or len(username)<11:
            messages.info(request,"Phone Number Must be 11 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
         
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name = first_name
        #myuser.middle_name = middle_name
        myuser.last_name = last_name
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
    return render(request,"handlelogin.html")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back to you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrolling")
        return redirect('/join')



    return render(request,"enroll.html",context)
