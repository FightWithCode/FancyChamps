"""FancyChamps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.sitemaps.views import sitemap
from cricket_center.sitemaps import StaticSitemap

handler404 = views.handler404
handler500 = views.handler500

sitemaps = {
      'static': StaticSitemap(),
    }

urlpatterns = [
    url(r'^verify_mobile_otp', views.MobileOTPVerifyView, name="MobileOTPVerify"),
    url(r'^verify_email_otp', views.EmailOTPVerifyView, name="EmailOTPVerify"),
    url(r'^check', views.CheckEnteredData, name="CheckEnteredData"),
    url(r'^$', views.IndexView, name="IndexView"),
    url(r'about_us', views.AboutUs, name='about_us'),
    url(r'^MasterAdminOfFancyChamps/', admin.site.urls),
    url(r'^cricket_center/', include('cricket_center.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^logout/', views.UserLogoutView, name="UserLogoutView"),
    url(r'^verify_mobile', views.MobileVerifyView, name="MobileVerifyView"),
    url(r'^verify_email', views.EmailVerifyView, name="EmailVerifyView"),
    url(r'verify_login_detail', views.VerifyLoginDetailView, name="VerifyLoginDetail"),
    url(r'privacy_policy', views.PrivacyPolicy, name="privacy_policy"),
    url(r'terms', views.Terms, name='terms'),
    url(r'legality', views.Legality, name='legality'),
    url(r'how_to_play', views.HowToPlay, name='how_to_play'),
    url(r'points_system', views.PointSystem, name='points_system'),
    url(r'faqs', views.Faqs, name='faqs'),
    url(r'contact_us/(?P<submitted>[0-1]+)', views.ContastUs, name='contact_us'),
    # url(r'^accounts/password_reset/$', auth_views.password_reset, {'template_name': 'registration/password_reset.html'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #url(r'^sitemap\.xml$', views.SiteMapView, name="SiteMap"),
]
