from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^profile/$', views.ProfileView, name="my_profile"),
    url(r'^remove/$', views.RemoveStorage, name="remove"),
    url(r'^my_account/$', views.MyAccountView, name="my_account"),
    url(r'^add_email/$', views.AddEmailView, name="add_email"),
    url(r'(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<uemailb64>[0-9A-Za-z_\-]+)$',
        views.activate, name='activate'),
    # url(r'^login/$', views.LogInView, name="login"),
]
