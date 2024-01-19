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
from django.conf.urls.static import static
from Patient.views import *
from Doctor.views import *

urlpatterns = [

    # urls for patient app
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
    path('get_doctors/', get_doctors, name='get_doctors'),

    path('payment/paymenthandler/', paymenthandler, name = "paymenthandler"),
  
    

    
    # urls for doctor app
    path('doctor/',doctor,name="doctor"),
    path('doctor_about/',doctor_about, name = "doctor_about"),
    path('doctor_department/',doctor_department, name = "doctor_department"),
    path('doctor_contact/',doctor_contact, name = "doctor_contact"),
    path('doctor_reg/', doctor_reg, name="doctor_reg"),
    path('doctor_login/', doctor_login, name="doctor_login"),
    path('doctor_otp/',doctor_otp, name="doctor_otp"),
    path('dashboard/',dashboard, name = "dashboard"),
    path('doctor_logout/', doctor_logout, name = "doctor_logout"),
    path('view_appoint/',view_appoint,name = "view_appoint"),
  


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)