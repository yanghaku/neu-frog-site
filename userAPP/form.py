""" form.py文件

负责根据数据库的models模型,与html表单实现互换,互相声称

"""

# 这个要导入用户创建表单
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


# 注册用的表单
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # 指明对应的数据模型
        fields = ('username', 'first_name', 'email', 'image')
        # html对应的表单显示


# 修改信息用的自定义表单
class ProfilesForm(forms.Form):
    email = forms.EmailField(error_messages={'required': u'邮箱不合法'})
    first_name = forms.CharField(error_messages={'required': '名字不合法'})