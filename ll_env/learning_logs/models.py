from django.db import models

# Create your models here.

class Topic(models.Model):
    """属性Text是由字符组成的数据，就是文本，需要存储少量的文本文件，名称、标题等，且需要高数Django在数据库中预留多少空间即max_length"""
    text = models.CharField(max_length=200)
    """记录日期和实践的数据，且当用户创建新主题时，会自动设置为当前的时间"""
    date_added = models.DateTimeField(auto_now_add=True)
    
    """当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据"""
    def __str__(self):
        """默认使用text格式来来显示有关主题的信息，返回存储在属性text中的字符串"""
        return self.text