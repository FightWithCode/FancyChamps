from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from accounts.forms import UserForm, ProfileForm, UserLogInForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import http.client
from accounts.models import OTPVerification, OTPVerificationEmail
import ast
from django.core.mail import send_mail, BadHeaderError
from django.utils.crypto import get_random_string
from support.forms import SupportQuerriesForm
from django.shortcuts import render_to_response
from accounts.models import User, Profile, TempUser, FailedLoginAttempt
from datetime import timedelta, datetime
from django.utils import timezone
# class IndexView(TemplateView):
#     template_name = "index.html"


# def handler404(request):
#     #return HttpResponseRedirect(reverse('IndexView'))
#     return render(request, 'error.html',{})
def SiteMapView(request):
    return render(request, 'sitemap.xml',{})


def handler404(request, *args, **argv):
    print("asfasdas")
    response = render_to_response('error.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    print("500")
    response = render_to_response('error.html')
    response.status_code = 500
    return response


def VerifyLoginDetailView(request):
    print("Called")
    print(request.POST)
    data = {
        'matched': False,
    }
    return JsonResponse(data)


def PrivacyPolicy(request):
    return render(request, 'privacy.html',{})


def PromotionsView(request):
    return render(request, 'promotions.html',{})


def HowToPlay(request):
    return render(request, 'how_to_play.html',{})


def PointSystem(request):
    return render(request, 'points_system.html',{})


def PointSystemKabaddi(request):
    print(".........................................")
    return render(request, 'points_system_kabaddi.html',{})


def Faqs(request):
    return render(request, 'faqs.html',{})


def AboutUs(request):
    return render(request, 'about_us.html',{})


def ContastUs(request, submitted):
    print(type(submitted))
    form = SupportQuerriesForm(request.POST or None, initial={'user':request.user.username})
    if request.method == 'POST':
        form = SupportQuerriesForm(request.POST)
        if form.is_valid():
            print(request.user.username)
            form.save()
            url = reverse('contact_us', kwargs={'submitted': 1})
            return HttpResponseRedirect(url)
    else:
        print(type(submitted))
        return render(request, 'contact_us.html',{"form":form, 'submitted':submitted})

def Terms(request):
    return render(request, 'terms.html',{})


def Legality(request):
    return render(request, 'legality.html',{})


def MobileVerifyView(request):
    mobile_no = request.POST['verify_it']
    if len(mobile_no) == 10 and (not Profile.objects.filter(phone_number__iexact=mobile_no).exists()):
        # conn = http.client.HTTPConnection("2factor.in")
        # payload = ""
        # # https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/AUTOGEN/FancyChamps OTP
        # headers = {'content-type': "application/x-www-form-urlencoded"}
        # conn.request("GET", "/API/V1/ed3da657-699c-11e9-90e4-0200cd936042/SMS/" + mobile_no + "/AUTOGEN/FancyChamps+OTP", payload, headers)
        # res = conn.getresponse()
        # data_of_2f = res.read()
        # responce_from_2f = ast.literal_eval(data_of_2f.decode("utf-8"))
        # print(responce_from_2f['Status'])
        # if responce_from_2f['Status'] == 'Success':
        #     otp_veri_obj = OTPVerification(
        #             mobile_no=mobile_no,
        #             otp_send_detail=responce_from_2f['Details'],
        #     )
        #     otp_veri_obj.save()
        data = {
            'digits_valid': True,
            'mobile_no': mobile_no,
            'otp_send': True,
        }
        # else:
        #     data = {
        #         'digits_valid': False,
        #     }
    # else:
    #     data = {
    #         'digits_valid': False,
    #     }
    elif(not len(mobile_no) == 10):
        data = {
            'digits_valid': False,
        }

    elif(Profile.objects.filter(phone_number__iexact=mobile_no).exists()):
        data = {
                'mobile_taken': True,
        }

    return JsonResponse(data)


def MobileOTPVerifyView(request):
    print("I for called")
    print(request.POST)
    username = request.POST['someuser']
    otp = request.POST['verify_otp']
    temp_user_obj = TempUser.objects.filter(username__iexact=username).latest("pk")
    mobile_no = temp_user_obj.mobile_no
    print(otp)
    print(username)
    print(mobile_no)
    otp_obj = OTPVerification.objects.filter(mobile_no__exact=mobile_no).order_by('-sent_time').first()
    details = otp_obj.otp_send_detail
    print(details)
    conn = http.client.HTTPConnection("2factor.in")
    payload = ""
    headers = {'content-type': "application/x-www-form-urlencoded"}
    # https://2factor.in/API/V1/6dc69c9e-e414-11e8-a895-0200cd936042/SMS/VERIFY/42dff03e-e417-11e8-a895-0200cd936042/646481
    conn.request("GET", "/API/V1/ed3da657-699c-11e9-90e4-0200cd936042/SMS//VERIFY/" + details + "/" + otp, payload, headers)
    res = conn.getresponse()
    data_of_2f = res.read()
    responce_from_2f = ast.literal_eval(data_of_2f.decode("utf-8"))
    print("print it")
    print(responce_from_2f)
    if responce_from_2f['Status'] == 'Success' and responce_from_2f['Details'] == 'OTP Matched':
        data = {
            'otp_matched_status': True,
        }
        user = User(username=username)
        user.set_password(temp_user_obj.password)
        user.save()
        profile = Profile(phone_number=mobile_no)
        profile.user = user
        profile.save()
        new_user = authenticate(username=username,
                        password=temp_user_obj.password,
                        )
        print(new_user)
        login(request, new_user)
        temp_user_obj.delete()
    else:
        data = {
            'otp_matched_status': False,
        }
    return JsonResponse(data)


def EmailVerifyView(request):
    email = request.POST['verify_it']
    if email.endswith('@gmail.com') and (not User.objects.filter(email__iexact=email).exists()):
        data = {
            'email_valid': True,
            'variable': "12531209",
            'value_of': 12531209,
        }
    elif(not email.endswith('@gmail.com')):
        data = {
            'email_valid': False,
        }

    elif(User.objects.filter(email__iexact=email).exists()):
        data = {
                'email_taken': True,
        }
    return JsonResponse(data)


def EmailOTPVerifyView(request):
    print("I for called")
    email = request.POST['verify_this_email']
    otp = request.POST['verify_otp']
    otp_obj = OTPVerificationEmail.objects.filter(email__exact=email).order_by('-sent_time').first()
    entered_otp = otp_obj.otp_send
    print("print it")
    if otp == entered_otp:
        data = {
            'otp_matched_status': True,
        }
    else:
        data = {
            'otp_matched_status': False,
        }

    return JsonResponse(data)


@login_required(login_url='IndexView')
def UserLogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('IndexView'))


def IndexView(request):
    print("main")
    if request.user.is_authenticated():
        return HttpResponseRedirect('kabaddi_center')
    else:
        print("main else")
        registered = False
        mobile_no = ""
        username = ""
        otp_send = False
        digits_valid = False
        user_form = UserForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None)
        login_form = UserLogInForm(request.POST or None)
        print(request.method)
        if request.method == 'POST':
            print("if of post")
            if request.POST.get('submit') == 'Login':
                print("if of login")
                login_form = UserLogInForm(data=request.POST)
                if login_form.is_valid:
                    username = login_form.data.get("username")
                    password = login_form.data.get("password")
                    time_threshold = timezone.now() - timedelta(minutes=30)
                    failed_attempts = FailedLoginAttempt.objects.filter(user__exact=username, failed_time__gt=time_threshold)
                    print(failed_attempts)
                    if failed_attempts.count() > 2:
                        print("called")
                        try:
                            user_obj = get_object_or_404(User, username__exact=username)
                            print("trt called")
                            if user_obj.is_active:
                                print("trt called if")
                                return render(request, 'index.html',
                                  {
                                    'user_form': user_form,
                                    'profile_form': profile_form,
                                    'login_form': login_form,
                                    'locked': True
                                  })
                            else:
                                print("trt called else")
                                user_obj.is_active = False
                                user_obj.save()
                                locked = True
                                print(locked)
                                return render(request, 'index.html',
                                  {
                                    'user_form': user_form,
                                    'profile_form': profile_form,
                                    'login_form': login_form,
                                    'locked': locked,
                                  })
                        except User.DoesNotExist:
                            print("User Does not Exists")
                    else:
                        user = authenticate(username=username, password=password)
                        if user:
                            # Check it the account is active
                            if user.is_active:
                                # Log the user in.
                                login(request, user)
                                user.save()
                                return HttpResponseRedirect('kabaddi_center')
                            else:
                                # If account is not active:
                                return render(request, 'index.html',
                                  {
                                    'user_form': user_form,
                                    'profile_form': profile_form,
                                    'login_form': login_form,
                                    'locked': True
                                  })
                        else:
                            login_error = True
                            print(request.META.get('HTTP_X_REAL_IP'))
                            print("Someone tried to login and failed.")
                            print("They used username: {} and password: {}".format(username, password))
                            # failed_attempts_obj = FailedLoginAttempt(user=username, ip=request.META.get('HTTP_X_REAL_IP'))
                            failed_attempts_obj = FailedLoginAttempt(user=username, ip=request.META.get('REMOTE_ADDR'))
                            failed_attempts_obj.save()
                            return render(request, 'index.html',
                                  {
                                    'user_form': user_form,
                                    'profile_form': profile_form,
                                    'login_form': login_form,
                                    'login_error': login_error
                                  })
            print("no post from center")
            print(request.POST)
            if request.POST.get('submit_btn') == 'Continue':
                print("if of regi")
                print("Hello World...")
                user_form = UserForm(data=request.POST)
                profile_form = ProfileForm(data=request.POST)
                if user_form.is_valid() and profile_form.is_valid():
                    # user = user_form.save(commit=False)
                    # user.set_password(user.password)
                    # #user.save()
                    # profile = profile_form.save(commit=False)
                    # profile.user = user
                    # #profile.save()
                    # print(user_form.cleaned_data)
                    # print(profile_form.cleaned_data)
                    print("Success")
                    temp_user_obj = TempUser(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'], mobile_no=profile_form.cleaned_data['phone_number'])
                    mobile_no = profile_form.cleaned_data['phone_number']
                    conn = http.client.HTTPConnection("2factor.in")
                    payload = ""
                    # https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/AUTOGEN/FancyChamps OTP
                    headers = {'content-type': "application/x-www-form-urlencoded"}
                    conn.request("GET", "/API/V1/ed3da657-699c-11e9-90e4-0200cd936042/SMS/" + mobile_no + "/AUTOGEN/FancyChamps+OTP", payload, headers)
                    res = conn.getresponse()
                    data_of_2f = res.read()
                    responce_from_2f = ast.literal_eval(data_of_2f.decode("utf-8"))
                    print(responce_from_2f['Status'])
                    if responce_from_2f['Status'] == 'Success':
                        otp_veri_obj = OTPVerification(
                                mobile_no=mobile_no,
                                otp_send_detail=responce_from_2f['Details'],
                        )
                        otp_veri_obj.save()
                        temp_user_obj.save()
                        digits_valid =  True
                        otp_send =  True
                        username = user_form.cleaned_data['username']
                    else:
                        digits_valid = False
                    print(digits_valid, otp_send)
                    #mobile_no = profile_form.cleaned_data['phone_number']
                    #otp_send=True
                    #print(user_form.cleaned_data['username'], user_form.cleaned_data['password'])
                    # new_user = authenticate(username=user_form.cleaned_data['username'],
                    #                 password=user_form.cleaned_data['password'],
                    #                 )
                    # print(new_user)
                    # login(request, new_user)
                    #return HttpResponseRedirect('cricket_center')

                else:
                    print(user_form.errors, profile_form.errors)
        return render(request, 'index.html',
                              {
                                'user_form': user_form,
                                'profile_form': profile_form,
                                'login_form': login_form,
                                'digits_valid': digits_valid,
                                'otp_send': otp_send,
                                'mobile_no':mobile_no,
                                'username':username
                              })


def csrf_failure(request, reason=""):
    # csrf_error = True
    # return render(request, 'index.html',
    #                           {
    #                             'user_form': user_form,
    #                             'profile_form': profile_form,
    #                             'login_form': login_form,
    #                             'registered': registered
    #                           })
    return HttpResponseRedirect(reverse('IndexView'))

def CheckEnteredData(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

