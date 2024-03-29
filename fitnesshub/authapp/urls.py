
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


    
]