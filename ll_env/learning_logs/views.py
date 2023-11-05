
from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """object.order_by是Django的一个数据库查询工具，它是依靠类模型中的rodering来排序"""
    topics = Topic.objects.order_by('date_added')
    """匹配模板中的 {{}} 变量"""
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    """显示单个主题及其所有条目,get()返回与给定的查找参数相匹配的对象"""
    topic = Topic.objects.get(id=topic_id)
    """ 查询与该主题相关的条目-表示降序排列 """
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    """将上下文提交到topic.html中"""
    return render(request,'learning_logs/topic.html',context)
    