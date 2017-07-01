from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#分类
class Category(models.Model):
    name = models.CharField(max_length=100)
#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField() #创建时间
    modified_time = models.DateTimeField() #修改时间
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category) #一对多