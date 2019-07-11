from django.conf.urls import url
from . import views
# from django.contrib.sitemaps.views import sitemap
# from cricket_center.sitemaps import StaticSitemap


# sitemaps = {
#       'static': StaticSitemap(),
#     }

app_name = 'cricket_center'


urlpatterns = [
    url(r'view_contest/(?P<match_slug>[\w]+)/(?P<contest_slug>[\w]+)', views.ContestsViews, name='view_contest'),
    url(r'capture_payment', views.CapturePayment, name='capture_payment'),
    url(r'^$', views.CricketCenterIndexView, name="cricket_center"),
    url(r'match/(?P<match_slug>[\w]+)', views.SingleMatchView, name='match'),
    url(r'rankings/(?P<match_slug>[\w]+)/(?P<contest_slug>[\w]+)', views.ContestsRankings, name='contest_ranking'),#//Resolved//Before match url is accessible
    url(r'create_team/(?P<match_slug>[\w]+)', views.CreateTeamView, name='create_team'),#//Resolved//After Match Starts then...
    url(r'(?P<match_slug>[\w]+)/(?P<contest_slug>[\w]+)/join_now_contest', views.ContestJoinNow, name='join_now_contest'),
    url(r'^pay_and_join/', views.PayAndJoin, name='pay_and_join'),
    url(r'^proceed_to_pay/', views.ProceedToPay, name='proceed_to_pay'),
    url(r'contest_joined/(?P<match_slug>[\w]+)', views.JoinedContests, name='joined_contests'),
    url(r'all_teams/(?P<match_slug>[\w]+)', views.MyTeams, name='my_teams'),
    url(r'edit/(?P<team>[\w]+)/(?P<match_slug>[\w]+)', views.TeamEdit, name='team_edit'),#//Resolved//After Match starts...
    url(r'get/(?P<team>[\w]+)/(?P<match_slug>[\w]+)', views.GetTeamInfo, name='get_team_info'),
    url(r'match_live/(?P<match_slug>[\w]+)', views.SingleMatchLiveView, name='match_live'),#//Resolved//Before Match starts
    url(r'ranking_team_preview/(?P<team_no>[\w]+)/(?P<team_name>[\w@%.%_%-]+)/(?P<match_slug>[\w]+)', views.RankingPreviewTeam, name='ranking_team_preview'),
    url(r'team_preview/(?P<team>[\w]+)/(?P<match_slug>[\w]+)', views.PreviewTeam, name='team_preview'),
    url(r'view_payout/(?P<contest_slug>[\w]+)', views.ViewPayout, name='view_payout'),
    url(r'match_his/(?P<match_slug>[\w]+)', views.SingleMatchHistoryView, name='match_his'),
    url(r'message', views.MessageCreateShow, name='message'),
    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
