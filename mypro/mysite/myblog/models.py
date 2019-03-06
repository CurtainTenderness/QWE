from django.db import models
from tinymce.models import HTMLField

# Create your models here.

# 定义作者类
class Users(models.Model):
    # 作者编号
    id=models.AutoField(primary_key=True)
    # 作者姓名
    name = models.CharField(max_length=30,unique=True,verbose_name='姓名 ')
    # 密码
    password=models.CharField(max_length=30)
    # 邮箱
    email=models.EmailField()
    # 年龄
    age=models.IntegerField()

# 定义文章类型
class Article(models.Model):
    # 文章编号
    id=models.AutoField(primary_key=True)
    # 文章题目
    title=models.CharField(max_length=255,verbose_name='标题')
    # 文章内容
    # content=models.TextField()
    content=HTMLField(verbose_name='内容')
    # 文章作者，外键引用作者类型
    author=models.ForeignKey(Users,on_delete=models.CASCADE)
    # 使用这个使标题能够显示
    def __str__(self):
        return self.title