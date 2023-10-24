from django.contrib import admin

# Register your models here.

"""导入注册的模型Topic，.models表示在当前目录下查找"""
from .models import Topic

"""让Django通过管理网站来管理模型"""
admin.site.register(Topic)