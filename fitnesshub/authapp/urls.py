
from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('equipments',views.equipments,name="equipments"),
    path('attendance',views.attendance,name="attendance"),
    path('service',views.service,name="service"),
    path('appointment',views.appointment,name="appointment"),
    path('payment/', views.payment, name='payment'),
    path('calculate_bmi',views.calculate_bmi,name='calculate_bmi'),
    path('underweight-diet-chart/', views.underweight_diet_chart_view, name='underweight_diet_chart'),
    path('normal-diet-chart/', views.normal_diet_chart_view, name='normal_diet_chart'),
    path('overweight-diet-chart/', views.overweight_diet_chart_view, name='overweight_diet_chart'),
    path('obese-diet-chart/', views.obese_diet_chart_view, name='obese_diet_chart'),
    path('register/<int:service_id>/', views.register, name='register'),





    
]