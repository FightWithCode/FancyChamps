from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from accounts.models import Profile
from cricket_center.models import JoiningTransactionDetail
from payments.models import TransactionDetail
from itertools import chain
from .models import User
from . forms import AddMoneyForm, UpdateEmailForm, UpdateStateForm
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail,BadHeaderError
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from cricket_center.models import MatchDetail as MatchDetailCricket
from kabaddi_center.models import MatchDetail as MatchDetailKabaddi
# Uncomment for Celery
# from accounts.tasks import send_feedback_email_task


@login_required(login_url='IndexView')
def ProfileView(request):
    user_obj = User.objects.filter(id=request.user.id).first()
    is_email_confirmed = user_obj.profile.is_email_confirmed
    return render(request, 'accounts/profile.html', context={"user": user_obj,'is_email_confirmed':is_email_confirmed})


@login_required(login_url='IndexView')
def AddStateView(request):
    user_obj = User.objects.filter(id=request.user.id).first()
    args = {'user':user_obj}
    print("HeallYEah")
    if request.method == 'POST':
        print("Heall")
        form = UpdateStateForm(request.POST, instance=request.user.profile)
        # print(form.errors)
        if form.is_valid():
            profile = form.save()
            print(profile)
            print("is_valid")
            return redirect('/accounts/profile')
    else:
        print("aa")
        form = UpdateStateForm(instance=request.user)
        print(form)
        args.update({'form':form})
    return render(request, 'accounts/add_state.html', args)


@login_required(login_url='IndexView')
def AddEmailView(request):
    user_obj = User.objects.filter(id=request.user.id).first()
    args = {'user':user_obj}
    print("HeallYEah")
    if request.method == 'POST':
        print("Heall")
        form = UpdateEmailForm(request.POST, instance=request.user)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            print("is_valid")
            # message = render_to_string('account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain   ,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # try:
            #     result = send_mail(
            #         subject,
            #         message,
            #         '',
            #         [user.email]
            #     )
            # except BadHeaderError:
            #     print("Something")
            # plaintext = get_template('email.txt')

            current_site = get_current_site(request)
            subject = 'Welcome to FancyChamps! Confirm Your FancyChamps email.'
            htmly     = get_template('account_activation_email.html')

            d = { 'user': user, 'domain':current_site.domain, 'uemail':urlsafe_base64_encode(force_bytes(user.email)), 'uid':urlsafe_base64_encode(force_bytes(user.pk)), 'token': account_activation_token.make_token(user)}

            # subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
            text_content = ""
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, 'FancyChamps <verify@fancychamps.com>', [user.email])
            msg.attach_alternative(html_content, "text/html")
            try:
                print("I am here")
                msg.send(fail_silently=False)
                #UnComment if want to use Celery
                # send_feedback_email_task.delay(subject, text_content, user.email, html_content)
                user.save()
            except Exception as e:
                print("In except")
                print(e)
                print("Error while sending email!")
            return redirect('/accounts/profile')
    else:
        print("aa")
        form = UpdateEmailForm(instance=request.user)
        print(form)
        args.update({'form':form})
    return render(request, 'accounts/add_email.html', args)


def activate(request, uidb64, token, uemailb64):
    print("called")
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        uemail = force_text(urlsafe_base64_decode(uemailb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.profile.is_email_confirmed = True
        #user.profile.email_confirmed = True
        print(user.profile.is_email_confirmed)
        user.email = uemail
        user.save()
        user.profile.save()
        return redirect('/accounts/remove')
    else:
        return render(request, 'account_activation_email.html')


def RemoveStorage(request):
    variables = {
        'variable': "12531209"
    }
    return render(request, 'accounts/remove_storage.html', variables)


@login_required(login_url='IndexView')
def MyAccountView(request):
    user_obj = User.objects.filter(id=request.user.id).first()
    join_transaction_obj = JoiningTransactionDetail.objects.filter(transact_user__exact=request.user.username)
    transaction_obj = TransactionDetail.objects.filter(transact_user__exact=request.user.username, added_to_user__exact=True)#.order_by("-transaction_time")
    sorted_transaction = sorted(chain(join_transaction_obj, transaction_obj), key=lambda obj: obj.transaction_time, reverse=True)
    trans_obj = TransactionDetail.objects.filter(Q(added_to_user__exact=False), Q(transact_user__exact=request.user.username), Q(transaction_status__exact="TXN_SUCCESS"))
    print(len(trans_obj))
    if len(trans_obj)>=1:
        money_added_status = True
        trans = trans_obj.first()
        if trans.captured:
            trans.added_to_user = True
            trans.save()
            user_obj_profile = Profile.objects.get(user__username__exact=request.user.username)
            user_obj_profile.balance = user_obj_profile.balance + trans.transaction_amt
            user_obj_profile.save()
            money_added = True
            print(money_added)
            try:
                match_obj = get_object_or_404(MatchDetailCricket, match_slug__exact=trans.requested_match_slug)
                return redirect('/cricket_center/match/'+str(match_obj.match_slug))
            except :
                try:
                    match_obj = get_object_or_404(MatchDetailKabaddi, match_slug__exact=trans.requested_match_slug)
                    return redirect('/kabaddi_center/match/'+str(match_obj.match_slug))
                except:
                    pass
        else:
            print("3")
            money_added = False
            print(money_added)
    else:
        print("4")
        money_added=False
        money_added_status = False
    print(money_added,money_added_status)
    return render(request, 'accounts/my_account.html', context={"user": user_obj, "sorted_transaction": sorted_transaction, "money_added":money_added, "money_added_status":money_added_status})
