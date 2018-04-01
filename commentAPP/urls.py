"""
二级路由,comment模块的url
"""
from django.urls import re_path, path
from commentAPP import views

urlpatterns = [
    path(r'about/', views.about, name='about'),
    path(r'guide/', views.guide, name='guide'),
    path(r'message/', views.message_leave, name='message'),
    path(r'fta/', views.father_to_article),
    path(r'ftm/', views.father_to_message),
    path(r'stf/', views.son_to_father),
    path(r'sts/', views.son_to_son),
    re_path(r'message_agree/(?P<pk>[0-9]+)/(?P<dis>\d)/$', views.message_agree),
    re_path(r'father_agree/(?P<pk>[0-9]+)/(?P<dis>\d)/$', views.reply_father_agree),
    re_path(r'son_agree/(?P<pk>[0-9]+)/(?P<dis>\d)/$', views.reply_son_agree),
]
