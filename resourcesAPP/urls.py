"""
资源索引模块的urls,url前边默认是resourceAPP
"""
from django.urls import include, re_path
from resourcesAPP import views

urlpatterns = [
    re_path(r'^paste/$', views.paste, name='paste'),
    re_path(r'^details/(?P<pk>[0-9]+)/$', views.details, name='details'),
    re_path(r'^list_cat/(?P<pk>[0-9]+)/$', views.list_cat, name='article_list_by_category'),
    re_path(r'^list_top/(?P<pk>[0-9]+)/$', views.list_top, name='article_list_by_topic'),
    re_path(r'^list_book_cat/', views.bookmark_category_list, name='bookmark_category_list'),
    re_path(r'^list_bookmark/(?P<pk>[0-9]+)/$', views.bookmark_list, name='bookmark_list'),
    re_path(r'category/', views.category_list, name='category_list'),
]
