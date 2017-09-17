# coding=utf-8
from django.db import models

# Create your models here.

# 首页轮播表
# verbose_name:后台显示的别名,也可以用于显示，搜索
# choices:下拉显示表
# default:默认
# max_length:为字数大小。
# 图片防止在upload,专门的文件中
# auto_now_add：时间自动添加
class Banner(models.Model):
    name = models.CharField(verbose_name='名称',max_length=30)
    status_choice =[(0,'下线'),(1,'上线')]
    status=models.IntegerField(choices=status_choice, verbose_name='状态',default =1)
    weight =models.IntegerField(verbose_name='权重:从大到小',default=0)
    img = models.ImageField(verbose_name='banner图片',upload_to='banner/')  # upload路经。加载路径
    href = models.CharField(verbose_name='图片链接',max_length=300)  # 点击图片的连接
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural=verbose_name='首页轮播表'

    def __unicode__(self):
        return self.name

# 公告表:
class Notice(models.Model):
    title = models.CharField(verbose_name='标题',max_length=30)
    status_choice=[(0,'下线'),(1,'上线')]
    status= models.IntegerField(choices=status_choice,verbose_name='公告是否上线',default=1)
    weight = models.IntegerField(verbose_name='权重',default=0)
    description=models.CharField(verbose_name='简介',max_length=100)
    content=models.TextField(verbose_name='内容')  # 自动识别大小

    class Meta:
         verbose_name_plural=verbose_name='公告'

    def __unicode__(self):
         return self.title


# 课程表
class Course(models.Model):
    name = models.CharField(verbose_name='课程名称',max_length=30)
    status_choice=[(0,'下线'),(1,'上线')]
    status=models.IntegerField(choices=status_choice,verbose_name='课程时候上线',default=1)
    weight = models.IntegerField(verbose_name='权重',default=0)
    description=models.CharField(verbose_name='课程简介',max_length=100)
    img = models.ImageField(verbose_name='课程封面',upload_to='course/')

    class Meta:
        verbose_name_plural=verbose_name='课程介绍表'
    def __unicode__(self):
        return self.name

# 学生表
class Student(models.Model):
    name=models.CharField(verbose_name='学生姓名',max_length=30,null=False)
    status_choice=[(0,'下线'),(1,'上线')]
    status=models.IntegerField(choices=status_choice,default=1,verbose_name='学生是否上线')
    weight=models.IntegerField(verbose_name='权重',default=0)
    avatar=models.ImageField(verbose_name='学生头像',upload_to='avatar/')
    company = models.CharField(verbose_name='就业公司',max_length=100)
    salary = models.CharField(verbose_name='就业工资',max_length=30)

    class Meta:
        verbose_name_plural=verbose_name='学生表'
    def __unicode__(self):
        return self.name

# 学生详情表
class StuDetail(models.Model):
    student = models.OneToOneField('Student')
    weight = models.IntegerField(verbose_name='权重',default=0)
    letter=models.TextField(verbose_name='感谢信') # 这里是text格式的
    class Meta:
        verbose_name_plural=verbose_name='学生详情表'
    def __unicode__(self):
        return self.student.name   # 这里显示的也是详情。

# 招聘信息表
class Recruit(models.Model):
    status_choice = [(0,'下线'),(1,'上线')]
    status = models.IntegerField(choices=status_choice,verbose_name='招聘是否上线',default=1)
    weight = models.IntegerField(verbose_name='权重：从大到小', default=0)

    title = models.CharField(verbose_name='标题',max_length=100)
    company = models.CharField(verbose_name='公司',max_length=200)
    salary = models.CharField(verbose_name='薪水',max_length=30)
    content = models.TextField(verbose_name='详情')
    date_dead = models.DateTimeField()

    class Meta:
        verbose_name_plural = verbose_name = '招聘信息'

    def __unicode__(self):
        return self.title

# 合作企业表
class Cooperation(models.Model):
    name=models.CharField(verbose_name='公司名称',max_length='100')
    weight = models.IntegerField(default=0,verbose_name='权重')
    logo=models.ImageField(verbose_name='企业logo',upload_to='logos/')
    link=models.CharField(verbose_name='链接地址',max_length=300)
    class Meta:
        verbose_name_plural=verbose_name='合作企业'
    def __unicode__(self):
        return self.name

# 建立老师表
class Teacher(models.Model):
    name=models.CharField(verbose_name='老师表',max_length='100')
    status_choice = [(0, '下线'), (1, '上线')]
    status = models.IntegerField(choices=status_choice,default=1,verbose_name='学生是否上线')
    weight = models.IntegerField(verbose_name='权重',default=0)
    teaimg = models.ImageField(verbose_name='教师头像',upload_to='teacherimage/')
    description = models.TextField(verbose_name='教师简介')
    class Meta:
        verbose_name_plural=verbose_name='教师表'
    def __unicode__(self):   # 在表格中显示出来的是什么,。
        return self.name

# 方向表
class Direaction(models.Model):
    weight = models.IntegerField(verbose_name='权重',default=0)
    name = models.CharField(verbose_name='名称',max_length=32)
    classification=models.ManyToManyField('Classification')  # 多对多关系

    class Meta:
        db_table='Direction'
        verbose_name_plural=verbose_name='方向'

    def __unicode__(self):
        return self.name

# 视频分类表,与方向是多对多的关系，python可以做很多方向，一个方向可以有很多的语言去做
class Classification(models.Model):
    weight = models.IntegerField(verbose_name='权重',default=0)
    name = models.CharField(verbose_name='名称',max_length=30)

    class Meta:
        db_table='Classification'
        verbose_name_plural=verbose_name='分类'
    def __unicode__(self):
        return self.name

#视频，与分类是一对多关系
class Video(models.Model):
    status_choice=((0,'下线'),(1,'上线'))
    level_choice = ((1,u'初级'),(2,u'中级'),(3,u'高级'))  # 不变成unicode,会照成影响。

    status = models.IntegerField(verbose_name='状态',choices = status_choice,default=1)
    level=models.IntegerField(verbose_name='级别',choices=level_choice,default=1)
    classification= models.ForeignKey('Classification',null=True,blank =True)
    weight = models.IntegerField(verbose_name='权重',default=0)
    title=models.CharField(verbose_name='标题',max_length =32)
    img = models.ImageField(verbose_name='图片',upload_to='./static/images/Video')
    href = models.CharField(verbose_name='视频地址',max_length=256)
    create_date =models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Video'
        verbose_name_plural=verbose_name='视频'
    def __unicode__(self):
        return self.title