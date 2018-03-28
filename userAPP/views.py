from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .form import RegisterForm, ProfilesForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods
import os
# Create your views here.


# 注册用的视图函数
@require_http_methods(['GET', 'POST'])
def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # 如果有的话
            if redirect_to:
                return redirect(redirect_to)
            else:
                # 若没有,转到首页
                return redirect_to('/')
        # 如果表单内容不正确,返回原表单
        else:
            return render(request, 'registration/register.html', context={'form': form, 'next': redirect_to})
    # 如果是get,返回空表单
    else:
        form = RegisterForm()
        return render(request, 'registration/register.html', context={'form': form, 'next': redirect_to})


# 个人中心视图函数,需要登录才能进入修改
@login_required(login_url='login')
@require_http_methods(['GET', 'POST'])
def profiles(request):
    if request.method == 'POST':
        # 获取表单内容
        form = ProfilesForm(request.POST)
        if form.is_valid():
            # 把更改存到数据库中
            request.user.email = request.POST.get('email')
            request.user.first_name = request.POST.get('first_name')
            request.user.save()
            message = r'alert("保存成功!");'
            return render(request, 'registration/profile.html', context={'form': form, 'message': message})
        # 如果表单无效就返回原表单
        return render(request, 'registration/profile.html', context={'form': form})
    else:
        form = ProfilesForm()
        # 如果是get方法,就生成空表单,然后前端js自动填写就行
        context = {'form': form}
        # 信息还是传过去, 但只有表单里的才能更改
        return render(request, 'registration/profile.html', context)


# 修改头像的函数
@login_required(login_url='login')
@require_POST
# 只允许post方法而且要在登录状态
def header_change(request):
    # 检查文件是否上传
    try:
        img = request.FILES['image']
    except KeyError:
        return HttpResponse(u'文件不存在')
    # 如果文件存在,就检查文件的各种信息是否合法
    if img.size/1024/1024 > 30:
        return HttpResponse(u'文件太大')
    # 记录以前头像的位置
    oldurl = request.user.image.url
    try:  # 保存到数据库中
        request.user.image = img
        request.user.save()
    except:
        return HttpResponse('保存异常')
    # 保存后删除原来的 使用相对路径,当前路径就在工程下
    if os.path.exists(oldurl):
        os.remove(oldurl)
    return HttpResponse('修改成功!'+request.user.image.url)


# 访问其他用户的资料的视图,只允许get方法
@require_GET
def other_profiles(request, pk):
    # 由一个类的pk值查找该对象,没有就返回404
    obj = get_object_or_404(User, pk=pk)
    context = {'information': obj}
    return render(request, 'registration/other_profile.html', context=context)
