from django.contrib import admin
from .models import User
# Register your models here
# 在后台注册


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'contribute', 'is_staff', 'is_superuser')


admin.site.register(User, UserAdmin)