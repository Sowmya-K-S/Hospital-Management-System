# import section
from django.shortcuts import render,redirect

#for razorpay functionality
import razorpay
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# importing random function
from random import randint

# importing settings.py
from django.conf import settings



# for email utility
from django.core.mail import send_mail

#importing DB tables from models.py
from Patient.models import Patient,Appoint
from Doctor.models import Doctor_table,DepartmentTable

# Create your views here.

# razor pay client
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


from django.utils import timezone 
from django.http import JsonResponse

# Create your views here.

def home(request):
    if 'email' in request.session:
        user_data = Patient.objects.get(email = request.session['email'])\
       
        return render(request, 'index.html',{'user_data': user_data})
    else:
        return render(request, 'index.html')

def about(request):
    doctor_list = Doctor_table.objects.all()
    if 'email' in request.session:
        user_data = Patient.objects.get(email = request.session['email'])
        return render(request, 'about.html',{'user_data': user_data,'doctor_list':doctor_list})
    else:
        return render(request, 'about.html',{'doctor_list':doctor_list})

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
    global special_data
    special_data = DepartmentTable.objects.all()
   
    if request.method == 'POST':
            one_day_appointments  = Appoint.objects.filter(a_date = request.POST['a_date'],specialisation = request.POST['special'], doctor_name = request.POST['doctor_name'] )
            if one_day_appointments:
                return render(request, 'appoint.html',{'msg':'Doctor is not available on this date', 'special_data':special_data})
            else:
                appoint_date = request.POST['a_date']
                if appoint_date  >= str(timezone.now().date()) :
                    global Appoint_object
                    Appoint_object = {'a_date' : request.POST['a_date'],'specialisation' : request.POST['special'], 'doctor_name' : request.POST['doctor_name']}
                    context = {
                                'appoint_data':Appoint_object,
                                'appoint_price':500
                              }
                    global amount
                    amount = 500 * 100 #paise version
                    currency = 'INR'
                    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

                    razorpay_order_id = razorpay_order['id']
                    callback_url = 'paymenthandler/'

                    # context dictionary
                    context['razorpay_order_id'] = razorpay_order_id
                    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
                    context['razorpay_amount'] = amount
                    context['currency'] = currency
                    context['callback_url'] = callback_url
                    return render(request, 'payment.html', context=context)
                else:
                    return render(request, 'appoint.html',{'msg':'Enter a valid date', 'special_data':special_data})

    else:
        return render(request, 'appoint.html', {'special_data': special_data})
    

def logout(request):
    del request.session['email']
    return redirect('home')

def doctor(request):
    if 'doctor_email'not in request.session:
        return render(request, "doctor_index.html")
    else:
        doctor_data = Doctor_table.objects.get(email = request.session['doctor_email'])
        return render(request, "doctor_index.html",{'doctor_data': doctor_data})


# for dependent dropdown rendering 
def get_doctors(request):
    specialization = request.GET.get('specialization', None)
    if specialization:
        doctors = Doctor_table.objects.filter(special=specialization)
        doctor_list = [{'id': doctor.id, 'name': doctor.full_name} for doctor in doctors]
        return JsonResponse({'doctors': doctor_list})
    else:
        return JsonResponse({'error': 'Specialization not provided'})
       
@csrf_exempt
def paymenthandler(request):

    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                f_amount = amount 

                try:
                    # capture the payment
                    razorpay_client.payment.capture(payment_id, f_amount)

                    #creating appointment for that item
                    Appoint.objects.create(a_date = Appoint_object['a_date'], special = Appoint_object['specialisation'], doctor_name = Appoint_object['doctor_name'])
        
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')

                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')

        except:
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
    




