from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^profile/$', views.ProfileView, name="my_profile"),
    url(r'^my_account/$', views.MyAccountView, name="my_account"),
    # url(r'^login/$', views.LogInView, name="login"),
]
