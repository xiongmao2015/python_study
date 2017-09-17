# coding=utf-8
from django.contrib import admin
import models

# Register your models here.

# 内嵌
class StuDetailInline(admin.StackedInline):
    model=models.StuDetail
    extra =1   # 内嵌表
class StudentAdmin(admin.ModelAdmin):
    inlines=[StuDetailInline]
# 注册
admin.site.register(models.Banner)
admin.site.register(models.Student,StudentAdmin)
admin.site.register(models.StuDetail)
admin.site.register(models.Cooperation)
admin.site.register(models.Course)
admin.site.register(models.Notice)
admin.site.register(models.Recruit)
admin.site.register(models.Teacher)

admin.site.register(models.Classification)
admin.site.register(models.Direaction)
admin.site.register(models.Video)