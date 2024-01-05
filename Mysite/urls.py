"""
URL configuration for Mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Patient.views import *
from Doctor.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/',about, name = "about"),
    path('department/',department, name = "department"),
    path('contact/',contact, name = "contact"),
    path('register/',register, name = "register"),
    path('login/',login, name = "login"),
    path('appoint/',appoint, name = "appoint"),
    path('otp/', otp, name = "otp"),
    path('logout/', logout, name = "logout"),
    path('doctor/',doctor,name="doctor"),
    path('doctor_reg', doctor_reg, name="doctor_reg"),
    path('doctor_login/', doctor_login, name="doctor_login"),
    path('doctor_otp/',doctor_otp, name="doctor_otp"),
    path('dashboard/',dashboard, name = "dashboard"),
    path('doctor_logout/', doctor_logout, name = "doctor_logout"),


]
