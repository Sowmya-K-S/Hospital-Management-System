# import section
from django.shortcuts import render,redirect

# importing random function
from random import randint

# importing settings.py
from django.conf import settings

# for email utility
from django.core.mail import send_mail

#importing DB tables from models.py
from Doctor.models import Doctor_table,DepartmentTable
from Patient.models import Appoint




# Create your views here.

def doctor_about(request):
    doctor_list = Doctor_table.objects.all()
    if 'doctor_email' in request.session:
        doctor_data = Doctor_table.objects.get(email = request.session['doctor_email'])
        return render(request, 'doctor_about.html',{'doctor_data':doctor_data, 'doctor_list':doctor_list})
    else:
        return render(request, 'doctor_about.html',{'doctor_list':doctor_list})

def doctor_department(request):
    dept_data = DepartmentTable.objects.all()
    if 'doctor_email' in request.session:
        doctor_data = Doctor_table.objects.get(email = request.session['doctor_email'])
        return render(request, 'doctor_services.html',{'doctor_data':doctor_data, 'dept_data':dept_data})
    else:
        return render(request, 'doctor_services.html',{'dept_data':dept_data})

def doctor_contact(request):
    if 'doctor_email' in request.session:
        doctor_data = Doctor_table.objects.get(email = request.session['doctor_email'])
        return render(request, 'doctor_contact.html',{'doctor_data':doctor_data})
    else:
        return render(request, 'doctor_contact.html')



def doctor_reg(request):
    global c_otp
    # when we click on register option
    if request.method == 'GET':
        return render(request, 'doctor_register.html')
    
    # when we click on register button
    else:
       
        # checking whether the entered email is already used for registration
        try:
            # error occurs when there is no email match
            # then control goes to except block

            Doctor_table.objects.get(email = request.POST['email'])
            return render(request,'doctor_register.html',{'msg':"Email already registered, try using other Email"})
        
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
                    "special" : request.POST['special'],
                    "degree" : request.POST['degree'],
                    "y_of_exp" : request.POST['y_of_exp'],
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
                return render(request,'doctor_otp.html')

            else:
                return render(request, 'doctor_register.html',{'msg':"Both Passwords didn't match"})

def doctor_otp(request):
    if str(c_otp) == request.POST['u_otp']:
        Doctor_table.objects.create(full_name=reg_form_data['full_name'], special = reg_form_data['special'], degree = reg_form_data['degree'], y_of_exp = reg_form_data['y_of_exp'], email = reg_form_data['email'], phoneno = reg_form_data['phoneno'], address = reg_form_data['address'], password = reg_form_data['password'], dept = DepartmentTable.objects.get(dept_name=reg_form_data['special']) )
        return render(request,'doctor_register.html', {'msg': "Registration Successfull !! Account created"})
    else:
        return render(request, 'doctor_otp.html',{'msg':"Invalid OTP"})


def doctor_login(request):
    if request.method == 'GET':
        return render(request, 'doctor_login.html')
    else:
        try:
            # finding the record of person trying to login in database
            session_doctor = Doctor_table.objects.get(email = request.POST['email'])
            if request.POST['password'] == session_doctor.password:
                request.session['doctor_email'] = session_doctor.email
                doctor_data = Doctor_table.objects.get(email = request.session['doctor_email'] )
                return render(request, 'doctor_index.html',{'doctor_data': doctor_data})
            else:
                return render(request, 'doctor_login.html', {'msg':'invalid password'})
        except:
            return render(request, 'doctor_login.html',{'msg': 'This email is not Registered !!'})


def doctor_logout(request):
    del request.session['doctor_email']
    return redirect('doctor')

def dashboard(request):
    doctor_data = Doctor_table.objects.get(email = request.session['doctor_email'] )
    return render(request,'d_index.html',{'doctor_data':doctor_data})

def view_appoint(request):
    doctor_data = Doctor_table.objects.get(email = request.session['doctor_email'] )
    appointment_list = Appoint.objects.filter(doctor_name= doctor_data.full_name)
    return render(request,'view_appoint.html',{'doctor_data':doctor_data, 'appointment_list':appointment_list})

