"""
django.contrib.auth.urls 相当于已经写好的APP,然后导入进来就可以实现用户的密码修改重置等功能
但是注册功能还是要自己实现
其中包括:
include:
^users/login/$ [name='login']
^users/logout/$ [name='logout']
^users/password_change/$ [name='password_change']
^users/password_change/done/$ [name='password_change_done']
^users/password_reset/$ [name='password_reset']
^users/password_reset/done/$ [name='password_reset_done']
^users/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^users/reset/done/$ [name='password_reset_complete']
"""
from django.urls import re_path, include
from userAPP import views


# users 模块  默认前面加了 ^users/
urlpatterns = [
    # 个人信息等
    re_path(r'^profiles/', include([
        re_path(r'^$', views.profiles, name='profiles'),
        re_path(r'^(?P<pk>[0-9]+)/$', views.other_profiles, name='other_user'),
        re_path(r'^header$', views.header_change, name='header_change')])),
    # 登录注册的
    re_path(r'', include('django.contrib.auth.urls')),
    re_path(r'^register/', views.register, name='register'),
]
