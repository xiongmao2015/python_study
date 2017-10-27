from django.shortcuts import render

from django.shortcuts import render, redirect, reverse, \
    HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt, \
    csrf_protect
from .models import UserInfo, MovieInfo
from hashlib import sha1
from . import user_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        passwd = request.POST.get('password', None)
        if username != '' and passwd != '':
            try:
                res = UserInfo.objects.get(
                    username=username)
                print(res)
                s1 = sha1()
                s1.update(passwd.encode('utf8'))
                passwd2 = s1.hexdigest()
                if passwd2 == res.password:
                    url = request.COOKIES.get('url',
                                              '/main/')
                    red = HttpResponseRedirect(url)
                    request.session['username'] = username
                    request.session.set_expiry(0)
                    return red
            except Exception as e:
                print(e)
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')


def Register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        passwd1 = request.POST.get('password1', None)
        passwd2 = request.POST.get('password2', None)
        print(username, passwd1, passwd2)
        if passwd1 != '' and passwd2 != '':
            if passwd1 == passwd2:
                s1 = sha1()
                s1.update(passwd1.encode('utf8'))
                passwd3 = s1.hexdigest()
                user = UserInfo()
                user.username = username
                user.password = passwd3
                user.save()
                return redirect(reverse('login'))
            else:
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')


def check_username(request):
    username = request.GET.get('username', None)
    message = "ok"
    if username == '':
        message = "none"
        return HttpResponse(message)
    else:
        try:
            res = UserInfo.objects.get(username=username)
            message = "用户名已经存在"
            return HttpResponse(message)
        except Exception as e:
            return HttpResponse(message)


@user_decorator.login_requied
def MainPage(request):
    username = request.session.get('username')
    print(username)
    return render(request, 'main.html',
                  {'username': username})


def IndexPage(request):
    movies = MovieInfo.objects.all()
    username = request.session.get("username", None)
    if username is None:
        return render(request, 'index.html',
                      {'movies': movies})
    else:
        user = UserInfo.objects.get(username=username)
        userlist = user.mymovies.all()
        return render(request, 'index.html',
                      {'movies': movies,
                       'userlist': userlist})  # 注意加引号


# 这个必须登陆
@csrf_exempt
def MylikePage(request):
    message = "no"
    if request.session.has_key("username"):
        try:
            movieid = request.POST.get("movieid")
            movieobject = MovieInfo.objects.get(
                postid=movieid)
            print(movieobject)
            username = request.session.get("username")
            user = UserInfo.objects.get(username=username)
            print(user)
            user.mymovies.add(movieobject)
            message = "ok"
            return HttpResponse(message)
        except Exception as e:
            return HttpResponse(message)
    else:
        return HttpResponse(message)


@user_decorator.login_requied
def DellikePage(request):
    message = "no"
    try:
        movieid = request.GET.get("movieid")
        movieobject = MovieInfo.objects.get(postid=movieid)
        print(movieid)
        username = request.session.get("username")
        user = UserInfo.objects.get(username=username)
        user.mymovies.remove(movieobject)
        message = "ok"
        return HttpResponse(message)
    except Exception as e:
        return HttpResponse(message)


def LikePage(request):
    username = request.session.get("username")
    user = UserInfo.objects.get(username=username)
    movies = user.mymovies.all()
    return render(request, "like.html", {'movies': movies})


def Logout(request):
    request.session.flush()
    return redirect(reverse('indexpage'))
