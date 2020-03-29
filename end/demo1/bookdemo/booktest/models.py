from django.db import models

# Create your models here.
#MVT M 数据模型
#ORM M 数据模型
#在此处编写应用的数据模型类

#有了数据模型之后如何与数据库交互
#1.注册模型 在settings.py中的INSTALLED_APPS 添加应用名booktest后面加，号
#2.生成迁移文件 用于与数据库交互 python manage.py makemigrations   会在对应文件生成迁移文件
#3.执行迁移 会在对应的数据库中生成对应的表 python manage.py migrate


class UserManager(models.Manager):
    """
    自定义模型管理类，该模型不再具有objects对象
    """
    def deleteByTelephone(self,tele):
        #django 默认的objects 是Manager类型
        user = self.get(telephone=tele)
        user.delete()
    def createUser(self,tele):
        #self.model可以获取模型类和构造函数
        user = self.model()
        user.telephone = tele
        user.save()
class User(models.Model):
    telephone = models.CharField(max_length=11,null=True,blank=True,verbose_name='手机号码')
    #自定义管理字段
    objects = UserManager()
    def __str__(self):
        return self.telephone
    class Meta:
        #表明
        db_table = "用户表"
        ordering = ["-telephone"]
        # admin 页面进入模型类显示名字
        verbose_name = "用户模型类a"
        #admin 页面在应用下方显示的模型名
        verbose_name_plural = "用户模型类s"
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
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="heros")
    def __str__(self):
        return self.name
class Account(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True, verbose_name="注册日期")
    # concact = models.OneToOneField('Concact',on_delete=models.CASCADE)
class Concact(models.Model):
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(default="1720039961@qq.com")
    account = models.OneToOneField(Account,on_delete=models.CASCADE,related_name="con")
class Article(models.Model):
    title = models.CharField(max_length=20,verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")
class Tag(models.Model):
    name = models.CharField(max_length=10,verbose_name="标签名")
    articles = models.ManyToManyField(Article, related_name="tags")
#一对多 一方book 多方hero 实例:关联字段定义在多方
#一找多 b.hero_set.all() 如果定义过related_name 则使用 b.heros.all()
#多找一 h.book

#一对一 一方Account 实例a  一方Concact 实例c 关联字段定义在任意一方
#a找c a.concact
#c找a c.account

#多对多 多方Article 实例a 多方Tag 实例t  关联字段定义在任意一方
#添加关系 t.articles.add(a) 移除关系 t.articles.remove(a)
#a 找所有的t a.tag_set.all() 如果定义过related_name 则使用 a.tags.all()
#t找所有的a t.articles.all()