from django.contrib import admin
from commentAPP.models import Message, ReplyFather, ReplySon
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time', 'text', 'agree']
    list_filter = ['user', 'created_time']


class ReplyFatherAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time', 'text', 'agree', 'content_type']
    list_filter = ['user', 'created_time']


class ReplySonAdmin(admin.ModelAdmin):
    list_filter = ['user', 'created_time', 'father']
    list_display = ['user', 'created_time', 'text', 'agree', 'content_type']


admin.site.register(Message, MessageAdmin)
admin.site.register(ReplyFather, ReplyFatherAdmin)
admin.site.register(ReplySon, ReplySonAdmin)
