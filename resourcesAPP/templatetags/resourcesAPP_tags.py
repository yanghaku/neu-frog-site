from django import template
from ..models import ArticleCategory, Topic, Article

register = template.Library()


@register.simple_tag
def get_category():
    return ArticleCategory.objects.all()


@register.simple_tag
def get_all_topic():
    return Topic.objects.all()


@register.simple_tag
def get_topic(article):
    return article.topic.all()
