# coding=utf-8
from django import template

register = template.Library()
#三个标签合并为一个
@register.simple_tag
def action(path,item,index):
    url_part=path.split('/')


    if index==4:
        if str(item['id']) == url_part[index].split('.')[0]:
            rep = '<a href ="%s" class = "active">%s</a>'
        else:
            rep = '<a href ="%s">%s</a>'
        url_part[4] = str(item['id']) + '.html'
        url = '/'.join(url_part)
        name=item['name']

    else:
        # 判断确定是否为选定状态，使得话加入action.
        if str(item.id) == url_part[index]:
            rep = '<a href ="%s" class = "active">%s</a>'
        else:
            rep = '<a href ="%s">%s</a>'

        url_part[index]=str(item.id)
        url='/'.join(url_part)
        name=item.name
    rep = rep%(url,name)
    return rep

#设置'全部'的前端样式和传递参数：,区别，不需要传item,及显示的对象了
@register.simple_tag
def action_all(path,index):
    url_part = path.split('/')
    if index ==4:
        if url_part[index].split('.')[0]=='0':
            rep='<a href="%s" class="active">%s</a>'
        else:
            rep='<a href="%s">%s</a>'
        url_part[index]='0'+'.html'
        url = '/'.join(url_part)
    else:
        if url_part[index]=='0':
            rep = '<a href="%s" class="active">%s</a>'
        else:
            rep= '<a href="%s">%s</a>'
        url_part[index]='0'
        url='/'.join(url_part)
    rep = rep %(url,u'全部')  # 这里的中文需要转化一下。
    return rep







# 生成方向a标签,
@register.simple_tag
def action1(path,item):
    url_part = path.split('/')  # 获取path的值，然后字符串切割
    url_part[2]=str(item.id)  # 把did给值。did切割完后是unicode,如果连接需要转化为字符串
    url = '/'.join(url_part)    # 然后再结合，就是为了把did放进去。重新生成路由地址
    # 生成a标签，直接调用。
    rep = '<a href ="%s">%s</a>' %(url,item.name)
    return rep

@register.simple_tag
def action2(path,item):
    url_part = path.split('/')  # 获取path的值，然后字符串切割
    url_part[3]=str(item.id)  # 把did给值。did切割完后是unicode,如果连接需要转化为字符串
    url = '/'.join(url_part)    # 然后再结合，就是为了把did放进去。重新生成路由地址
    # 生成a标签，直接调用。
    rep = '<a href ="%s">%s</a>' %(url,item.name)
    return rep

# 这个与其他的还不太一样。
@register.simple_tag
def action3(path,item):
    url_part = path.split('/')  # 获取path的值，然后字符串切割
    print url_part
    url_part[4]=str(item['id'])+'.html'  # 把did给值。did切割完后是unicode,如果连接需要转化为字符串
    url = '/'.join(url_part)    # 然后再结合，就是为了把did放进去。重新生成路由地址
    # 生成a标签，直接调用。
    rep = '<a href ="%s">%s</a>' %(url,item['name'])
    return rep