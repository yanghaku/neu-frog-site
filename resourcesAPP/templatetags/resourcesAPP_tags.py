from django import template
from ..models import ArticleCategory, Topic, BookCategory
from django.db.models import Count

register = template.Library()


@register.simple_tag
def get_category():
    # 使用annotate建立一个新的属性 article_num 文章数
    return ArticleCategory.objects.annotate(article_num=Count('article')).all()


@register.simple_tag
def get_all_topic():
    # 使用annotate建立一个新的属性 article_num 文章数
    return Topic.objects.annotate(article_num=Count('article')).all()


@register.simple_tag
def get_topic(article):
    return article.topic.all()


@register.simple_tag
def get_book_category():
    return BookCategory.objects.annotate(bookmark_num=Count('bookmark'))
