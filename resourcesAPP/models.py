"""
    资源数据库是主要的数据库,然后可以在这里面建立多个数据表,包括
    1.话题 Topic
    2.文章分类 ArticleCategory
    3.文章 Article
    4.书签所属的目录 BookCatgory
    5.标准书签  Bookmark
"""

from django.db import models
from django.utils import timezone
from userAPP import models as user_models
from django.urls import reverse
# Create your models here.


# 1.话题
class Topic(models.Model):
    name = models.CharField(max_length=20, unique=True)
    # 点击量
    click = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('article_list_by_topic', kwargs={'pk': self.pk})

    # 浏览量加一
    def increase_click(self):
        self.click += 1
        self.save(update_fields=['click'])

    def __str__(self):
        return self.name


# 2.文章目录
class ArticleCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_list_by_category', kwargs={'pk': self.pk})


# 3.文章
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    # 点击量
    click = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING)
    topic = models.ManyToManyField(Topic)
    user = models.ForeignKey(user_models.User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['click', '-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    # 增加阅读量
    def increase_click(self):
        self.click += 1
        self.save(update_fields=['click'])


# 4.书签所属目录
class BookCategory(models.Model):
    # 书签名
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_bookmark_list(self):
        return reverse('bookmark_list', kwargs={'pk': self.pk})


# 5.标准书签
class BookMark(models.Model):
    # 书签名
    title = models.CharField(max_length=50)
    # 链接
    url = models.URLField()
    # 描述 (这两个是为了搜索用的)
    description = models.CharField(max_length=200)
    # 创建日期
    created_time = models.DateField(default=timezone.now)
    # 点击量
    click = models.PositiveIntegerField(default=0)
    # 图标
    img = models.ImageField(upload_to='bookmark_icon', blank=True)

    # 外键,第一: 一对多联系到目录, 第二联系到上传人,第三就是所属的文章
    category = models.ForeignKey(BookCategory, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(user_models.User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)

    class Meta:
        # 元数据, 归定按点击量排序
        ordering = ['click', '-created_time']

    def __str__(self):
        return self.title
