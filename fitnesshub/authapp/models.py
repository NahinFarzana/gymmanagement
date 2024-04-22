from django.db import models
from datetime import datetime
# Create your models here.
#Will create database table here
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self):
        return self.email
    

class Enrollment(models.Model):        
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    SelectMembershipplan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(max_length=55,blank=True,null=True)
    DueDate=models.DateTimeField(blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField(max_length=25)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)

    def __int__(self):
        return self.id


class Equipments(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='equipments')
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    def __int__(self):
        return self.id
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='service', null=True, blank=True)
    description = models.TextField()
    fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    starts_from = models.DateTimeField(default=datetime.now) 
    ends_on = models.DateTimeField(default=datetime.max)  # Default value
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   


class Appointment(models.Model):
    full_name = models.CharField(max_length=150)
    user_phone = models.CharField(max_length=20)
    trainer=models.CharField(max_length=200, default='')
    date_and_time = models.DateTimeField()
    duration = models.DurationField()
    appointment_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20)


import datetime
class Payment(models.Model):
    card_number = models.CharField(max_length=16, null=True)
    expiry_date = models.DateField(default=datetime.date.today)
    cvv = models.CharField(max_length=4,null=True)
    name_on_card = models.CharField(max_length=100, default='Visa')  # Default value is set to 'Visa'
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)  

