from django.db import models
from django.contrib.auth.models import User
from django.urls import  reverse


# Create your models here.
#分类
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField() #创建时间
    modified_time = models.DateTimeField() #修改时间
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category) #一对多
    tags = models.ManyToManyField(Tag, blank=True) #多对多
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title
    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})