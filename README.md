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
3. 表单处理，Django提供了表单处理的功能，可以方便地创建和验证表单。开发者可以使用它的表单累来生成HTNML表单

下面来下载Django

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

接下来我们在models中输入

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
        return self.text
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

​	此外还可以使用`sqlmigrate`来查看使用的哪些`sql`命令来创建的表，它并不会创建表，只是输出命令到屏幕

```sqlite
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env> python.exe .\manage.py sqlmigrate learning_logs 0001
BEGIN;
--
-- Create model Topic
--
CREATE TABLE "learning_logs_topic" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "text" varchar(200) NOT NULL, "date_added" datetime NOT NULL);
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

​	刚刚创建了国际象棋和攀岩的主题，如果我们要记录这些的知识，那么用户就必须在学习笔记中添加条目。
