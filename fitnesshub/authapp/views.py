from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Equipments,Attendance,Service,Appointment,Payment
from datetime import timedelta


# Create your views here.

def Home(request):
    return render(request,"index.html")

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)
    #return render(request,"profile.html")
 


def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        first_name=request.POST.get("first_name")
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


def equipments(request):
    posts=Equipments.objects.all()
    context={"posts":posts}
    return render(request,"equipments.html",context)


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendance Applied Successfully")
        return redirect('/attendance')
    return render(request,"attendance.html",context)


def service(request):
    services=Service.objects.all()
    context={"services":services}
    return render(request,"service.html",context)


def appointment(request):
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        user_phone=request.POST.get('PhoneNumber')
        trainer=request.POST.get('trainer')
        date_and_time=request.POST.get('workout')
        duration_minutes = int(request.POST.get('duration'))
        appointment_type=request.POST.get('appointment_type')
        status=request.POST.get('status')

         # Convert duration to timedelta object
        duration = timedelta(minutes=duration_minutes)
        query=Appointment(full_name=full_name,user_phone=user_phone,trainer=trainer,date_and_time=date_and_time,duration=duration,appointment_type=appointment_type,status=status )
        query.save()
        messages.warning(request,"Appointment Booked Successfully")
        return redirect('/appointment')
    return render(request,"appointment.html",context)


def payment(request):
    price = request.GET.get('price')  # Get the price from URL parameters
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        name_on_card = request.POST.get('name_on_card')
        amount = request.POST.get('amount')  # Assuming amount is also submitted in the form

        # Assuming you need to convert amount to DecimalField
        # You might need to import Decimal from decimal module
        # amount = Decimal(amount)

        # You can directly create and save the Payment object
        payment = Payment(
            card_number=card_number,
            expiry_date=expiry_date,
            cvv=cvv,
            name_on_card=name_on_card,
            amount=amount
        )
        payment.save()

        messages.success(request, 'Your payment is successful')
        return redirect('/payment')  # Redirect to a success page

    # Render the payment form template if it's a GET request
    return render(request, 'payment.html', {'price': price})


def calculate_bmi(request):
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))

        # Calculate BMI
        bmi = calculate_bmi_value(weight, height)

        # Determine BMI category
        bmi_category = determine_bmi_category(bmi)

        return render(request, 'bmi_result.html',{'bmi': bmi,'bmi_category': bmi_category})

    return render(request, 'calculate_bmi.html')


def calculate_bmi_value(weight, height):
    # Formula: BMI = weight (kg) / (height (m))^2
    return round(weight / ((height / 100) ** 2), 2)


def determine_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'
    
def underweight_diet_chart_view(request):
    # Add your view logic here
    return render(request, 'underweight_diet_chart.html')

def normal_diet_chart_view(request):
    # Add your view logic here
    return render(request, 'normal_diet_chart.html')

def overweight_diet_chart_view(request):
    # Add your view logic here
    return render(request, 'overweight_diet_chart.html')

def obese_diet_chart_view(request):
    # Add your view logic here
    return render(request, 'obese_diet_chart.html')




def register(request, service_id):
    service = Service.objects.get(pk=service_id)
    context = {
        'service': service,
    }
    return render(request, 'register.html', context)

