# coding=utf-8
from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect,HttpResponseRedirect
from django.core.urlresolvers import reverse

import models
# Create your views here.
def index(request):
    # 帅选出上线的然后根据权重排序，
    banner_list=models.Banner.objects.filter(status=1).order_by('-weight').all()
    notice_list=models.Notice.objects.filter(status=1).order_by('-weight').all()
    course_list= models.Course.objects.filter(status=1).order_by('-weight').all()[0:6]
    student_detail = models.StuDetail.objects.filter(student__status=1).order_by('-weight').first()  # 调用一对一关系
    student_list = models.Student.objects.filter(status=1).order_by('salary').all()[0:5]   # 这里的排序不是按照数字排序,是按照字符排序
    recruit_list=models.Recruit.objects.filter(status=1).all()
    cooperation_list=models.Cooperation.objects.all().order_by('weight')
    context={
        'banner_list':banner_list,
        'notice_list':notice_list,
        'course_list':course_list,
        'student_detail':student_detail,
        'student_list':student_list,
        'recruit_list':recruit_list,
        'cooperation_list':cooperation_list,
    }
    return render(request,'home/index.html',context)

#学生函数
def student(request):
    student_list=models.StuDetail.objects.all()
    context={
        'student_list':student_list,
    }
    return render(request,'home/student.html',context)

# 老师函数
def teacher(request):
    teacher_list=models.Teacher.objects.all()
    context={
       'teacher_list':teacher_list
    }
    return render(request,'home/teacher.html',context)

# 公告详情页：
def noticeDetail(request):
    nid=request.GET.get('nid',None)
    if nid is not None:
        notice = models.Notice.objects.get(pk=nid)  # 直接get,获取对象。
        return render(request,'home/notice_detail.html',{'notice':notice})
    else:
        # return HttpResponse('没有找到')
        # return HttpResponseRedirect('/index/')
        return HttpResponseRedirect(reverse(index))

def video(request,did,cid,lid):
    q={}   # q是用来组合查询条件的。
    q['status']=1
    did = int(did)  #获取的为字符串，需要转化为整形
    cid = int(cid)
    lid = int(lid)
    print cid,did,lid
    direaction_list = models.Direaction.objects.all()  # 这是展示所有选项，
    if did ==0:   # 所有方向，需要展示的class.
        cls_list = models.Classification.objects.all()
        if cid !=0:
            q['classification_id__in']=[cid,]        # 这是外键的调用：一个视频只有一个分类，一个分类有多个视频，外键在表现形式就是_id。
            # 外键的调用,如果只有一个值可以这样调用，In是过滤器。，后面是列表，相当于或了。相当于在那个列表中。
    else:  # 某个方向
        if cid==0:  # 考虑选择方向后，分类归0.
            direaction=models.Direaction.objects.get(pk=did)
            cls_list = direaction.classification.all()  # 当前方向所有分类
            cid_list = map(lambda x:x.id,cls_list)
            # q['classification_id__in']=cid_list

        else:
            direaction= models.Direaction.objects.get(pk=did)
            cls_list=direaction.classification.all()    # 多对多查询方式，注意了。
            cid_list = map(lambda x:x.id,cls_list)  # 根据cls_list查询出所有class的id.，查看有哪些id.相当于提取每个对象的id.
        #
            q['classification_id__in']=cid_list
        #
            if cid not in cid_list:  # 如果当前cid不再cid列表中。不再的话进行
                url_part=request.path.split('/')  # 分解当前url
                url_part[3]='0'  #  将分类的url 变成 0
                request.path = '/'.join(url_part)  # 重新组成url.

    if lid!=0:   # 判断一下中高初,
        q['level']= lid


    # level_list = models.Video.level_choice  #
    # 自己定义映射关系，map关系，
    level_list = map(lambda x:{'id':x[0],'name':x[1]},models.Video.level_choice) # 为了和其他地方统一,定义一个字典，转成字典结构，方便调用
    video_list=models.Video.objects.filter(**q).all()
    context={
        'direaction_list':direaction_list,
        'cls_list':cls_list,
        'level_list':level_list,
        'video_list':video_list,
    }

    return render(request,'home/video.html',context)