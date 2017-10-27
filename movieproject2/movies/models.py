from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=20,verbose_name="用户名",blank=False)
    password=models.CharField(max_length=60,verbose_name="密码")
    mymovies=models.ManyToManyField("MovieInfo",verbose_name="我的收藏")
    myimg=models.ImageField(upload_to="myimg/",verbose_name="我的图片",blank=True)
    class Meta:
        verbose_name_plural=verbose_name="用户"
    def __str__(self):
        return self.username

class MovieInfo(models.Model):
    postid=models.IntegerField(verbose_name="电影号")
    title=models.CharField(max_length=30,verbose_name="电影名",blank=False)
    image=models.CharField(max_length=100,verbose_name="电影宣传图")
    class Meta:
        verbose_name_plural=verbose_name="电影"
    def __str__(self):
        return self.title