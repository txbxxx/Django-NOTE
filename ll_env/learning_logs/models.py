from django.db import models

# Create your models here.
"""定义主题模型"""
class Topic(models.Model):
    """属性Text是由字符组成的数据，就是文本，需要存储少量的文本文件，名称、标题等，且需要高数Django在数据库中预留多少空间即max_length"""
    text = models.CharField(max_length=200)
    """记录日期和实践的数据，且当用户创建新主题时，会自动设置为当前的时间"""
    date_added = models.DateTimeField(auto_now_add=True)
    
    """当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据"""
    def __str__(self):
        """默认使用text格式来来显示有关主题的信息，返回存储在属性text中的字符串"""
        # return f"{self.text} - {self.date_added}"
        return f"{self.text}"


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
    
    def __str__(self):
        """显示文本的前50个字符后续字符用......"""
        # return f"{self.text[:50]}..."  原始
        """字符大于50就前50个字符和显示....号，小于则不会显示"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
