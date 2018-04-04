"""Frog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

这个是项目的主路由,每个匹配后的会分发给下面的相匹配的APP
然后转到每个APP的urls(二级路由)

"""
from django.contrib import admin
from django.urls import path, re_path, include
# 以下两行是为了增加匹配媒体文件
from django.conf.urls.static import static
from django.conf import settings
# 导入每个app的视图,都是直接包含的二级路由
from resourcesAPP import views as re_view


# url是顺序匹配的,像顺序查找,因此要把访问多的放在前面, 除了首页,都是载入的二级路由
urlpatterns = [
    # 主页的url
    path('', re_view.index, name='index'),
    # 搜索模块的url
    re_path(r'^search/', include('haystack.urls')),
    # user模块
    re_path(r'users/', include('userAPP.urls')),
    # 资源分享模块的url
    re_path(r'^resourcesAPP/', include('resourcesAPP.urls')),
    # 评论模块
    re_path(r'^comment/', include('commentAPP.urls')),
    # 管理员站点
    path('admin/', admin.site.urls),
    # 最后一行是访问静态媒体的url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
