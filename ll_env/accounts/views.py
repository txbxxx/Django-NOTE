from django.shortcuts import render,redirect
"""导入login模块"""
from django.contrib.auth import login
"""导入模块"""
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method != 'POST':
        """如果不是POST请求就创建一个空表单，不提供任何原格数据"""
        form = UserCreationForm()
    else:
        """如果时POST请求，就将填写的数据一起提交，并检测是否合法"""
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            """保存成功后自动登录用户"""
            login(request,new_user)
            return redirect('learning_logs:index')
    context = {'form':form}
    return  render(request,'registration/register.html',context)
