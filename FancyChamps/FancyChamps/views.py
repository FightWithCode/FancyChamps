from django.shortcuts import render
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
from accounts.models import User, Profile

# class IndexView(TemplateView):
#     template_name = "index.html"


# def handler404(request):
#     #return HttpResponseRedirect(reverse('IndexView'))
#     return render(request, 'error.html',{})

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


def HowToPlay(request):
    return render(request, 'how_to_play.html',{})


def PointSystem(request):
    return render(request, 'points_system.html',{})


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
            data = {
                'digits_valid': True,
                'mobile_no': mobile_no,
                'otp_send': True,
            }
        else:
            data = {
                'digits_valid': False,
            }
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
    mobile = request.POST['verify_this_mobile']
    otp = request.POST['verify_otp']
    otp_obj = OTPVerification.objects.filter(mobile_no__exact=mobile).order_by('-sent_time').first()
    details = otp_obj.otp_send_detail
    conn = http.client.HTTPConnection("2factor.in")
    payload = ""
    headers = {'content-type': "application/x-www-form-urlencoded"}
    # https://2factor.in/API/V1/6dc69c9e-e414-11e8-a895-0200cd936042/SMS/VERIFY/42dff03e-e417-11e8-a895-0200cd936042/646481
    conn.request("GET", "/API/V1/ed3da657-699c-11e9-90e4-0200cd936042/SMS//VERIFY/" + details + "/" + otp, payload, headers)
    res = conn.getresponse()
    data_of_2f = res.read()
    responce_from_2f = ast.literal_eval(data_of_2f.decode("utf-8"))
    print("print it")
    if responce_from_2f['Status'] == 'Success' and responce_from_2f['Details'] == 'OTP Matched':
        data = {
            'otp_matched_status': True,
        }
    else:
        data = {
            'otp_matched_status': False,
        }
    return JsonResponse(data)


def EmailVerifyView(request):
    email = request.POST['verify_it']
    if email.endswith('@gmail.com') and (not User.objects.filter(email__iexact=email).exists()):
        generated_otp = get_random_string(length=6, allowed_chars='1234567890')
        try:
            result = send_mail(
                'FancyChamps OTP Verification Email.',
                'Hello! Champ, Welcome to FancyChamps.\nUse this below given Six Digit OTP for your Email Verification \n\n' + str(generated_otp) + '\n\nWe Hope to see you on the Leaderboard Soon.\nThankyou.',
                '',
                [email],
            )
            print(result)
            data = {
                'email_valid': True,
                'email_send': True,
            }
            if result:
                otp_veri_obj = OTPVerificationEmail(
                    email=email,
                    otp_send=generated_otp,
                )
            otp_veri_obj.save()

        except BadHeaderError:
            data = {
                'email_valid': True,
                'email_send': False,
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
    if request.user.is_authenticated():
        return HttpResponseRedirect('cricket_center')
    else:
        registered = False
        user_form = UserForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None)
        login_form = UserLogInForm(request.POST or None)
        if request.method == 'POST':
            if request.POST.get('submit') == 'Login':
                login_form = UserLogInForm(data=request.POST)
                if login_form.is_valid:
                    username = login_form.data.get("username")
                    password = login_form.data.get("password")
                    user = authenticate(username=username, password=password)
                    if user:
                        # Check it the account is active
                        if user.is_active:
                            # Log the user in.
                            login(request, user)
                            user.save()
                            return HttpResponseRedirect('cricket_center')
                        else:
                            # If account is not active:
                            return HttpResponse("Your account is not active.")

                    else:
                        login_error = True
                        print("Someone tried to login and failed.")
                        print("They used username: {} and password: {}".format(username, password))
                        return render(request, 'index.html',
                              {
                                'user_form': user_form,
                                'profile_form': profile_form,
                                'login_form': login_form,
                                'login_error': login_error
                              })
            if request.POST.get('submit') == 'Register':
                user_form = UserForm(data=request.POST)
                profile_form = ProfileForm(data=request.POST)
                if user_form.is_valid() and profile_form.is_valid():
                    user = user_form.save(commit=False)
                    user.set_password(user.password)
                    user.save()
                    profile = profile_form.save(commit=False)
                    profile.user = user
                    profile.save()
                    registered = True
                else:
                    print(user_form.errors, profile_form.errors)
        return render(request, 'index.html',
                              {
                                'user_form': user_form,
                                'profile_form': profile_form,
                                'login_form': login_form,
                                'registered': registered,
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


