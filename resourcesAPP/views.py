from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleCategory, Topic, BookCategory
from .form import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET
from markdown import markdown
# Create your views here.


def index(request):
    return render(request, 'index.html')


# 站内搜索的首页
def index_search(request):
    return render(request, 'search/search_index.html')


# 文章详情页
@require_GET
def details(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 用markdown渲染
    # article.text = markdown(article.text, extensions=[
    #    'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc',
    # ])
    article.text = markdown(article.text)
    # 文章浏览量加一
    article.increase_click()
    return render(request, 'resourcesAPP/details.html', context={'article': article})


# 发布文章的页面
@login_required(login_url='login')
@require_http_methods(['GET', 'POST'])
def paste(request):
    if request.method == 'POST':
        html = request.FILES.get('html', None)
        form = ArticleForm(request.POST)
        if form.is_valid():
            # commit=false是先不保存
            article = form.save(commit=False)
            article.user = request.user
            if html:
                article.text += html.read().decode('utf-8')
            article.save()
            # 保存后才能添加 多对多 外键
            for topic in form.cleaned_data['topic']:
                article.topic.add(topic)
            return redirect(article.get_absolute_url())
        # 表单无效就返回错误表单
        else:
            return render(request, 'resourcesAPP/paste.html', context={'form': form})
    # 如果不是post就返回空表单
    else:
        form = ArticleForm()
        return render(request, 'resourcesAPP/paste.html', context={'form': form})


# 从分类展示文章列表
@require_GET
def list_cat(request, pk):
    category = get_object_or_404(ArticleCategory, pk=pk)
    article_list = category.article_set.all()
    context = {'article_list': article_list, 'title': category.name}
    return render(request, 'resourcesAPP/article_list.html', context)


# 根据话题展示这个话题的文章列表
@require_GET
def list_top(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    # 浏览量加一
    topic.increase_click()
    article_list = topic.article_set.all()
    context = {'article_list': article_list, 'title': topic.name}
    return render(request, 'resourcesAPP/article_list.html', context)


# 文章的分类,话题的列表
@require_GET
def category_list(request):
    return render(request, 'resourcesAPP/category_list.html')


# 展示书签的分类列表
@require_GET
def bookmark_category_list(request):
    return render(request, 'resourcesAPP/bookmark_catgory.html')


# 展示某个分类下的所有书签
@require_GET
def bookmark_list(request, pk):
    mark = get_object_or_404(BookCategory, pk=pk)
    return render(request, 'resourcesAPP/bookmark_list.html', context={'bookmark_list': mark.bookmark_set.all()})
