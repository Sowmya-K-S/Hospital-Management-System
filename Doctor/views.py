from django.shortcuts import render, redirect
from Doctor.models import DepartmentTable,DoctorTable


# Create your views here.
def home(request):
    return render(request, 'd_index.html')

def about(request):
    return render(request, 'd_header.html')

"""def department(request):
    return render(request, 'd_login.html')

def contact(request):
    return render(request, 'd_register.html')

def register(request):
    return render(request, 'd_otp.html')"""

"""def login(request):
    return render(request, 'login.html')

def appoint(request):
    return render(request,'appoint.html')"""