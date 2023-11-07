#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
-----------------------------------------------------------------
 
@文件 :form.py
@说明 : Django Form表单
@时间 :2023/11/06 20:51:17
@作者 :TanChang
 
------------------------------------------------------------------
'''

"""导入form类"""
from django import forms
"""导入模型"""
from .models import Topic,Entry

"""创建一个TopicForm的类它继承于ModelForm"""
class TopicForm(forms.ModelForm):
    class Meta:
        """根据哪个模型来创建表单，表单中包含了哪些字段"""
        model = Topic
        """生成的 Form 类将按照 fields 属性中指定的顺序为每个指定的模型字段设置一个表单字段。这里只包含text字段"""
        fields = ['text']
        """对字段标签，这个表示不对text字段标签"""
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        """Textarea 是一个Django的部件也是HTML中的一个标签，他的意思是定义一个多行文本输出文件"""
        widgets = {'text':forms.Textarea(attrs={'cols':80})}