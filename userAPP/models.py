from django.db import models
# 这是导入控制数据库的模型
from django.contrib.auth.models import AbstractUser
# 导入自带的用户抽象类
from django.urls import reverse
# 我们不用的有
# last_name 可选。少于30个字符
# user_permissions 与Permission 之间的多对多关系。


# 其中用到的属性有:用户信息有:
# 1. username(用户名)
# 2. password (密码)
# 3. email (邮箱)
# 4. is_superuser (管理员权限)
# 5. is_staff (是否可以访问admin站点)
# 6. is_active (帐号是否激活)
# 7.date_joined 账户创建的时间
# 8.last_login 用户最后一次登录的时间。
# 9.first_name (用这个来做nickname) 可选,少于等于30个字符
# 我们添加的有
# 1. image (头像)
# 2. contribute (贡献数)
#   还可以添加的
# 3.QQ号
# 4.学校专业
# 5.等

class User(AbstractUser):
    image = models.ImageField(default='../static/userAPP/img/head.jpg', upload_to='user_img')
    contribute = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        ordering = ['contribute']

    # 定义当点开这个的用户时的网址
    def get_absolute_url(self):
        return reverse('other_user', kwargs={'pk': self.pk})

# SEX_CHOICES = (
#        ('boy', u'男'),
#        ('girl', u'女'),
#        ('mi', u'保密'),
#    )
#    sex = models.CharField
