from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import get_language
from django.urls import resolve, reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from . import Checksum
from .models import TransactionDetail, TransactionFailedDetail, PreTransData, WidhdrawRequest
import random, string, requests
from accounts.models import Profile
from decimal import Decimal
from django.shortcuts import get_object_or_404
from accounts.models import User, Profile
from cricket_center.models import JoiningTransactionDetail
from itertools import chain
from django.contrib.messages import get_messages
from django.http import JsonResponse
from django.db import IntegrityError


def PayTmPaymentView(request):
    print("Hello Worl From Paytm Payment")
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    get_lang = "/" + get_language() if get_language() else ''
    CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()
    print(settings.PAYTM_WEBSITE)
    bill_amount = request.GET['money_to_add']
    if bill_amount:
        data_dict = {
                    'MID':MERCHANT_ID,
                    'ORDER_ID':order_id,
                    'TXN_AMOUNT': bill_amount,
                    'CUST_ID':'harish@pickrr.com',
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':CALLBACK_URL,
                }
        param_dict = data_dict
        print(MERCHANT_KEY)
        print(data_dict)
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        pre_trans_obj = PreTransData(
            mid=param_dict['MID'],
            order_id=param_dict['ORDER_ID'],
            checksum=param_dict['CHECKSUMHASH'],
            transact_user=request.user.username,
            url_called=resolve(request.path_info).url_name
        )
        pre_trans_obj.save()
        return render(request,"payments/payment.html",{'paytmdict':param_dict})
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")


@csrf_exempt
def PayTmResponseView(request):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        transaction_obj = TransactionDetail(
                                            transaction_id=data_dict["TXNID"],
                                            transaction_status=data_dict["STATUS"],
                                            transaction_amt=Decimal(data_dict["TXNAMOUNT"].strip('"')),
                                            transact_user=request.user.username,
                                            captured=False,
                                            added_to_user=False,
                                  )
        try:
            pre_trans_obj = get_object_or_404(PreTransData, order_id=data_dict["ORDERID"])
        except:
            pass
        # url = 'https://securegw.paytm.in/order/status'
        # data = {
        #     "MID":"Iuyebg49353440880066",
        #     "ORDERID":pre_trans_obj.order_id,
        #     "CHECKSUMHASH":pre_trans_obj.checksum
        # }
        if (data_dict["STATUS"] == "TXN_SUCCESS") and (data_dict["RESPMSG"] == "Txn Success") and verify:
            try:
                transaction_obj.transaction_amt = Decimal(data_dict["TXNAMOUNT"].strip('"'))
                transaction_obj.captured = True
                transaction_obj.save()
                return HttpResponseRedirect("/accounts/my_account/")
            except IntegrityError:
                return HttpResponseRedirect("/accounts/my_account/")
        else:
            transaction_obj = TransactionFailedDetail(
                                            transaction_id=data_dict["TXNID"],
                                            transaction_status=data_dict["STATUS"],
                                            transaction_amt=Decimal(data_dict["TXNAMOUNT"].strip('"')),
                                            transact_user=request.user.username,
                                            captured=False,
                                  )
            transaction_obj.save()
    return HttpResponseRedirect("/accounts/my_account/")


# def PayTmResponseView(request):
#     if request.method == "POST":
#         MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
#         data_dict = {}
#         for key in request.POST:
#             data_dict[key] = request.POST[key]
#         verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])

#         transaction_obj = TransactionDetail(
#                                             transaction_id=data_dict["TXNID"],
#                                             transaction_status=data_dict["STATUS"],
#                                             transaction_amt=Decimal(data_dict["TXNAMOUNT"].strip('"')),
#                                             transact_user=request.user.username,
#                                             captured=False,
#                                   )
#         try:
#             pre_trans_obj = get_object_or_404(PreTransData, order_id=data_dict["ORDERID"])
#         except:
#             pass
#         url = 'https://securegw.paytm.in/order/status'
#         data = {
#             "MID":"Iuyebg49353440880066",
#             "ORDERID":pre_trans_obj.order_id,
#             "CHECKSUMHASH":pre_trans_obj.checksum
#         }
#         print(pre_trans_obj)
#         data = {
#           'JsonData': '{"MID":"Iuyebg49353440880066","ORDERID":pre_trans_obj.order_id,"CHECKSUMHASH":pre_trans_obj.checksum}'
#         }
#         headers = {'content-type': 'application/json'}
#         r = requests.post(url, data=data, headers=headers)
#         resp_data = r.json()
#         print(resp_data)
#         if (data_dict["STATUS"] == "TXN_SUCCESS") and (data_dict["RESPMSG"] == "Txn Success") and verify:
#             print("Hello Workld.................................1")
#             print("I got Something")
#             print(r)
#             transaction_obj.transaction_amt = Decimal(data_dict["TXNAMOUNT"].strip('"'))
#             transaction_obj.captured = True
#             user_obj = Profile.objects.get(user__username__exact=request.user.username)
#             print(type(Decimal(data_dict["TXNAMOUNT"].strip('"'))))
#             user_obj.balance = user_obj.balance + Decimal(data_dict["TXNAMOUNT"].strip('"'))
#             user_obj.save()
#             transaction_obj.save()
#             #current_url = resolve(request.path_info)
#             messages.add_message(request, messages.INFO, "Money added successfully!")
#             return HttpResponseRedirect("/accounts/my_account/")
#             # PaytmHistory.objects.create(user=request.user, **data_dict)
#         else:
#             print("Hello Workld.................................3")
#             transaction_obj = TransactionFailedDetail(
#                                             transaction_id=data_dict["TXNID"],
#                                             transaction_status=data_dict["STATUS"],
#                                             transaction_amt=Decimal(data_dict["TXNAMOUNT"].strip('"')),
#                                             transact_user=request.user.username,
#                                             captured=False,
#                                   )
#             transaction_obj.save()
#             print("Else")
#             messages.add_message(request, messages.INFO, "Failed")
#     return HttpResponse(status=200)

def CheckBalanceView(request):
    user_obj = User.objects.filter(username__exact=request.user.username).first()
    user_profile = Profile.objects.get(user__username__exact=request.user.username)
    data = {
        "widhdrawable_balance" : user_profile.widhdrawable_balance,
        "username" : request.user.username,
        "minimum" : 100,
        "max" : 10000,
        "is_email_confirmed" : user_profile.is_email_confirmed,
    }
    return JsonResponse(data)


def SubmitWidhdrawRequestView(request):
    cash = Decimal(request.GET.get('cash', None).strip('"'))
    # Decimal(data_dict["TXNAMOUNT"].strip('"')),
    user_obj = User.objects.filter(username__exact=request.user.username).first()
    user_profile = Profile.objects.get(user__username__exact=request.user.username)
    widhdraw_obj = WidhdrawRequest(
        user=request.user.username,
        widhdraw_amount=cash,
    )
    if(cash<=user_profile.widhdrawable_balance and cash>=100 and cash<10000):
        user_profile.widhdrawable_balance = user_profile.widhdrawable_balance - cash
        transaction_obj = TransactionDetail(
                                transaction_id = ''.join(random.SystemRandom().choice(string.ascii_lowercase  + string.digits) for _ in range(15)),
                                transaction_amt = Decimal(cash),
                                transaction_status = "pending",
                                transact_user = request.user.username,
                                transaction_message = "Withdrawn",
                                transaction_type = "deducted",
                                added_to_user= True,
                          )
        try:
            transaction_obj.save()
            user_profile.save()
            widhdraw_obj.save()
            data ={
                "request":True
            }
            print("HelloWOelr")
        except:
            data ={
                "request":False
            }
        
    else:
        data ={
            "request":False
        }
    # print(data)
    return JsonResponse(data)
