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



#### 18.1.4安装Django

Django是一个开源的Web应用框架，是由Python完成，

1. Django提供了强大的ORM（对象关系映射），使得用户可以直接使用Python来操作数据库，无需编写SQL语句
2. 自动化的管理后台，Django提供一个自动生成的管理后台，可以方便地对数据库的内容进行增删改查操作，管理后台还可以自定义扩展
3. 表单处理，Django提供了表单处理的功能，可以方便地创建和验证表单。开发者可以使用它的表单累来生成HTNML表单

下面来下载Django

```powershell
(ll_env) PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\Scripts> deactivate
PS D:\资料\example\example\python笔记\code\Web应用程序\ll_env\Scripts>
```



#### 18.1.5 在Django中创建项目

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



##### 18.1.6创建数据库

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



