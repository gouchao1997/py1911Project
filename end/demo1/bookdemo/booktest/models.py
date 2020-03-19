from django.db import models

# Create your models here.
#MVT M 数据模型
#ORM M 数据模型
#在此处编写应用的数据模型类

#有了数据模型之后如何与数据库交互
#1.注册模型 在settings.py中的INSTALLED_APPS 添加应用名booktest后面加，号
#2.生成迁移文件 用于与数据库交互 python manage.py makemigrations   会在对应文件生成迁移文件
#3.执行迁移 会在对应的数据库中生成对应的表 python manage.py migrate
class Book(models.Model):
    """
    book继承了Model类 因为Model类拥有操作数据的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")
    def __str__(self):
        return self.title
class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='male')
    content = models.CharField(max_length=100)
    #book 是一对多中的外键 on_delete代表删除主表数据时如何做
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.name