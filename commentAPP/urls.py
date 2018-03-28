"""
二级路由,comment模块的url
"""
from django.urls import re_path, path
from commentAPP import views

urlpatterns = [
    path(r'about/', views.about, name='about'),
    path(r'guide/', views.guide, name='guide'),
    path(r'message/', views.message_leave, name='message'),
    path(r'fta', views.father_to_article),
    path(r'ftm', views.father_to_message),
    path(r'stf', views.son_to_father),
    path(r'sts', views.son_to_son),
]
