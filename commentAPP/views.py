from django.shortcuts import render, HttpResponse, get_object_or_404
from resourcesAPP.models import Article
from commentAPP.models import Message, ReplySon, ReplyFather
from commentAPP.form import MessageForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.contenttypes.models import ContentType


# Create your views here.


# 关于我们 的视图
@require_GET
def about(request):
    return render(request, 'commentAPP/about_us.html')


# 网站指南的视图
@require_GET
def guide(request):
    return render(request, 'commentAPP/guide.html')


# 留言的视图, 需要登录
@login_required(login_url='login')
@require_http_methods(['GET', 'POST'])
def message_leave(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            message_list = Message.objects.all()
            context = {'message_list': message_list}
            return render(request, 'commentAPP/leave_message.html', context)
        else:
            # 返回错误表单
            message_list = Message.objects.all()
            context = {'message_list': message_list}
            return render(request, 'commentAPP/leave_message.html', context)
    else:
        message_list = Message.objects.all()
        context = {'message_list': message_list}
        return render(request, 'commentAPP/leave_message.html', context)


# 以下视图是创建评论的视图,因此命名的时候用  obj_to_obj 的规则命名


@login_required(login_url='login')
@require_POST
# 一级评论 评论文章
def father_to_article(request):
    text = request.POST.get('reply', '')
    pk = request.POST.get('pk', None)
    if text == "":
        return HttpResponse("Error", status=403)
    if pk:
        ReplyFather.objects.create(user=request.user,
                                   object_pk=pk,
                                   content_type=ContentType.objects.get_for_model(Article),
                                   text=text)
        return HttpResponse(request.user.image.url, status=200)
    else:
        return HttpResponse("Error", staus=403)


@require_POST
@login_required(login_url="login")
# 一级评论 回复留言
def father_to_message(request):
    text = request.POST.get("reply", '')
    pk = request.POST.get('pk', None)
    if text == "":
        return HttpResponse("评论不能为空!", status=403)
    if pk:
        ReplyFather.objects.create(user=request.user,
                                   text=text,
                                   content_type=ContentType.objects.get_for_model(Message),
                                   object_pk=pk)
        return HttpResponse(request.user.get_absolute_url())
    else:
        return HttpResponse("Error", status=403)


@login_required(login_url='login')
@require_POST
# 二级评论 回复一级评论
def son_to_father(request):
    text = request.POST.get('reply', '')
    pk = request.POST.get('pk', None)
    if text == '':
        return HttpResponse("评论不能为空!", status=403)
    if pk:
        ReplySon.objects.create(father_id=pk,
                                content_type=ContentType.objects.get_for_model(ReplyFather),
                                object_pk=pk,
                                user=request.user,
                                text=text)
        return HttpResponse("ok")
    else:
        return HttpResponse("Error", status=403)


@login_required(login_url="login")
@require_POST
# 二级评论 回复 二级评论
def son_to_son(request):
    text = request.POST.get('reply', '')
    pk = request.POST.get('pk', None)
    pkk = request.POST.get('pkk', None)
    if text == '':
        return HttpResponse(u"评论不能为空!", status=403)
    if pk and pkk:
        ReplySon.objects.create(father_id=pk,
                                content_type=ContentType.objects.get_for_model(ReplySon),
                                object_pk=pkk,
                                user=request.user,
                                text=text)
        return HttpResponse("ok")
    else:
        return HttpResponse("Error", status=403)


@login_required(login_url='login')
@require_GET
# 留言赞或者反对
def message_agree(request, pk, dis):
    mess = get_object_or_404(Message, pk=pk)
    if dis == '1':
        agree = mess.agree+1
        Message.objects.filter(pk=pk).update(agree=agree)
    elif dis == '0':
        disagree = mess.disagree+1
        Message.objects.filter(pk=pk).update(disagree=disagree)
    else:
        return HttpResponse("error", status=404)
    return HttpResponse("ok", status=200)


@login_required(login_url='login')
@require_GET
# 一级评论的赞成或反对
def reply_father_agree(request, pk, dis):
    reply = get_object_or_404(ReplyFather, pk=pk)
    if dis == '1':
        agree = reply.agree+1
        ReplyFather.objects.filter(pk=pk).update(agree=agree)
    elif dis == '0':
        disagree = reply.disagree+1
        ReplyFather.objects.filter(pk=pk).update(disagree=disagree)
    else:
        return HttpResponse("error", status=404)
    return HttpResponse("ok", status=200)


@login_required(login_url='login')
@require_GET
# 二级评论的赞成或反对
def reply_son_agree(request, pk, dis):
    reply = get_object_or_404(ReplySon, pk=pk)
    if dis == '1':
        agree = reply.agree+1
        ReplySon.objects.filter(pk=pk).update(agree=agree)
    elif dis == '0':
        disagree = reply.disagree+1
        ReplySon.objects.filter(pk=pk).update(disagree=disagree)
    else:
        return HttpResponse("error", status=404)
    return HttpResponse("ok", status=200)
