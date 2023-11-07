#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
-----------------------------------------------------------------
 
@文件 :urls.py
@说明 :
@时间 :2023/11/06 20:30:00
@作者 :TanChang
 
------------------------------------------------------------------
'''



"""learning_logs应用程序的URL配置文件"""
from django.urls import path
"""调用视图文件"""
from . import views

"""配置app_name,用于在主体urls.py文件中与其他应用程序区分"""
app_name = "learning_logs"

urlpatterns = [
     #主页
    # """
    # 1. 第一个参数是 URL 路径：这是一个字符串，表示 URL 的路径部分。
    # 2. 第二个参数是视图函数：指定调用views.py中的哪个函数来处理；
    # 3. 可选的第三个参数是 URL 名称：这是一个字符串，用于为 URL 定义一个唯一的名称。可以在其他任何地方引用它
    # """
    path('',views.index,name='index'),
    path('topics/', views.topics,name='topics'),
    path('topics/<int:topic_id>',views.topic,name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>',views.new_entry,name='new_entry'),
    path('edit_entry/<int:entry_id>',views.edit_entry,name="edit_entry")
]
