

# 18 Django入门

## 18.1建立项目

### 18.1.1制定规范

:star: 我们要编写一个名为“学习笔记”的Web应用程序：

1. 让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加日志条目。
2. “学习笔记”的主页对这个网站进行描述，并邀请用户注册或登录
3. 用户登录后可用创建新主题、添加新条目以及阅读既有的条目。



### 18.1.2建立虚拟环境

​	我们可以建立一个虚拟的工作环境；`虚拟环境`就是可以理解为对`Python`环境封闭的一个文件夹，可以在其中安装一些其他的`Python`安装包，并且它会于其他`Python`包隔离，也可以理解为`Python环境`的一个**`副本`，如下图所示，可以看到虚拟环境中有python和pip的执行文件，也有lib库中的包，他们都是指向系统内部的Python环境的

![v2-ed22d7960927b35e815ab96d9dbd9e34_1440w](https://image-1305907375.cos.ap-chengdu.myqcloud.com/prometheus/v2-ed22d7960927b35e815ab96d9dbd9e34_1440w.png)

接下来我们创建一个Python虚拟环境，进入到需要创建环境的文件夹，如何CMD中打开，需要调用venv库：

```shell
PS D:\资料\example\example\python笔记\code\Web应用程序> python -m venv ll_env
PS D:\资料\example\example\python笔记\code\Web应用程序> dir


    目录: D:\资料\example\example\python笔记\code\Web应用程序


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2023/10/16     20:52                ll_env
-a----        2023/10/16     21:27           1195 README.md
```



### 18.1.3 激活/关闭虚拟环境

需要进入Scripts中执行activate,如果前面出现了虚拟环境名说明成功

```powershell
PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\Scripts> .\activate
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\Scripts>
```

关闭虚拟环境

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\Scripts> deactivate
PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\Scripts>
```



### 18.1.4安装Django

Django是一个开源的Web应用框架，是由Python完成，

1. Django提供了强大的ORM（对象关系映射），使得用户可以直接使用Python来操作数据库，无需编写SQL语句
2. 自动化的管理后台，Django提供一个自动生成的管理后台，可以方便地对数据库的内容进行增删改查操作，管理后台还可以自定义扩展
3. 表单处理，Django提供了表单处理的功能，可以方便地创建和验证表单。开发者可以使用它的表单累来生成HTML表单

下面来下载Django`pip install django`

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\Scripts> deactivate
PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\Scripts>
```



### 18.1.5 在Django中创建项目

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> .\django-admin.exe startproject learning_log .
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> ls


    目录: D:\资料\example\example\python笔记\code\Web应用程序\ll_env


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2023/10/16     20:52                Include
d-----        2023/10/16     22:16                learning_log
d-----        2023/10/16     20:52                Lib
d-----        2023/10/16     22:16                Scripts
-a----        2023/10/16     22:12         106438 django-admin.exe
-a----        2023/10/16     22:16            690 manage.py
-a----        2023/10/16     20:52             87 pyvenv.cfg

(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\learning_log> ls


    目录: D:\资料\example\example\python笔记\code\Web应用程序\ll_env\learning_log


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2023/10/16     22:16            417 asgi.py
-a----        2023/10/16     22:16           3362 settings.py
-a----        2023/10/16     22:16            790 urls.py
-a----        2023/10/16     22:16            417 wsgi.py
-a----        2023/10/16     22:16              0 __init__.py
```

```
manage.py是一个简单的程序，接受命令并将其交给Django的相关部分运行
settings.py 指定了Django如何与系统交互以及如何管理项目，在开发项目中，可以修改其中的设置，也可以添加设置
urls.py  它告诉Django，应该创建哪些页面来响应浏览器的请求
wsgi.py  它帮助Django提供它船舰的文件，它是Web server gateway interface 的缩写
asgi.py   application server gateway interface
```







### 18.1.6创建数据库

​	Django 支持许多不同的数据库服务器，官方支持 [PostgreSQL](https://www.postgresql.org/)、[MariaDB](https://mariadb.org/)、[MySQL](https://www.mysql.com/)、[Oracle](https://www.oracle.com/) 和 [SQLite](https://www.sqlite.org/)。使用manage.py migrate 来自动创建数据库表，而且需要确保Django又权限在你使用数据库中创建和修改表；

这是Django官方的原话：

> 如果你正在开发一个小项目或不打算在生产环境中部署的东西，SQLite 通常是最好的选择，因为它不需要运行一个单独的服务器。然而，SQLite 与其他数据库有许多不同之处，所以如果你正在开发一些实质性的东西，建议使用你计划在生产中使用的同一数据库进行开发

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

![image-20231016225022553](https://image-1305907375.cos.ap-chengdu.myqcloud.com/prometheus/image-20231016225022553.png)



### 18.1.7 启动

​	使用 `manage.py  runserver` 启动Django服务，可以使用浏览器访问 http://127.0.0.1:8000/，如果你不想使用默认端口就是 在命令后 写入的端口号；

​	这里是用纯Python写的轻量级网络服务器；

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 17, 2023 - 10:24:31
Django version 4.2.6, using settings 'learning_log.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

![image-20231017102631665](https://image-1305907375.cos.ap-chengdu.myqcloud.com/prometheus/image-20231017102631665.png)









## 18.2 创建应用程序-学习笔记

​	在Django中每个应用都是一个Python包，它们协同工作让项目成为一个整体；Django自带一个工具可以帮我们自动生成应用的基础目录

​	不要接受上一步启动的Django，重新打开一个终端，**并启动虚拟环境**，使用 `manage.py startapp`命令后面接app的名字

> 项目和应用有什么区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

```powershell
(learning_log-3) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py startapp learning_logs
```

生成了一个`learning_logs`的目录，查看目录下

![image-20231017112638145](https://image-1305907375.cos.ap-chengdu.myqcloud.com/prometheus/image-20231017112638145.png)

```javascript
models.py	定义要在应用程序中管理的数据
```





#### 18.2.1  定义模型

每个用户都会在学习笔记中创建很多主题：

1. 用户输入的每个条目都与特定主题相关联，这些条目将以文本的方式显示在下面代码用使用text导入
2. 需要创建每个条目的时间戳，以便告诉用户各个跳舞都是什么时候创建的。使用date_added

:star: 模型准确且唯一的描述了数据。它包含了存储数据的重要字段和行为。**而且一般来说每一个模型都映射了一张数据库表示。**

- 每个模型都是Python的类，这些类都继承于django.db.models.Model
- 模型类的每个属性都相当于一个数据库的字段
- 一旦创建数据模型后，Django会自动给予一套数据库抽象的`API`可以增删改查，在`18.4`会重点说明一下

接下来我们在models中输入，Topic表示一个模型，它拥有`text`和`date_added`两个字段,**字段名需要避免和模型API名字冲突**

```python
###models.py

"""导入了模块models让我们自己定义模型"""
from django.db import models

# Create your models here.

"""创建Topic类，它继承Model"""
class Topic(models.Model):
    """属性Text是由字符组成的数据，就是文本，需要存储少量的文本文件，名称、标题等，且需要高数Django在数据库中预留多少空间即max_length"""
    text = models.CharField(max_length=200)
    """记录日期和实践的数据，且当用户创建新主题时，会自动设置为当前的时间"""
    date_added = models.DateTimeField(auto_now_add=True)
    
    """当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据"""
    def __str__(self):
        """默认使用text格式来来显示有关主题的信息，返回存储在属性text中的字符串"""
        return f"{self.text} - {self.date_added}"
```

每个字段都需要指定一些特定的参数，`CharField`是一个字符串字段，它接受了`max_length`参数，但是还有一些其他参数如

:one: `null` 如果设置为`true`，该字段为空时，`Django`会将数据库中该字段设置为`Null`，默认为false
:two:`blank` 如果设置为`true`，该字段允许为空，`null`的区别在于blank涉及表单验证方面，`null`只是表面层
:three:`choices` 一系列的二元组，如果使用者提供了二元组，默认表单小部件时一个选择框，而不是标准文本字段
:four:`default` 该字段的默认值，可以是一个值或者是个可调用的对象，如果是个可调用的对象，每次实列化模型都会调用该对象
:five:`primary_key` 如果设置为`True`，该字段设置为该模型的主键，如果你在一个模型中，你没有对任何字段设置主键，`Django`会自动添加一个`IntegerField`字段，并设置为主键

:six:`unique` 如果设置为True,这字段的值必须在整个表中保持唯一

:star: 任何字段都会一个字段备注名，如果没有指定，Django会自动使用**字段的属性名来作为该参数**值，而且会把下划线转换为空隔，如果要设置可以参照以下代码

```python
#设置备注为 text express
text = models.CharField("text express"max_length=200)
```



#### 18.2.2	激活模型

​	在上面我们定义了一个model，如果要让Django将定义的应用程序包含到项目中，需要打开`settings.py` 

其中`INSTALLED_APPS`字段，用来告诉Django哪些应用程序被安装到了项目中，并将协同工作，将我们创建的learning_logs安装到项目中

```python
##settings.py


# Application definition

INSTALLED_APPS = [
    #我的应用程序
    'learning_logs',
    #默认应用程序
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

让Django修改数据库，使其能够存储与模型Topic相关的信息。

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
```

​	使用`makemigrations`让Django确定如何去修改数据库，使其可以存储与前面定义的新模型相关联的数据；以上输出表面Django创建的一个0001_initial.py的迁移文件，这个文件将在数据库中为模型Topic创建一个表

​	此外还可以使用`sqlmigrate`来查看使用的哪些`sql`命令来创建的表，它并不会创建表，只是输出命令到屏幕，可以看到整个表的详细，创建了一个表`learning_logs_topic`表示，id字段会被自动添加，但是也可以被改写，

```sqlite
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py sqlmigrate learning_logs 0001
BEGIN;
--
-- Create model Topic
--
CREATE TABLE "learning_logs_topic" 
(
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "text" varchar(200) NOT NULL,
    "date_added" datetime NOT NULL
);
COMMIT;
```

使用命令来查看数据库的表

```sqlite
sqlite> .tables
auth_group                  auth_user_user_permissions
auth_group_permissions      django_admin_log
auth_permission             django_content_type
auth_user                   django_migrations
auth_user_groups            django_session
```

> 这个 [`migrate`](https://docs.djangoproject.com/zh-hans/4.2/ref/django-admin/#django-admin-migrate) 命令查看 [`INSTALLED_APPS`](https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#std-setting-INSTALLED_APPS) 配置，并根据 `mysite/settings.py` 文件中的数据库配置和随应用提供的数据库迁移文件，创建任何必要的数据库表。你会看到它应用的每一个迁移都有一个消息。如果你有兴趣，运行你的数据库的命令行客户端，输入 `\dt` （PostgreSQL）， `S.HOW TABLES;` （MariaDB，MySQL）， `.tables` （SQLite）或 `SELECT TABLE_NAME FROM USER_TABLES;` （Oracle）来显示 Django 创建的表

接下来使用`migrate`来迁移数据库

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
```

迁移完成后再次查看数据的表

```sqlite
sqlite> .tables
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups            learning_logs_topic
auth_user_user_permissions
sqlite>
```





#### 18.2.3	Django管理网站

​	Django提供了一个管理网站`admin site` 让管理员可以轻松的处理模型，且只有管理员可以使用，普通用户不能使用

##### 1）创建管理员用户

​	Django允许创建具备所有权限的用户，即超级用户，使用`createsuperuser`来创建超级用户

```python
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py createsuperuser
Username (leave blank to use 'tanchang'): ll_admin ##输入超级用户
Email address:									   ##输入电子邮件
Password:										   ##输入密码，需要输入两次
Password (again):
Superuser created successfully.
```

现在我们可以登录到`admin`管理界面中去了进入http://127.0.0.1:8000/admin,但是并没有看见我们的learning_logs,需要注册模型

![image-20231023212100541](https://image-1305907375.cos.ap-chengdu.myqcloud.com/prometheus/image-20231023212100541.png)

##### 2)  向管理网站注册模型

​	Django自动在管理网站中添加了一些模型如`Users`和`Group`，但是我们自己创建的模型，必须手工进行注册

​	我们需要在创建的应用程序目录中修改`admin.py`文件

```python
from django.contrib import admin

# Register your models here.

"""导入注册的模型Topic，.models表示在当前目录下查找"""
from .models import Topic

"""让Django通过管理网站来管理模型"""
admin.site.register(Topic)
```

进入浏览器输入http://127.0.0.1:8000/admin查看可以查看到learning_logs了

![image-20231023212850166](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231023212850166.png)



##### 3)添加主题

创建`chess`国际象棋，`rock climbing`攀岩的主题

![image-20231023213027155](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231023213027155.png)

![image-20231023213142382](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231023213142382.png)





#### 18.2.4 定义模型Entry

​	:a: 刚刚创建了国际象棋和攀岩的主题，如果我们要记录这些的知识，那么用户就必须在学习笔记中添加条目。

​	:star2: 需要定义相关的模型。**每个条目都与特定主题相关联**，这种关系被称为**多对一关系**，即多个条目可关联到同一个主题

​	在`models.py`中添加如下几行

```python
##models.py


"""定义主题类"""
class Entry(models.Model):
    """
    创建外键，每创建一个主题时就会分配一个建。需要在两项数据建立连接的时候,Django就会使用键
    on_delete=models.CASCADE 表示删除主题的同时就会删除与之相关的所有条目，这被称为级联删除
    """
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    """用于管理模型额外的消息，"""
    class Meta:
        """拥有多个条目时就使用entries来表示，否者就会用entrys来表示"""
        verbose_name_plural = 'entries'
    
    def __str__(self):v
        """显示文本的前50个字符后续字符用......"""
        return f"{self.text[:50]}..."
    
```

`	models.ForeignKey`设置了一个多对一的关联关系，它和`Topic`模型关联,它的选项`on_delete`选择他的删除方式他的选项有

:one: `CASCADE`：级联删除
:two: `PROTECT`: 通过引发`ProtectedError`来防止删除被引用对象
:three: `RESTRICT`：通过引发`RestrictedError`来防止删除被引用的对象，但是如果引用对象也引用了一个在同一操作中被删除的不同对象，可以通过CASCADE关系来删除
:four: `SET_NULL` 设置只有当`ForeignKey`为空，null为True才可能被删除
:five: `SET_DEFAULT` 将`ForeignKey`设置默认值

详细信息请看：[¶ (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/models/fields/#foreignkey)

模型`meta`是用来保管主模型中的其他额外配置文件中，他还有其他一些可选的字段[¶ (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/models/options/#model-meta-options)



#### 18.2.5 迁移模型Entry

​	生成了一个`0001__entry.py`的文件，他会告诉Django该如何去修改这个数据库，使其可以存储Entry相关的信息

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python .\manage.py makemigrations learning_logs
Migrations for 'learning_logs':
  learning_logs\migrations\0002_entry.py
    - Create model Entry
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0002_entry... OK
```



#### 18.2.6 向网站注册Entry

​	注册到网站后，就可以打开`admin`管理平台来添加Text文档，可以用来记录`chess`和`rock climbing`的学习笔记，这里添加两个的学习笔记，在`entries`中添加，需要选择`Topic`选择后可以添加`Text`

```python
from django.contrib import admin

# Register your models here.

"""导入注册的模型Topic，.models表示在当前目录下查找"""
from .models import Topic
from .models import Entry


"""让Django通过管理网站来管理模型"""
admin.site.register(Topic)
admin.site.register(Entry)
```

![image-20231029202111852](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231029202111852.png)

添加，学习笔记

![image-20231029202450089](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231029202450089.png)

点击`SAVE`后可以看到保存后的界面，在界面中由于我们设置了`[:50]`所以界面就只显示了50个字符并且后面使用`.....`来省略

![image-20231029203338152](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231029203338152.png)

在次添加国际象棋和攀岩的笔记

![image-20231029203823787](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231029203823787.png)



#### 18.2.7 Django shell

​		`Django shell`是一个Python的交互解释器他可以使用`-i`来指定是`ipython`，`bpython`还是`python`来执行，可以使用`Shell`来进行测试和排除项目的故障，也可以使用`-c`来直接指定命令，下面是一个交互式`Shell`的会话

​		`Topic.objects.all()`获取模型Topic的所有实例，这将返回一个称为查询集（`queryest`）的列表

```django
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py shell
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: chess - 2023-10-23 13:30:29.738659+00:00>, <Topic: Rock Climbing - 2023-10-23 13:31:21.454303+00:00>]>
>>>
```

​	也可以像遍历列表一样遍历查询集，这里查询`topic`的`id`

```python
>>> topics =  Topic.objects.all()
>>> for topic in topics:
...     print(topic.id,topic)
...
1 chess - 2023-10-23 13:30:29.738659+00:00
2 Rock Climbing - 2023-10-23 13:31:21.454303+00:00
>>>
```

使用`Topic.objects.get()`来获取该对象并查看其属性

```python
>>> t = Topic.objects.get(id=1)
>>> t.text
'chess'
>>> t.date_added
datetime.datetime(2023, 10, 23, 13, 30, 29, 738659, tzinfo=datetime.timezone.utc)
```

之前在定义`entry`模型的时候将`topic`作为了`entry`的外键，将条目和主题关联起来了，在`shell`也可以查询，使用`模型名_set.all()`查询

```python
>>> t.entry_set.all()
<QuerySet [<Entry: 国奖象棋的第一个阶段是开局，大致是前10步左右。在开局阶段，最好做三件事情：将象和马调出来，努力控制...>, <Entry: 在国际象棋的开局阶段，将 象和马调出来横重要，这些棋子威力大，机动性强，在开局阶段扮演着重要角色...>]>
```

#### 练习

##### 18-1

```python
##修改

	def __str__(self):
        """显示文本的前50个字符后续字符用......"""
        # return f"{self.text[:50]}..."  原始
        """字符大于50就前50个字符和显示....号，小于则不会显示"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
```

##### 18-2

请自行查看

[执行查询 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/topics/db/queries/)



##### 18-3







## 18.3 创建页面：学习笔记主页

​	使用Django创建页面的过程分为三个阶段：

:one: 定义URL
:two: 编写试图
:three: 编写模板

​	在Django中，网页和其他内容都是从视图派生而来的。每一个**视图表现为一个`Python`函数**。`Django`会根据用户请求的`URL`来选择使用哪个**视图**；
​	`URL`模式描述了`URL`是如何设计的，让`Django`知道如何将浏览器请求与网站`URL`匹配，以确定返回哪个页面。
​	Django使用`URLconf`是为了将URL和视图关联起来	

#### 18.3.1  映射URL

​	为了给一个应用程序设计URL，你需要创建一个Python模块，通常被称为`URLconf`,这个模块是纯粹的Python代码，

​	打开`urls.py`文件，`urls.py`文件通常是写包含哪些应用程序的的**路由信息**，它定义了整个项目的路由，而不是单单一个应用程序的，它通常是包含一些全局的URL模式

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

​	导入了`admin`便于对管理网站的URL进行管理，在`urlpathtern`是定义`url`的变量的，通常写入的是含项目中的应用程序的`URLconf`的，不会直接在`urls.py`内写`Urlconf`的文件，因为这样会显得过于臃肿和不好维护，如果在`Urlconf`中的`urlpathern`中就是包含视图文件的

​	因此我们还需要写一个`Urlconf`来配置`learning_logs`应用层程序的单独`url`配置，在应用程序`learning_logs`中创建`urls.py`文件

```python
"""learning_logs应用程序的URL配置文件"""
from django.urls import path
"""调用视图文件"""
from . import views

"""配置app_name,用于在主体urls.py文件中与其他应用程序区分"""
app_name = "learning_logs"

urlpatterns = [
     #主页
    path('',views.index,name='index'),
]

```

path函数:
	:one:第一个参数是 URL 路径：这是一个字符串，表示 URL 的路径部分。
	:two:第二个参数是视图函数：指定调用`views.py`中的哪个函数来处理；
	:three:可选的第三个参数是 URL 名称：这是一个字符串，用于为 URL 定义一个唯一的名称。可以在其他任何地方引用它	

在主题`urls.py`文件中，写入包含`learning_logs`应用程序的`urlconf`，

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #使用include来包含learing_logs模块
    path('',include('learning_logs.urls')),
]
```



#### 18.3.2 编写视图

​	视图函数接受请求中的信息，准备好生成页面所需要的数据，再将这些数据发送给浏览器
​	`views.py`文件在使用 `manage.py startapp`就自动生成了，初始阶段只导入了`render()`函数
​	`render`函数是在Python代码中生成HTML响应，它将给定的模板和上下文字典组合，加以渲染返回一个`HttpResponse`,它需要以下参数：
​	:one: request: 用于生成此响应的请求对象
​	:two: template_name: 要使用的`html`文件
​	:three: context(可选): 字典文件，在之后的模板文件需要使用到
​	:four: status(可选)：响应的状态码默认200
​	:five: using:	用于加载模板的引擎

```python
from django.shortcuts import render

# Create your views here.

```

​	在文件中加入应用程序`learning_logs`的主页文件

```python
from django.shortcuts import render

# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request,'learning_logs/index.html')
```





#### 18.3.3 编写模板文件

​	模板定义的外观，需要使用到`Html`文件来编写
​	为了让Django可以成功读取到编写的`Html`文件，**我们需要在应用程序的文件夹中创建一个**`templates`**文件在此文件中在次创建一个以应用程序命名的文件夹**，在里面创建`html`文件编写，这样才可以很好的被Django自动识别

```html5
<!DOCTYPE html>
<html>
<body>
    <p>这是learning_log的learning_logs应用程序</p>
    <p>它是用于记录学习笔记的一个应用程序</p>
</body>
</html>
```

![image-20231104210021309](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231104210021309.png)

​	打开浏览器输入http://127.0.0.1:8000查看是

![image-20231104210149361](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231104210149361.png)





## 18.4 创建其他页面

我们需要创建两个显示数据的页面:
:one: 列出所有主题
:two: 显示所有主题的所有条目

且对于每个页面我们都将指定URL模型、编写一个视图函数和一个模板，在此之前需要创建一个父模板，项目中的其他模板都将继承它，模板继承允许使用者建立一个基本的”骨架“模板，它包含你的网站的所有常用院所，并定义了子模版可以覆盖的 `块(block)`

详细信息[模板 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/topics/templates/)
模板继承说明[Django 模板语言 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/templates/language/#template-inheritance)

##### 1）创建父模板

在刚刚创建`Django`的`index.html`目录下在创建一个`base,html`的父模板文件

```django
<P>
    <a href="{% url 'learning_logs:index' %}">learning log</a>
</p>
{% block content %}{% endblock content %}
```

​	Django有着自己的模板语言的标签，在HTML基础上，将所有的模板标签都定义为`{% %}`表示。而`{{}}`用于包含变量，变量可以在`render`中`context`替换

​	`	{% url %}`用来返回给定视图和可选参数的绝对路径引用，上面代码它会去匹配，`learning_logs/urls.py`，也就是应用程序中的`urlconf`，名为`index`的URL匹配模式，`index`就是在URL中设置的name，而`learning_logs`表示为一个命名空间，其命名空间设置就是使用的`app_name`，这里使用了a标签来获取链接到`html`

[内置模板标签和过滤器 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/templates/builtins/#ref-templates-builtins-tags)



​	:star: 其中block标签定义了块，子模版可以使用这些块，块名为`content`，并且填充，但是子模版不需要对副模版中的所有块进行填充，只需要填充需要的即可，所有父模板可以随意定义多个块来预留空间



##### 2)子模版

需要将之前编写的`html`文件修改为继承父模板的文件

```django
{% extends "learning_logs/base.html" %}

{% block content %}
<p>这是learning_log的learning_logs应用程序</p>
<p>它是用于记录学习笔记的一个应用程序</p>
{% endblock content %}
```

`extedns`标签用于让Django知道他继承了哪个父模板，可以使用`block`标签来对父模板的block来进行填充，指定填充`content`模板

接下来打开浏览器刷新

![image-20231104221312664](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231104221312664.png)







#### 18.4.2 显示所有主题的页面

接下来就要创建所有主题何显示特定的主题中条目的页面了，需要按照以上的方法高效的添加

##### 1）添加URL模式

在`learning_logs`项目目标下的`urls.py`下修改

```python
urlpatterns = [
     #主页
    # """
    # 1. 第一个参数是 URL 路径：这是一个字符串，表示 URL 的路径部分。
    # 2. 第二个参数是视图函数：指定调用views.py中的哪个函数来处理；
    # 3. 可选的第三个参数是 URL 名称：这是一个字符串，用于为 URL 定义一个唯一的名称。可以在其他任何地方引用它
    # """
    path('',views.index,name='index'),
    path('topics/', views.topics,name='topics'),
]
```

##### 2）添加视图	

需要创建一个`topics`函数来匹配`url`，此函数也需要获取到`topics`这个页面的的`html`文件来返回请求，在`learning__logs`应用程序添加`topics`的匹配视图`views.py`中添加如下代码

```python
from .models import Topic


def topics(request):
    """object.order_by是Django的一个数据库查询工具，它是依靠类模型中的rodering来排序"""
    topics = Topic.objects.order_by('date_added')
    """匹配模板中的 {{}} 变量"""
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html',context)
```

:star2: `obejct.order_by`是Django的一个数据库查询工具，Django有自己的数据库查询工具`QuerySet`它是依靠类模型中的meta类中的ordering来排序[¶ (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/models/options/#ordering),可以通过它来覆盖它，这里就是根据属性`date_added`来查看[¶ (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/models/querysets/#order-by)

​	之前提到模型相当于数据库中的一个字段，且模型提供了一条`API`供用户查询，**一张模型类代表一张数据表，一个模型实例代表数据库中的一行记录**
:star2: 要从数据库来检索对象，就需要通过类模型中的`Manager`类构建一个`QuerySet`,而且没个类模型都会默认有一个`manager`的类，它会讲值赋予给它模型中的`objects`属性，用户可以使用`objects`属性来调用默认的manager类，从而对模型类内的数据进行查询 详情请查看[管理器 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/topics/db/managers/#django.db.models.Manager)，`QuerySet`是一个可查询对象的集合，它表示数据库中的一组数据，它是由`Manager`类来返回的；
​	他们都可以用来查询，`Manager`是初始查询，`QuerySet`是在`Manager`查询的基础上进行进一步查询，列如**过滤、排序、删除**等操作    			    	  



##### 3）添加模板

编写`HTML`模板文件，显示所有主题的页面，上面视图文件使用了context来显示topic的数据`templates\learning_logs\topics.html`

```Django
{% extends "learning_logs/base.html" %}
{% block content %}
</p>Topics</p>
<ul>
    <!--类似于Python中的for语句，它会匹配在视图文件中的上下文-->
    {% for topic in topics  %}
        <li>{{topic}}</li>
    <!--如果列表中摸鱼topic就执行-->
    {% empty %}
        <li>No topics have been added yet.</li>
    {% endfor %}
</ul>
{% endblock content %}


```

接下来修改父模板，添加一个topics的入口链接

```python
<P>
    <a href="{% url 'learning_logs:index' %}">learning log</a>
    <a href="{% url 'learning_logs:topics' %}">Topics</a>
</p>
{% block content %}{% endblock content %}
```



在网页中查看这是点击了`Topics`的效果，返回了两个以及创建的Topic并且按照创建时间排序了，如果不想Topic名字后接时间信息，可以在`models.py`中修改`Topic`的 `__str__`

![image-20231105212324731](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231105212324731.png)

![image-20231105213024352](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231105213024352.png)

#### 18.4.3显示特定主题的页面

上面我们显示了所有主题的界面，那么接下来我们就需要写每个主题它的特定显示页面了

##### 1）修改Url模式

显示特定的主题页面需要在`urls.py`中修改Path中的路径

```python
        path('topics/<int:topic_id>',views.topic,name='topic')
```

`<int:topic_id>`表示在编写模板时需要引用这个参数为匹配为整形的topic_id，会调用视图函数来处理这个参数



##### 2）修改视图文件

获取指定的主题以及相关联的所有条目,这里除了`request`还有`topic_id`，因为这个函数需要接受URL的表达式的topic_id的值，并且存储在里面

```python
def topic(request,topic_id):
    """显示单个主题及其所有条目,get()返回与给定的查找参数相匹配的对象"""
    topic = Topic.objects.get(id=topic_id)
    """ -表示降序排列 """
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
```



##### 3）修改模板

新建一个`topic.html`模板 ,需要显示每个的页面和他们的条目信息

```Django
{% extends 'learning_logs/base.html' %}


{%block content %}
    <p>Topic: {{topic}} </p>
    <p>Entries</p>
    <ul>
    {% for entry in entries  %}
        <li>
            <p>{{entry.date_added|date:'M d,Y H:i'}}</p>
            <p>{{entry.text|linebreaks}}</p>
        </li>
    {% empty %}
        <li>There are no entries for this topic yet.</li>
    {% endfor %}
    </ul>
{% endblock %}
```

​	可以看到在模板中的`for`语句中，调用了视图中的`entries`，而`entries`又是依靠数据库中查询来调用的；其中`|`表示模板的过滤器，对模板的变量的值进行修改的函数，M表示月份`momth`，d表示第几天，Y表示`year`，H和i分别表示小时和分钟，条目的分隔符可以自定义，而`linebreaks`表示显示完整的词



我们可以查看数据库中表数据来直接查看，可以很详细的看到条目的`id`、`text`和`date_added`的数据

```sqlite
PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> sqlite3.exe .\db.sqlite3
sqlite> .header on 							###打开头显示
sqlite> .mode column						###调用模块
sqlite> SELECT * FROM learning_logs_entry;	##查询此数据表中的所有信息
id  text                                                          date_added                  topic_id
--  ------------------------------------------------------------  --------------------------  --------
1   国奖象棋的第一个阶段是开局，大致是前10步左右。在开局阶段，最好做三件事情：将象和马调出来，努力控制棋盘的中间区域，以及  2023-10-29 12:30:42.440112  1
    用车将王护住。
        当然，这些知识指导原则。学习说明情况吓遵守这些原则、什么情况下不用遵守很重要


2   在国际象棋的开局阶段，将象和马调出来横重要，这些棋子威力大，机动性强，在开局阶段扮演着重要角色               2023-10-29 12:35:48.971523  1

3   最重要的攀岩概念之一是尽可能让双脚承受体重。有人误以为攀岩者能依靠手臂的力量坚持一整天。实际上，有限的攀岩者都是经过专门  2023-10-29 12:38:13.364699  2
    的训练，能够尽可能让双脚承受体重。
```

也可以查看一下`Topic`中的信息

```
sqlite> SELECT * FROM learning_logs_topic;
id  text           date_added
--  -------------  --------------------------
1   chess          2023-10-23 13:30:29.738659
2   Rock Climbing  2023-10-23 13:31:21.454303
```

随后需要修改`topics.py`文件，将显示的Topic名添加链接指向视图中的`topic`函数来处理，并且传递`topic.id`参数，`topic.id`在for循环中获取，也就是说`topic.id`是在`topics`视图中获取到的并且传给`topic`的

```django
{% extends "learning_logs/base.html" %}
{% block content %}
</p>Topics</p>
<ul>
    <!--类似于Python中的for语句，它会匹配在视图文件中的上下文-->
    {% for topic in topics  %}
        <li><a href="{% url 'learning_logs:topic' topic.id%}">{{topic}}</a></li>
    <!--如果列表中摸鱼topic就执行-->
    {% empty %}
        <li>No topics have been added yet.</li>
    {% endfor %}
</ul>
{% endblock content %}
```

打开浏览器查看

![image-20231106104905070](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231106104905070.png)







# 19. 用户账户

​	web程序的核心是让任何用户都能够注册账户并能够使用它，在本章将要做到:

:one: 创建表单，让用户可以添加主题和条目

:two: 学习Django如何防范对基本表单的页面发起的常见攻击

:three: 实现一共用户身份验证系统，创建一共注册页面，提供用户创建账户，并且让有些页面只能供已经登录的用户访问

:four: 修改视图函数，使得用户只能看到自己的数据，且需要保证用户数据的安全





## 19.1 让用户输入数据



### 19.1.1 添加新的主题

需要创建一个可以让用户添加新主题。



#### 1）添加用于添加主题的表单

​	让用户输入并提交学习的页面都是表单，在`html`或者说在网页中，大多数情况是，你看到的都是开发者想要你看到的，从而没有用户的思想，而表单提供了用户自己提供思想的一个方法

​	除非你计划搭建的网站和应用只发布内容且不会接受访问者的输入，否则就需要理解和使用表单，且Django提供了一系列的工具和库来帮助创建者来接受用户的输入，然后处理以及响应这些输入

​	表单是`HTML`中的一个概念它使用`<form>`标签来构建，`Django`在表单中会设计处理三个不同的部分

- 准备并重组数据，以便下一步的渲染
- 为数据创建`HTML`表单
- 接受并处理客户端提交的表单数据

这些`DJango`都可以帮助使用者来完成这些工作

​	:star:**在`Django`中的表单系统中核心的组件就是`Form`类型，它与Django模型描述对象的逻辑结构、行为以及它呈现给我们的内容的形式的方式大致相同，它类似于模型类的字段映射到数据库字段的方式，表单类的字段会映射到HTML表单有`<input>`元素中。`ModelForm`通过`Form`映射模型类的字段到HTML表单的`<input>`元素，表单字段本身在`Django`中也是一个类，在浏览器中，表单字段以HTML控件（也叫表单元素）的形式展现，每个字段类型都有与之相匹配的[控件类](https://docs.djangoproject.com/zh-hans/4.2/ref/forms/widgets/)（用于自定义HTML输入字段的小部件）但必要时可以覆盖，这里的覆盖可能是覆盖HTML文件中原有的表单元素**

更加详细的介绍可以查看[¶ (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/topics/forms/#the-django-form-class)

​	在Django中，创建表单最简单的办法就是[`ModelForm`](https://docs.djangoproject.com/zh-hans/4.2/topics/forms/modelforms/#modelform)，它可以根据从一个Django模型中创建一个`Form`类，接下来创建一个`Form`类，需要创建一个`form.py`的文件，创建在和`models.py`同级的目录中

```python
"""导入form类"""
from django import forms
"""导入模型"""
from .models import Topic

"""创建一个TopicForm的类它继承于ModelForm"""
class TopicFrom(forms.ModelForm):
    class Meta:
        """根据哪个模型来创建表单，表单中包含了哪些字段"""
        model = Topic
        """生成的 Form 类将按照 fields 属性中指定的顺序为每个指定的模型字段设置一个表单字段。这里只包含text字段"""
        fields = ['text']
        """对字段标签，这个表示不对text字段标签"""
        labels = {'text':''}
```



#### 2）创建URL模式

```python
   path('new_topic/',views.new_topic,name='new_topic')
```





#### 3）创建视图文件

```python
from django.shortcuts import render,redirect
from .form import TopicFrom


........

def new_topic(request):
    """添加新主题"""
    
    """判断是否是POST请求，Django中请求只有POST和GET两种，不是POST就是GET"""
    if request.method !='POST':
        """不是则创建一个Topic空表单"""
        form = TopicFrom()
    
    else:
        """如果是就创建一个，request.POST创建的TopicForm中包含了用户提交的信息"""
        form = TopicFrom(data=request.POST)
        """在提交数据到数据库中时，需要通过检查来确定条目是否是有效的，is_valid核实用户填写了所有必不可少的字段，或者超出了大小等检测"""
        if form.is_valid():
            """将表单中的数据存储到数据库中"""
            form.save()
            """提交后重定向到topics界面，用户将在topics中查看到新建的数据主题"""
            return redirect('learning_logs:topics')
    """通过上下文提交给视图"""
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)
```

​	:one:关于`Post`和`GET`请求，在处理表单的时候就只会用到GET和`POST`两种`HTTP`方法，它们两个通常用于不同的目的，也就是可以理解为**任何可能用于更改系统状态的请求应该使用POST，比如修改数据库，添加数据库，而GET应该只用于不会影响系统状态的请求**，详细主要区别可以看[¶ `(djangoGet和POST)`](https://docs.djangoproject.com/zh-hans/4.2/topics/forms/#get-and-post) 

​	:two: 导入了[`redirect`](https://docs.djangoproject.com/zh-hans/4.2/topics/http/shortcuts/#render)函数，用户使用这个函数可以重定向到某个页面



#### 4）创建模板文件

​	按照上一个步骤需要创建一个`new_topic.html`，用于显示刚刚创建的表单:

```django
{% extends "learning_logs/base.html" %}

{% block content %}
    <p>Add a new topic:</p>
    <form action = "{% url 'learning_logs:new_topic' %}" method="post">
        {% csrf_token %}
        {{form.as_p}}
        <button name="submit">Add Topic</button>
    </form>

{% endblock  %}
```

​	同样的它也继承了`base.html`，在`<form>`标签定义了一个表单，它将创建好的订单通过`button`的`submit`发送给action中的链接，这里也就是发送给`new_topic`这个视图中去处理，并且是通过`post`请求发送的

​	模板标签[`{% csrf_token %}`](https://docs.djangoproject.com/zh-hans/4.2/ref/templates/builtins/#csrf-token)用于来防止攻击者利用表单来获得对服务器未经授权的访问也就是夸站请求伪造，它是一个内置标签

​	`{{form.as_p}}`变量在视图`new_topic`中传入，`as_p`也是一个内置的过滤器它的作用是自动创建显示表单所需要的全部字段，详情可以查看[as_q](https://docs.djangoproject.com/zh-hans/4.2/ref/forms/api/#as-p)



​	接下下来用户该如何进入创建主题的页面呢？用户在`topics`页面中查看，那我们可以直接在Topic页面中引用修改`topic.html`

```django
......
    </ul>
    <a href = "{% url 'learning_logs:new_topic' %}">Add a new topic</a>
```

​	将链接指向`new_topic`视图，它会调用new_topic.html来执行

![image-20231107201851739](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231107201851739.png)

![image-20231107201900863](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231107201900863.png)

### 19.1.2  添加新的条目

#### 1）添加表单

```PYTHON
from .models import Topic,Entry

class EntryForm(forms.ModelForm):
    class mate:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        """Textarea 是一个Django的部件也是HTML中的一个标签，他的意思是定义一个多行文本输出文件"""
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
```

​	`Textarea`他的意思是定义一个多行文本输出文件，它会数据渲染成`<textare></textare>`，

这里它将文本框提高到了80列而不是默认的40列



#### 2) 添加URL模式

```python
    path('new_entry/<int:topic_id>',views.new_entry,name='new_entry')
```

这里需要添加`topic_id`，因为需要知道添加条目是添加到哪个主题





#### 3）添加视图

创建`new_entry()`视图函数,再`views.py`中

```PYTHON
def new_entry(request,topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)
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
```



#### 4）创建模板

先创建当前需要实现的目标文件`new_entry.html`文件和`new_topic`类似

```django
{% extends "learning_logs/base.html" %}

{% block content %}
<p><a href = "{% url 'learning_logs:topic' topic.id%}">{{topic}}</a></p>
<p>Add new entry</p>
<form action= "{% url 'learning_logs:new_entry' topic.id %}" method='post' >
    {% csrf_token %}
    {{form.as_p}}
    <button name='submit'>Add entry</button>
</form>
{% endblock content %}
```



我们需要进入到单个主题页面中引用，再`topic.html`中添加

```django
{%block content %}
    <p>Topic: {{topic}} </p>
    <p>Entries:</p>
    <p>
        <a href = "{% url 'learning_logs:new_entry' topic.id %}">Add new entry</a>
    </p>
    <ul>
```

![image-20231107212856205](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231107212856205.png)

![image-20231107212911564](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231107212911564.png)

:star: 可能会好奇`topic.id`它的数据从何而来，其实他是层层嵌套而来的





### 19.1.3编辑条目



#### 1）添加URL模式

添加`url`模式，这里添加了一个`entry_id`，和条目的`id`对应

```python
    path('edit_entry/<int:entry_id>',views.edit_entry,name="edit_entry")
```





#### 2）添加视图

在视图中天机一个`edit_entry`函数用于处理`URL`模式请求，这里传入了参数`entry_id`，并且导入了`Entry`模型和`EntryForm`表单

```python
def edit_entry(request,entry_id):
    """在Entry模型中查早entry_id"""
    entry = Entry.objects.get(id=entry_id)
    """匹配主题，在entry的条目中会显示是哪个主题的条目"""
    topic = entry.topic
    
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
            redirect('learning_logs:topic',topic.id)
    context = {"topic":topic,"form":form,'entry':entry}
    return render(request,'learning_logs/edit_entry.html',context) 
```



#### 3）添加模板

```django
{% extends "learning_logs/base.html" %}

{% block content %}
<p>{{entry}}</p>
<form action = "{% url 'learning_logs:edit_entry' entry.id %}" method='post'>
    {% csrf_token %}
    {{form.as_p}}
    <button name='submit'>Edit entry</button>
</form>
{% endblock content %}
```



#### 4）在主题模板中引入修改链接

需要在主题模板中引入修改条目的链接，不然用户只能通过输入条目id来进行编辑

```django
    {% for entry in entries  %}
        <li>
            <p>{{entry.date_added|date:'M d,Y H:i'}}</p>
            <p>{{entry.text|linebreaks}}</p>
            <p><a href= "{% url 'learning_logs:edit_entry' entry.id %}">Edit entry</a></p>
        </li>
    {% empty %}
        <li>There are no entries for this topic yet.</li>
    {% endfor %}
    </ul>
{% endblock %}
```

这下在条目内容后面就会显示一个主题的链接



在浏览器中查看

![image-20231111151326230](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231111151326230.png)

![image-20231111151342156](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231111151342156.png)



## 19.2 创建用户账户

需要创建一个用户注册和身份验证的系统，让用户能够注册账户，进而登录和注销。为此我们需要：

:one: 创建一个新的应用程序，包含处理用户账户相关的所有功能

:two: 使用Django自带的用户身份验证系统来完成工作

:three: 将每个主题都归于特定用户



### 19.2.1 创建应用程序users

需要使用`startapp`命令来创建一个`accounts`的应用程序

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py startapp accounts
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> ls


    目录: D:\资料\example\example\python笔记\code\Web应用程序\ll_env


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2023/10/29     21:29                18-4
d-----        2023/10/16     20:52                Include
d-----        2023/10/16     22:45                learning_log
d-----         2023/11/6     20:51                learning_logs
d-----        2023/10/16     20:52                Lib
d-----        2023/10/16     22:16                Scripts
d-----        2023/11/11     15:31                accounts
-a----        2023/11/11     15:25         143360 db.sqlite3
-a----        2023/10/16     22:12         106438 django-admin.exe
-a----        2023/10/16     22:16            690 manage.py
-a----        2023/10/16     20:52             87 pyvenv.cfg






(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> cd .\accounts\
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\accounts> ls


    目录: D:\资料\example\example\python笔记\code\Web应用程序\ll_env\accounts


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2023/11/11     15:31                migrations
-a----        2023/11/11     15:31             66 admin.py
-a----        2023/11/11     15:31            148 apps.py
-a----        2023/11/11     15:31             60 models.py
-a----        2023/11/11     15:31             63 tests.py
-a----        2023/11/11     15:31             66 views.py
-a----        2023/11/11     15:31              0 __init__.py

```





### 19.2.2 将users加入到settings.py中

```
INSTALLED_APPS = [
    #我的应用程序
    'learning_logs',
    'accounts',
```



### 19.2.3 创建包含users的Url模式

项目`learning_log`中的`urls.py`中添加

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    # """匹配users打头的"""
    path('accounts/',include('accounts.urls')),
    #使用include来包含learing_logs模块
    path('',include('learning_logs.urls')),
]

```



### 19.2.4 登录界面

Django提供了一个默认的登录视图`login`，在`users`应用程序中添加一个`urls.py`文件，并添加默认登录界面的`path`，

```python
from django.urls import path,include

"""应用程序的名字"""
app_name = 'accounts'
urlpatterns = [
    #添加默认登录界面的url
    path('',include('django.contrib.auth.urls')),
]
```

[django.contrib.auth](https://docs.djangoproject.com/zh-hans/4.2/ref/contrib/auth/#django-contrib-auth)是Django默认提供了一个登录认证的应用程序，它在项目的`settings.py`包含的应用程序内可以看见，它匹配`/users/login`,从项目中匹配`users`然后从`users`应用程序中匹配`urls.py`到匹配到`login`就会发给Django默认的视图`login`

[django.contrib.aut.url](https://docs.djangoproject.com/zh-hans/4.2/topics/auth/default/#module-django.contrib.auth.views)

#### 1）编写`login.html`

Django虽然提供了一个默认的`login`应用程序，但是我们还是需要在`learning_logs`应用程序中编写`html`模板来调用这个视图和应用，使用`django.contrib.auth.url`视图默认会从`registration`目录中查找模板,**这里需要在项目目录中创建**，我在应用程序目录创建会一直报错

```django
{% extends "learning_logs/base.html" %}

{% block content %}
    <!--
        form.errors中包含了表单中的所有错误的字典对象，当表单验证失败，就会将错误信息存储在form.errors中
        这个if判断的时候的时候如果form.errors不为空，即存在错误,判断久为真，这里是判断用户名和密码是否和数据库中匹配
    -->
    {% if  form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    {% endif %}
    <!--创建表单，提交到login视图中-->
    <form method='post' action = "{% url 'accounts:login' %}">
        {% csrf_token %}
        {{form.as_p}}

        <button name="submit">log in</button>
    </form>
{% endblock content %}
```

在登录后`Django`需要知道要重定向哪个界面，可以在项目配置文件的`settings.py`中添加以下配置文件来使得重定向到主页

```python
###我的设置
LOGIN_REDIRECT_URL = 'learning_logs:index'
```



#### 2）链接到登录页面

需要在`base`模板中在应用`login`，让所有的页面都包含它，如果用户登录则不会显示，那么就需要使用到`if`语句当用户登录后会显示其他语句

```django
<p>
    <a href="{% url 'learning_logs:index' %}">learning log</a>
    <a href="{% url 'learning_logs:topics' %}">Topics</a>
    {% if user.is_authenticated %}
        Hello,{{user.username}}.
    {% else %}
        <a herf="{% url 'accounts:login' %}">log in</a>
    {% endif %}
</p>

{% block content %}{% endblock content %}
```

`is.authenticated`可以判断用户是否登录具体请查看[¶ (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/topics/auth/default/#authentication-in-web-requests)和[¶ (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated)



#### 3）使用登录界面

![image-20231112195725876](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231112195725876.png)

![image-20231112203820106](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231112203820106.png)



### 19.2.5 注销

​	现在只有登录界面，还需要添加一个用户注销按钮，注销请求必须以POST请求的方式提交，而且之前创建的accounts也自带logout只需要引用表单即可



#### 1）在base模板中引用logout

这里使用了`hr`标签来显示一个分割线，然后调用了选择提交链接为`account:logout`

```django

{% block content %}{% endblock content %}

{% if user.is_authenticated %}
    <hr/>
    <form method='post' action="{% url 'accounts:logout' %}">
        {% csrf_token %}
        <button name='submit'>log out</button>
    </form>
{% endif %}
```



#### 2) 设置settings.py

添加`logout`重定向链接

```python
###我的设置
LOGIN_REDIRECT_URL = 'learning_logs:index'
LOGOUT_REDIRECT_URL = 'learning_logs:index'
```



![image-20231112210231662](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231112210231662.png)





### 19.2.6 注册页面

​	创建一个让新用户可以注册的页面。会使用到Django提供的表单`UserCreationForm`,但是需要编写自己的视图函数和模板



##### 1）注册页面的URL模式

在应用程序`accounts`中的`urls.py`文件内添加

```python
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
```



##### 2）添加视图函数register

在`accounts`应用程序中的`views.py`添加

```python
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
```





##### 3）编写注册模板

在`account`项目中，和之前`login`创建在同一个路径，`register.html`

```django
{% extends "learning_logs/base.html" %}

{% block content %}
    <form method = 'post' action = "{% url 'accounts:register' %}">
        {% csrf_token %}
        {{form.as_div}}
        <button name="submit">register</button>
    </form>
{% endblock content %}
```



##### 4) 在主模板中链接

```django
<p>
    <a href="{% url 'learning_logs:index' %}">learning log</a>
    <a href="{% url 'learning_logs:topics' %}">Topics</a>
    {% if user.is_authenticated %}
        Hello,{{user.username}}.
    {% else %}
        <a href="{% url 'accounts:login' %}">log in</a>
    <!--添加-->
        <a href="{% url 'accounts:register' %}">register</a>
    {% endif %}
```



![image-20231112213523849](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231112213523849.png)

![image-20231112213538778](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231112213538778.png)





### 19.3 让用户拥有自己的数据

​	用户有了，但是用户的数据并没有做固定和保护，无论是否登录都可以看到主题和条目，可以让每个用户自己创建属于自己的主题和条目；然后限制用户的访问，让他们只能访问自己的页面；



#### 19.3.1 使用@login_required 限制访问

Django提供了装饰器`@login_required`,可以使用它来限制页面的访问，它只允许已经登录的用户来访问某个页面



##### 1）限制对页面`topics`的访问

​	每个主题都归属于特定的用户，首先先限制只允许登录的用户来访问每个`Topics`，在`learning_logs/views.py`中的`Topics`函数之前添加装饰器

```python
"""导入login_required"""
from django.contrib.auth.decorators import login_required

"""在运行topics函数之前就运行login_required的代码，如果用户没有登录就重定向到登录页面"""
@login_required
def topics(request):
    """object.order_by是Django的一个数据库查询工具，它是依靠类模型中的rodering来排序"""
    topics = Topic.objects.order_by('date_added')
    """匹配模板中的 {{}} 变量"""
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html',context)
```

修改项目文件`settings.py`让Django知道重定向到哪，如果没登录查看`Topic`就会重定向到登录界面

```python
###我的设置
LOGIN_REDIRECT_URL = 'learning_logs:index'
LOGOUT_REDIRECT_URL = 'learning_logs:index'
LOGIN_URL = 'accounts:login'
```

![image-20231112221428299](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231112221428299.png)

现在你点`Topics`就会需要登录来查看了



##### 2）全面限制对项目学习笔记的访问

​	此刻只是限制了`Topics`页面，没有限制`new_topic`、`entry_topic`等页面，用户还是可以通过`url`的方式进入，需要将除了`index`页面之外的页面都使用装饰器来限制它们的访问，需要编辑`learning_logs`应用程序中的`views.py`文件

```python
from django.shortcuts import render,redirect
from .models import Topic,Entry
from .form import TopicForm,EntryForm
"""导入login_required"""
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request,'learning_logs/index.html')


"""在运行topics函数之前就运行login_required的代码，如果用户没有登录就重定向到登录页面"""
@login_required
def topics(request):
    """object.order_by是Django的一个数据库查询工具，它是依靠类模型中的rodering来排序"""
    topics = Topic.objects.order_by('date_added')
    """匹配模板中的 {{}} 变量"""
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html',context)


@login_required
def topic(request,topic_id):
    """显示单个主题及其所有条目,get()返回与给定的查找参数相匹配的对象"""
    topic = Topic.objects.get(id=topic_id)
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
            form.save()
            """提交后重定向到topics界面，用户将在topics中查看到新建的数据"""
            return redirect('learning_logs:topics')
    """通过上下文提交给视图"""
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)
    
    

@login_required
def new_entry(request,topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)
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
```

添加完成保存后，再次使用链接进入如果未登录就会重定向到登录界面





#### 19.3.2 将数据关联到用户

​	之后需要将每个条目和主题都关联到不同的用户中，后来创建条目和主题都会和用户进行绑定，只有用户可以查看；这里我们需要在`Topic`中模型添加一个外键关联到用户中去，应为条数是属于主题的，修改了主题的拥有者，就相当于也修改了条目的拥有者



##### 1）修改模型`Topic`

```python
from django.db import models
"""导入User模型"""
from django.contrib.auth.models import User

# Create your models here.
"""定义主题模型"""
class Topic(models.Model):
	......
    """添加外键使Topic关联到每个用户中去"""
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        # return f"{self.text} - {self.date_added}"
        return f"{self.text}"

```





##### 2）确定当前有哪些用户

​	虽然我们修改了模型文件，添加了`owner`属性，然而现在数据库内并没有这个字段，所以现在就需要进行一个数据库迁移，确保之前创建的也有这个条目，我们需要确认当前用户有多少个，然后迁移数据库将主题的信息更改

```sqlite
##确认用户个数的方式有两种
1.
> sqlite3.exe .\db.sqlite3
sqlite> .headers on
sqlite> .mode colum
sqlite> select * from auth_user;
id  password                                                      last_login                  is_superuser  username  last_name  email  is_staff  is_active  date_joined                 first_name
--  ------------------------------------------------------------  --------------------------  ------------  --------  ---------  -----  --------  ---------  --------------------------  ----------
1   pbkdf2_sha256$600000$fR87Q0su3XhQ1z3DeJngUd$TGus41qpuGCs1OeL  2023-11-12 13:02:15.715479  1             ll_admin                    1         1
 2023-10-23 08:02:06.425097
    EpbcZGbcl757h/K5rcwzVO05q4Q=


2   pbkdf2_sha256$600000$vCt6mIL1TbLV15eQpbjwjg$Iv6lWYozqez+hCOr  2023-11-12 13:40:14.988336  0             cat                         0         1
 2023-11-12 13:40:14.766285
    2tJEvKawyXqe1dVIcTySmLNb4vs=

sqlite>



2.
> python .\manage.py shell
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: ll_admin>, <User: cat>]>
>>> for user in User.objects.all():
...     print(user.username,user.id)
...
ll_admin 1
cat 2
```



##### 3）迁移数据库

我们知道用户的`id`之后就可以迁移数据库了，在迁移的时候Python会询问添加哪个`User`作为`owner`，这里我选择将我的一号用户，也就是超级用户光联所有的主题

```python
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python .\manage.py makemigrations
It is impossible to add a non-nullable field 'owner' to topic without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 1
Migrations for 'learning_logs':
  learning_logs\migrations\0004_topic_owner.py
    - Add field owner to topic
```

它生成了`004_topic_owner.py`迁移文件

```python
# Generated by Django 4.2.6 on 2023-11-13 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_logs', '0003_alter_entry_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

```

接下来开始迁移文件

```python
> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0004_topic_owner... OK
```

验证主题是否都关联了

```powershell
sqlite> select * from learning_logs_topic
   ...> ;
id  text           date_added                  owner_id
--  -------------  --------------------------  --------
1   chess          2023-10-23 13:30:29.738659  1
2   Rock Climbing  2023-10-23 13:31:21.454303  1
3   test           2023-11-07 12:19:12.741322  1


也可以在shell中查看

>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: chess>, <Topic: Rock Climbing>, <Topic: test>]>
>>> for topic in Topic.objects.all():
...     print(topic,topic.owner)
...
chess ll_admin
Rock Climbing ll_admin
test ll_admin
```

可以看到每个主题都关联到超级用户了

:warning: 其实也可以不用迁移数据库，而是简单的重置数据库但是这样会丢失所有的数据，`python manage.py flush`,这样就会将重建数据库结构。如果这样做那么久必须重新创建超级用户，且之前所有的数据都会丢失





#### 19.3.3 限制用户只能访问自己的主题

在`learning_logs`应用程序的`views.py`文件中，使用[`filter`]([¶ (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/models/querysets/#filter))来查询此用户的主题

```python
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
```

登录一个没有主题的用户会显示

![image-20231113140139393](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231113140139393.png)



#### 19.3.4 保护用户的主题

​	我们只是限制了每个用户的条目显示，还没有限制对显示单个主题的页面的访问，因此你还是可以通过`topics/1`来访问每个主题

![image-20231113140505804](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231113140505804.png)

​	如果需要修复这个问题久需要在`topic`视图和`edit_entry`中添加一个判断，判断访问的是不是他的所属用户，如果不是则报错404

```python
@login_required
def topic(request,topic_id):
    """显示单个主题及其所有条目,get()返回与给定的查找参数相匹配的对象"""
    topic = Topic.objects.get(id=topic_id)
    """判断是否为404"""
    if topic.owner != request.user:
        raise Http404
```

```python
def edit_entry(request,entry_id):
    """在Entry模型中查早entry_id"""
    entry = Entry.objects.get(id=entry_id)
    """匹配主题，在entry的条目中会显示是哪个主题的条目"""
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
```

![image-20231113141922852](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231113141922852.png)





#### 19.3.6 将新主题关联到当前用户

​	现在用户如果创建一个新主题会博爱错`InterityError`指出`Learning_logs_topic.user.id`不能为Null

![image-20231113142124512](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Django-WebAppimage-20231113142124512.png)

也就是说，我们在创建主题了时候并没有给定`user`，在创建主题视图添加：

```python
@login_required
def new_topic(request):
.....
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
    
```



#### 练习 19.3

在  `views.py` 中，我们在两个地⽅核实了主题关联到的⽤户为当前登录的⽤户。请将执⾏该检查的代码放在函数`check_topic_owner`() 中，并在这两个地⽅调⽤这个函数。

```python
@login_required
def topic(request,topic_id):
    """显示单个主题及其所有条目,get()返回与给定的查找参数相匹配的对象"""
    topic = Topic.objects.get(id=topic_id)
    """判断是否为404"""
    check_topic_owner(request,topic)

    
@login_required
def edit_entry(request,entry_id):
    """在Entry模型中查早entry_id"""
    entry = Entry.objects.get(id=entry_id)
    """匹配主题，在entry的条目中会显示是哪个主题的条目"""
    topic = entry.topic
    """判断访问者是否是本所属用户"""
    check_topic_owner(request,topic)

def check_topic_owner(request,topic):
    if topic.owner != request.user:
        raise Http404
```



#### 练习19.4

保护⻚⾯ `new_entry` ⼀个⽤户可以在另⼀个⽤户的学习笔记中添加条⽬，⽅法是在  URL 中指定属于另⼀个⽤户的主题的  ID。为了防范这种攻击，请在保存新条⽬前，核实它所属的主题归属于当前⽤户。

```python
@login_required
def new_entry(request,topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    """添加"""
    check_topic_owner(request,topic)
    if request.method != 'POST':
        form = EntryForm()
```







# 20 设置应用程序的样式并部署

:star: 当前学习笔记的功能虽然很齐备的，但是没有设置样式，只能算是个'毛坯房'，而且只能在本地计算机上运行本章节会学习到：

:one: 使用[`boostrap`](https://v5.bootcss.com/docs/getting-started/introduction/)库来设置样式，它是用于设置Web应用程序样式的工具，可以兼容任何设备

:two: 将项目部署到`platform.sh`上，这个网站可以将项目推送到其服务器上。



## 20.1 设置项目学习笔记的样式

前面章节已经将学习笔记的项目框架给搭建起来了，但是没有考虑到样式设计问题，在程序设计中外观是非常重要一个环境，只有外观好看了才可以使得用户想用



### 20.1.1 下载`django-·bootstrap5`

使用pip下载[`django-bootstrap5`](https://pypi.org/project/django-bootstrap5/)

```cmd
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> pip install django-bootstrap5
```

添加到`settings.py`中

```python
INSTALLED_APPS = [
    #我的应用程序
    'learning_logs',
    'accounts',
    #第三方应用程序
    'django_bootstrap5'
    #默认应用程序
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



### 20.1.2 使用Bootstrap-django设置样式















































## 其他



### 一、修改应用程序名称

要修改Django应用程序的名字，您需要执行以下步骤：

1. 打开您的Django项目的settings.py文件。
2. 在文件中找到`INSTALLED_APPS`列表。
3. 在该列表中找到您的应用程序名称，它通常是以字符串形式列出的。
4. 修改该字符串以反映您希望更改的应用程序名称。
5. 如果您的应用程序使用了自定义的模板，您还需要更新模板文件夹的名称以匹配新的应用程序名称。**这通常涉及将模板文件夹的名称**从`app_name`改为新的应用程序名称如`app.py`文件。
6. 如果您的应用程序使用了自定义的管理页面模板，您需要更新这些模板以匹配新的应用程序名称。这通常涉及将模板文件中的`app_name`替换为新的应用程序名称。
7. 运行以下命令更新数据库：
```shell
python manage.py makemigrations
python manage.py migrate
```
8. 最后，更新所有引用到该应用程序的地方，包括URLs、视图函数、模型等，以使用新的应用程序名称。

请注意，这些步骤可能会因您的项目结构和配置而有所不同。在进行更改之前，最好备份您的项目，以防意外发生。





### 二、Django修改对接的数据库(Mysql/MariaDB)

参考[配置 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#std-setting-DATABASE-ENGINE)

在文件中找到`setting.py`文件，搜索如下，复制它，然后注释掉它，然后修改

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

修改为：

```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': BASE_DIR / 'flowers.sql', 如果这里是用链接本地或者远程的mysql环境，而不是本地文件
        'NAME': 'flowers', #只需要填写数据库名称就好
        "USER": "root",
        "PASSWORD": "000000",
        "HOST": "127.0.0.1",
        "PORT":"3306",
    }
}
```

随后使用 `pip install mysqlclient`下载Python操作数据库的的组件

打开mariadb创建数据库

```mysql
MariaDB [(none)]> create database flowers
    -> ;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| flowers            |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.001 sec)
```

链接数据库：

```CMD
(flowers) PS D:\资料\example\example\python笔记\code\鲜花库存管理系统\flowers\Scripts> .\python.exe .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
