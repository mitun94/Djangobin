from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name='profile'),
    url(r'^trending/$', views.trending_snippets, name='trending_snippets'),
    url(r'^trending/(?P<language_slug>[\w]+)/$', views.trending_snippets, name='trending_snippets'),
    url(r'^(?P<snippet_slug>[\d]+)/$', views.snippet_detail, name='snippet_detail'),
    url(r'^tag/(?P<tag>[\w-]+)/$', views.tag_list, name='tag_list'),
    url('^download/(?P<snippet_slug>[\d]+)/$', views.download_snippet, name='download_snippet'),
    url('^raw/(?P<snippet_slug>[\d]+)/$', views.raw_snippet, name='raw_snippet'),
    url('^contact/$', views.contact, name='contact'),
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'djangobin/login.html'},
        name='login'
        ),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'djangobin/logout.html'},
        name='logout'
        ),
    url(r'^userdetails/$', views.user_details, name='user_details'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}'
        r'-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    url('^settings/$', views.settings, name='settings'),
    url('^delete/(?P<snippet_slug>[\d]+)/$', views.delete_snippet, name='delete_snippet'),
    url('^search/$', views.search, name='search'),



]
