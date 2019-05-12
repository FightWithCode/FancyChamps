from django.conf.urls import url
from . import views

app_name = 'payments'

urlpatterns = [
    url(r'^payment/', views.PayTmPaymentView, name='payment'),
    url(r'^response/', views.PayTmResponseView, name='response'),
    url(r'^check/', views.CheckBalanceView, name='check'),
    url(r'^submit/', views.SubmitWidhdrawRequestView, name='submitwidhrew'),
]
