from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """
    自定义用户类继承django自带的用户系统
    """
    telephone = models.CharField(max_length=20, verbose_name='手机号')
    questions = models.ManyToManyField('Question')




class Question(models.Model):
    title = models.CharField(max_length=50,verbose_name="投票问题")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return  self.title
    class Meta:
        ordering = ["-create_time"]
        verbose_name = "投票问题"
        verbose_name_plural = "投票问题"
class Choices(models.Model):
    content = models.CharField(max_length=50, verbose_name="选项")
    votes = models.PositiveIntegerField(verbose_name="得票数")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    def __str__(self):
        return self.content
    class Meta:
        ordering = ["-create_time"]
        verbose_name = "选项"
        verbose_name_plural = "选项"

