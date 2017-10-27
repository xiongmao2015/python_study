from django.http import HttpResponseRedirect
# 装饰器的编写,必须有一个返回值。
def login_requied(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key("username"):
            # 如果登陆了，就返回刚才的网页。
            return func(request,*args,**kwargs)
        else:
            result=HttpResponseRedirect('/login/')
            result.set_cookie('url',request.get_full_path(),expires=20)
            return result
    return login_fun

# 不能少了最后一句。
