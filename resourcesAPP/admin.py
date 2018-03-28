from django.contrib import admin
from .models import Topic, ArticleCategory, Article, BookCategory, BookMark
# Register your models here.


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'click')


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'click', 'category', 'user')


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BookMarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'click', 'category', 'user')
    list_filter = ('category', 'user')


admin.site.register(Topic, TopicAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(BookMark, BookMarkAdmin)
