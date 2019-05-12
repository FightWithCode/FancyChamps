from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from accounts.models import Profile
from cricket_center.models import JoiningTransactionDetail
from payments.models import TransactionDetail
from itertools import chain
from .models import User
from . forms import AddMoneyForm


@login_required(login_url='IndexView')
def ProfileView(request):
    user_obj = User.objects.filter(username__exact=request.user.username).first()
    return render(request, 'accounts/profile.html', context={"user": user_obj})


@login_required(login_url='IndexView')
def MyAccountView(request):
    user_obj = User.objects.filter(username__exact=request.user.username).first()
    join_transaction_obj = JoiningTransactionDetail.objects.filter(transact_user__exact=request.user.username)
    transaction_obj = TransactionDetail.objects.filter(transact_user__exact=request.user.username)#.order_by("-transaction_time")
    sorted_transaction = sorted(chain(join_transaction_obj, transaction_obj), key=lambda obj: obj.transaction_time, reverse=True)
    trans_obj = TransactionDetail.objects.filter(Q(added_to_user__exact=False), Q(transact_user__exact=request.user.username))
    print(len(trans_obj))
    if len(trans_obj)>=1:
        print(trans_obj)
        money_added_status = True
        trans = trans_obj.first()
        print(trans)
        if trans.captured:
            print("second IF")
            trans.added_to_user = True
            trans.save()
            user_obj_profile = Profile.objects.get(user__username__exact=request.user.username)
            user_obj_profile.balance = user_obj_profile.balance + trans.transaction_amt
            user_obj_profile.save()
            money_added = True
            print(money_added)
        else:
            print("3")
            money_added = False
            print(money_added)
    else:
        print("4")
        money_added=False
        money_added_status = False
    print(money_added,money_added_status)
    return render(request, 'accounts/my_account.html', context={"user": user_obj, "total_balance": user_obj.profile.balance + user_obj.profile.bonus + user_obj.profile.widhdrawable_balance, "sorted_transaction": sorted_transaction, "money_added":money_added, "money_added_status":money_added_status})




# def MyAccountView(request):
#     user_obj = User.objects.filter(username__exact=request.user.username).first()
#     join_transaction_obj = JoiningTransactionDetail.objects.filter(transact_user__exact=request.user.username)
#     transaction_obj = TransactionDetail.objects.filter(transact_user__exact=request.user.username)#.order_by("-transaction_time")
#     # print(join_transaction_obj, transaction_obj)
#     sorted_transaction = sorted(chain(join_transaction_obj, transaction_obj), key=lambda obj: obj.transaction_time, reverse=True)
#     print(sorted_transaction)
#     money_added = False
#     money_added_status = False
#     return render(request, 'accounts/my_account.html', context={"user": user_obj, "total_balance": user_obj.profile.balance + user_obj.profile.bonus + user_obj.profile.widhdrawable_balance, "sorted_transaction": sorted_transaction, "monney_added":money_added, "money_added_status":money_added_status})
# @login_required
# def LogoutView(request):
#     logout(request)

# def RegisterView(request):

#     registered = False

#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = ProfileForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             registered = True

#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = ProfileForm()
#     return render(request, 'index.html',
#                           {'user_form': user_form,
#                            'profile_form': profile_form,
#                            'registered': registered})

# def RegisterView(request):

#     registered = False

#     if request.method == 'POST':

#         user_form = UserForm(data=request.POST)

#         if user_form.is_valid:

#             user = user_form.save()

#             user.set_password(user.password)

#             user.save()

#     else:
#         user_form = UserForm()

#     return render(request, 'accounts/registration.html', {'user_form': user_form, 'registered': registered})


# def LogInView(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 q = User.objects.get(pk=request.user.pk)
#                 q.balance = q.balance+10
#                 return HttpResponseRedirect(reverse('accounts:register'))
#             else:
#                 return HttpResponse("Your account is not active.")
#         else:
#             print("Someone tried to login and failed.")
#             print("They used username: {} and password: {}".format(username, password))
#             return HttpResponse("Invalid login details supplied.")

#     else:
#         return render(request, 'accounts/login.html', {})
# #