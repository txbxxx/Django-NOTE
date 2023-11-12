#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
-----------------------------------------------------------------
 
@文件 :urls.py
@说明 :
@时间 :2023/11/11 15:58:22
@作者 :TanChang
 
------------------------------------------------------------------
'''


from django.urls import path,include
"""导入视图模块"""
from . import views

"""应用程序的名字"""
app_name = 'accounts'
urlpatterns = [
    #添加默认登录界面的url
    path('',include('django.contrib.auth.urls')),
    #添加一个指向views.register视图函数的url模式
    path('register/',views.register,name='register')
]
