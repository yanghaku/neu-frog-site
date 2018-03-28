from django.db import models
from django.utils import timezone
from userAPP.models import User
# 为实现reply模块导入的包
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# 参考:http://www.jb51.net/article/70076.htm
# ugettext_lazy 在运行时才会翻译
from django.utils.translation import ugettext_lazy as _


# Create your models here.


# 每个评论基础的内容有:
# 1.创建的时间 created_time
# 2.创建的用户 user
# 3.内容的主体 text
# 4.支持 agree
# 5.反对 disagree
# 6.是否被删除 is_removed


# 第一,先创建父类抽象类,其中包括所以共有的属性
# (为了让每个类拥有各自的数据表,父类应该声明为抽象类,防止生成)
class Comment(models.Model):
    created_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=500, blank=False)
    agree = models.PositiveIntegerField(default=0)
    disagree = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_time']
        abstract = True

    def __str__(self):
        return self.text[:20]


# 第一张表:message留言,没有回复的对象,因此直接继承就行
class Message(Comment):
    pass

    class Meta(Comment.Meta):
        verbose_name_plural = _(r'留言')


# 第二张表,第一层回复,可以回复任意对象
class ReplyFather(Comment):
    # https://axiacore.com/blog/how-use-genericforeignkey-django/
    # GenericForeignkey可以关联任何的对象, 因此reply可以回复文章,评论,回复自己等等
    # 评论对象的类型
    content_type = models.ForeignKey(ContentType,
                                     verbose_name=_('content type'),
                                     related_name="content_type_set_for_%(class)s",
                                     on_delete=models.CASCADE)
    # 评论对象的ID
    object_pk = models.PositiveIntegerField(_('object ID'))
    # 根据前两个生成的保存为评论的对象
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_pk")
    is_removed = models.BooleanField(_('is removed'), default=False,
                                     help_text=_("Check this box if the comment is inappropriate. "
                                                 "A \"This comment has been removed\" message will "
                                                 "be displayed instead."))

    class Meta(Comment.Meta):
        ordering = ['-agree', '-created_time']
        verbose_name_plural = _(r'一级评论')


# 第三张表,第二层回复,不仅可以回复任何对象,还要有所属的一级评论才行
class ReplySon(Comment):
    # 增加了所属的评论这个属性
    father = models.ForeignKey(ReplyFather,
                               verbose_name='father',
                               related_name='son',
                               on_delete=models.CASCADE)
    # 其余和第二张一样,为了生成在两张表中,所以不能用继承关系
    content_type = models.ForeignKey(ContentType,
                                     verbose_name=_('content type'),
                                     related_name="content_type_set_for_%(class)s",
                                     on_delete=models.CASCADE)
    object_pk = models.PositiveIntegerField(_('object ID'))
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_pk")
    is_removed = models.BooleanField(_('is removed'), default=False,
                                     help_text=_("Check this box if the comment is inappropriate. "
                                                 "A \"This comment has been removed\" message will "
                                                 "be displayed instead."))

    class Meta(Comment.Meta):
        ordering = ['created_time']
        verbose_name_plural = _(r'二级评论')
