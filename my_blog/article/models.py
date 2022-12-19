from django.db import models
#导入内建的user模型
from django.contrib.auth.models import User
#处理时间相关的事物
from django.utils import timezone
# Create your models here.

#博客的数据模型
class ArticlePost(models.Model):
    #文章作者。on——delete删除
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #tittle 
    title = models.CharField(max_length=100)
    #body
    body = models.TextField()
    #create time
    created = models.DateTimeField(default=timezone.now)
    #update time
    updated = models.DateTimeField(auto_now=True)
    #定义内部类和方法规范行为
    #内部类class Meta用于定义元数据
    class Meta:
      #ordering 模型返回的数据的排列顺序
      #'-created'倒序
      ordering = ('-created',)
    def __str__(self):
      #返回文章标题
      return self.title
