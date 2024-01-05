# import section
from django.shortcuts import render,redirect

# importing random function
from random import randint

# importing settings.py
from django.conf import settings

# for email utility
from django.core.mail import send_mail

#importing DB tables from models.py
from Patient.models import Patient
from Doctor.models import Doctor_table,DepartmentTable

# Create your views here.

def home(request):
    if 'email' in request.session:
        user_data = Patient.objects.get(email = request.session['email'])
        return render(request, 'index.html',{'user_data': user_data})
    else:
        return render(request, 'index.html')

def about(request):
    if 'email' in request.session:
        user_data = Patient.objects.get(email = request.session['email'])
        return render(request, 'about.html',{'user_data': user_data})
    else:
        return render(request, 'about.html')

def department(request):
    dept_data = DepartmentTable.objects.all()
    if 'email' in request.session:
        user_data = Patient.objects.get(email = request.session['email'])
        return render(request, 'services.html',{'user_data': user_data, 'dept_data':dept_data})
    else:
        return render(request, 'services.html',{'dept_data':dept_data})

def contact(request):
    if 'email' in request.session:
        user_data = Patient.objects.get(email = request.session['email'])
        return render(request, 'contact.html',{'user_data': user_data})
    else:
        return render(request, 'contact.html')


def register(request):
    global c_otp
    # when we click on register option
    if request.method == 'GET':
        return render(request, 'register.html')
    
    # when we click on register button
    else:
       
        # checking whether the entered email is already used for registration
        try:
            # error occurs when there is no email match
            # then control goes to except block

            Patient.objects.get(email = request.POST['email'])
            return render(request,'register.html',{'msg':"Email already registered, try using other Email"})
        
        except:
            # validating password and confirm password
            if request.POST['password'] == request.POST['cpassword']:
                #  generating otp
                global c_otp
                c_otp = randint(100_000,999_999)

                #extracting data from registration form
                global reg_form_data 

                reg_form_data = {
                    "full_name" : request.POST['full_name'],
                    "gender" : request.POST['gender'],
                    "age" : request.POST['age'],
                    "blood_group" : request.POST['blood_group'],
                    "email" : request.POST['email'],
                    "phoneno" : request.POST['phoneno'],
                    "address" : request.POST['address'],
                    "password" : request.POST['password'],
                }

                # sending the generated OTP via mail
                subject = "Medick Registration"
                message = f'Hello{reg_form_data["full_name"]}, Welcome to Medick. Your OTP is {c_otp}'
                sender = settings.EMAIL_HOST_USER
                receiver = [reg_form_data['email']]
                send_mail(subject, message, sender, receiver)

                #after sending OTP render the page to enter OTP
                return render(request,'otp.html')

            else:
                return render(request, 'register.html',{'msg':"Both Passwords didn't match"})
            
def otp(request):
    if str(c_otp) == request.POST['u_otp']:
        Patient.objects.create(full_name=reg_form_data['full_name'], gender = reg_form_data['gender'], age = reg_form_data['age'], blood_group = reg_form_data['blood_group'], email = reg_form_data['email'], phoneno = reg_form_data['phoneno'], address = reg_form_data['address'], password = reg_form_data['password'])
        return render(request,'register.html', {'msg': "Registration Successfull !! Account created"})
    else:
        return render(request, 'otp.html',{'msg':"Invalid OTP"})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            # finding the record of person trying to login in database
            session_user = Patient.objects.get(email = request.POST['email'])
            if request.POST['password'] == session_user.password:
                request.session['email'] = session_user.email
                return redirect('home')
            else:
                return render(request, 'login.html', {'msg':'invalid password'})
        except:
            return render(request, 'login.html',{'msg': 'This email is not Registered !!'})
                

def appoint(request):
    special_data = DepartmentTable.objects.all()
    # doctor_data = Doctor_table.objects.filter(dept_id = DepartmentTable.objects.all(dept_name = request.POST['special']))
    if request.method == 'GET':
        return render(request,'appoint.html',{'special_data':special_data})
    else:
        pass


def logout(request):
    del request.session['email']
    return redirect('home')

def doctor(request):
    if 'doctor_email'not in request.session:
        return render(request, "doctor_index.html")
    else:
        doctor_data = Doctor_table.objects.get(email = request.session['doctor_email'])
        return render(request, "doctor_index.html",{'doctor_data': doctor_data})

        