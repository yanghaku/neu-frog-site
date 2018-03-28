from django import forms
from .models import Article


# 发布文章的表格
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'category', 'topic']
