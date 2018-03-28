from django import forms
from commentAPP.models import Message, ReplyFather, ReplySon


# 留言的表单,只需要文本就行
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']

