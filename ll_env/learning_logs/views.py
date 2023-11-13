
from django.shortcuts import render,redirect
from .models import Topic,Entry
from .form import TopicForm,EntryForm
"""导入login_required"""
from django.contrib.auth.decorators import login_required
"""导入404模块"""
from django.http import Http404

# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request,'learning_logs/index.html')


"""在运行topics函数之前就运行login_required的代码，如果用户没有登录就重定向到登录页面"""
@login_required
def topics(request):
    """object.order_by是Django的一个数据库查询工具，它是依靠类模型中的rodering来排序"""
    # topics = Topic.objects.order_by('date_added')
    """在用户登录之后，request将有一个user属性集，其中包含了用户的信息，filter查询属于这个用户的主题并返回"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    """匹配模板中的 {{}} 变量"""
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html',context)


@login_required
def topic(request,topic_id):
    """显示单个主题及其所有条目,get()返回与给定的查找参数相匹配的对象"""
    topic = Topic.objects.get(id=topic_id)
    """判断是否为404"""
    check_topic_owner(request,topic)
    """ 查询与该主题相关的条目-表示降序排列 """
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    """将上下文提交到topic.html中"""
    return render(request,'learning_logs/topic.html',context)



@login_required
def new_topic(request):
    """添加新主题"""
    
    """判断是否是POST请求，Django中请求只有POST和GET两种，不是POST就是GET"""
    if request.method !='POST':
        """不是则创建一个Topic空表单"""
        form = TopicForm()
    
    else:
        """如果是就创建一个，request.POST创建的TopicForm中包含了用户提交的信息"""
        form = TopicForm(data=request.POST)
        """在提交数据到数据库中时，需要通过检查来确定条目是否是有效的，is_valid核实用户填写了所有必不可少的字段，或者超出了大小等检测"""
        if form.is_valid():
            """将表单中的数据存储到数据库中"""
            new_topic = form.save(commit=False)
            new_topic.owner  = request.user
            new_topic.save()
            """提交后重定向到topics界面，用户将在topics中查看到新建的数据"""
            return redirect('learning_logs:topics')
    """通过上下文提交给视图"""
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)
    
    

@login_required
def new_entry(request,topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request,topic)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            """
            commit=False意思为，Django创建一个新的条目对象，并赋予给new_entry,但是它不会保存到数据库中，因为此时
            还不知道是哪个主题的条目，在将topic赋予给new_entry.topic之后再保存
            """
            new_entry  = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            """需要调用topic，此函数包含topic_id需要赋予"""
            return redirect('learning_logs:topic',topic_id)
    context = {'topic':topic,"form":form}
    return render(request,'learning_logs/new_entry.html',context)




@login_required
def edit_entry(request,entry_id):
    """在Entry模型中查早entry_id"""
    entry = Entry.objects.get(id=entry_id)
    """匹配主题，在entry的条目中会显示是哪个主题的条目"""
    topic = entry.topic
    """判断访问者是否是本所属用户"""
    check_topic_owner(request,topic)
    
    """判断是否是POST请求，不是则依靠原有entry条目来创建一个表单"""
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        """如果是POST请求那么久是直接使用原有条目和request.POST中修改的数据进行修改"""
        form = EntryForm(instance=entry,data=request.POST)
        """检测文本是否达标\合理"""
        if form.is_valid:
            form.save()
            """修改完成后重定向到此主题界面"""
            return redirect('learning_logs:topic',topic.id)
    context = {"topic":topic,"form":form,'entry':entry}
    return render(request,'learning_logs/edit_entry.html',context) 


"""检测用户"""
def check_topic_owner(request,topic):
    if topic.owner != request.user:
        raise Http404