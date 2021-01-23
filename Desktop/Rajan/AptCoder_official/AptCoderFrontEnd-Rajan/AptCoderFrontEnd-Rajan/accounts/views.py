from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
import uuid, re
from .models import *
from .forms import CreateUserForm,InformationForm

is_registerd =False

def register_view(request):
    global is_registered
    is_registered = False
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data.get('email')).exists():
                messages.info(request, 'This email is already registered')
                return render(request, 'accounts/register.html', {'form': form})
            else:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                message = render_to_string('acc_active_email.html', {
                    'user':user, 'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                # Sending activation link in terminal
                # user.email_user(subject, message)
                mail_subject = 'Activate your account.'
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return render(request, 'webDevelopment/confirm_email.html')
            # return render(request, 'acc_active_sent.html')
        form = CreateUserForm()
        return render(request, 'accounts/register.html', {'form': form})
    else:
        form = CreateUserForm()
        return render(request, 'accounts/register.html', {'form': form})


def oneClickRegistration(request):
    global is_registered
    is_registered = True
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        userMail = request.POST['email']
        username = re.split('@', userMail)[0]
        print(userMail)
        print(username)
        if User.objects.filter(email=request.POST['email']).exists():
            messages.info(request, 'This email is already registered, Please register with a new email!')
            return render(request, 'accounts/register.html', {'form': form})
        else:
            user = User.objects.create_user(
                username=username,
                password='password@123',
                email=userMail,
            )
            user.save()
            current_site = get_current_site(request)
            couponCode = getCouponCode()
            print("coupon code called")
            print(couponCode)
            message = render_to_string('acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'couponCode': couponCode,
                'coupon': "<b>Coupon Code</b>",
                'fb': "<b>Our Facebook Page:</b>",
                'lk': "<b>Our Linkedin Page:</b>",
                'address': "<b>Our Company Address:</b>",
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)

            # unique coupon code created for each registered user
            coupon_code, created = CouponCode.objects.get_or_create(user=user, coupon=couponCode)



            message = message
            mail_subject = 'Activate your account, and get one class fee waved off'
            to_email = userMail
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request,'webDevelopment/confirm_email.html',{'couponCode':couponCode,})
    else:
        print("Call happened no data found")

def getCouponCode():
    token = str(uuid.uuid4())
    return token


def registered_courselist(request):
    course_li = Course_Registration.objects.all()
    free_course,created = UserModel.objects.get_or_create(user=request.user,course=course_li[0])
    return render(request,'accounts/registered_course.html',{'course_li':course_li})



def information_details(request):
    if request.method == 'POST':
        form1 = InformationForm(request.POST)
        if form1.is_valid():
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            address = form1.cleaned_data['address']
            contact_number = form1.cleaned_data['contact_number']
            # coupon_code = form1.cleaned_data['coupon_code']
            inf, created = InformationModel.objects.get_or_create(user=request.user, first_name=first_name,
                                                                  last_name=last_name,
                                                                  address=address, contact_number=contact_number)
            return redirect(registered_courselist)
    form1 =  InformationForm()
    return render(request,'accounts/information.html',{'form1':form1,})





def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        if is_registered:
            return redirect(information_details)
        else:
            return render(request, 'webDevelopment/email_confirmed.html')
        # return render(request, 'webDevelopment/email_confirmed.html')
    else:
        return HttpResponse('Activation link is invalid!')	


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/registered_course')
        else:
            messages.info(request, 'Username or Password is incorrect')


    context = {}
    # return redirect('/registered_course')
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def coupon_code_verify(request,pk):
    coupon_code = request.POST.get('coupon')
    print(coupon_code)
    if CouponCode.objects.filter(coupon=coupon_code).exists():
        course = Course_Registration.objects.get(pk =pk)
        course_packege = UserModel.objects.get(user = request.user,course=course)
        print(course_packege)

        course.is_free = True
        course.save()
        print(course.is_free)

        print("*************")
        print(course_packege.course.fees)
        return redirect(registered_courselist)
    else:
        messages.info(request, 'please enter the valid coupon code')
        return redirect(registered_courselist)