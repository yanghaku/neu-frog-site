from django import template
from django.contrib.contenttypes.models import ContentType
from commentAPP.models import ReplyFather

register = template.Library()


# 获取留言的评论,按照时间顺序排序
@register.simple_tag
def get_comment_message(obj):
    return ReplyFather.objects.filter(content_type=ContentType.objects.get_for_model(obj), object_pk=obj.pk).order_by('created_time')


# 获得对象的全部一级评论
@register.simple_tag
def get_father_comment(obj):
    return ReplyFather.objects.filter(content_type=ContentType.objects.get_for_model(obj), object_pk=obj.pk)


# 获得一级评论之下的全部二级评论
@register.simple_tag
def get_son_comment(obj):
    return obj.son.all()
