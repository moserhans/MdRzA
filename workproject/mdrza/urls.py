from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reg/$', views.register, name='registration'),
    url(r'^$', views.team_list, name='team_list'),
    url(r'^team/(?P<pk>\d+)/$', views.team_detail, name='team_detail'),
    url(r'^team/new/$', views.team_new, name='team_new'),
    url(r'^radler/new/$', views.radler_new, name='radler_new'),
    url(r'^radler/(?P<pk>\d+)/$', views.radler_detail, name='radler_detail'),
    url(r'^radler/(?P<pk>\d+)/edit/$', views.radler_edit, name='radler_edit'),
    url(r'^radler/$', views.radler_list, name='radler_list'),
    url(r'^woche/(?P<pk>\d+)/$', views.woche_detail, name='woche_detail'),
    url(r'^woche/(?P<pk>\d+)/edit/$', views.woche_edit, name='woche_edit'),
    url(r'^woche/new/$', views.woche_new, name='woche_new'),
]
