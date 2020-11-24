from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required   # 控制视图是否允许在未登陆时访问
from project_manage.models import Project,Module

# Create your views here.
def hello(request):
    # return  HttpResponse("hello django")  # HttpResponse 返回的是字符串
    # return render(request,"hello.html")
    if request.method == "GET":
        name = request.GET.get('name' , "")
        print(name)
        return render(request,'hello.html', {"n":name})  # {"n":name} 字典

#
# def index(request):
#     """
#     返回index.html登陆页面
#     :param request:
#     :return:
#     """
#     return render(request,"index.html")


def index(request):
    """
    :param request:
    :return:
    """
    # 返回登陆页面
    if request.method == "GET":
        return render(request,"login.html")

    #处理登录数据
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password", "")

        print(username,password)
        if username =="" or password == "":
            return render(request, "login.html", {"error": "The username or password is empty !!"})

        user = auth.authenticate(username=username, password=password)
        print("====>", user)

        if user is not None:
            auth.login(request, user)  #到数据库写session
            # return render(request, "manage.html")
            # return HttpResponseRedirect("/manage/")
            response = HttpResponseRedirect('/manage/')
            # response.set_cookie("user", username, 3600)  # F12的application的cookies, 设置cookies多久后过期.key是user,value是登录名
            # 直接设置cookie到浏览器不安全，应该设置session id,session id对应的数据写在数据库里面的
            request.session['user'] = username
            return response
        else:
            return render(request, 'login.html', {"error": "Wrong user name or password！！"})

        # if username =="" or password == "":
        #     return render(request, "index.html", {"error": "The username or password is empty !!"})
        #
        # if username == "admin" and password == '123456':
        #     return render(request, "index.html", {"error": "login successfully！ "})
        # else:
        #     return render(request,'index.html' , {"error": "Wrong user name or password！！"})

@login_required  # 用户不登陆时不能进入
def manage(request):
    """
    系统管理页面
    :param request:
    :return:
    """
    projects = Project.objects.all()

    # username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    return render(request, "manage2.html", {'user':username, "projects":projects})

@login_required
def logout(request):
    """
    退出登陆
    :param request:
    :return:
    """
    auth.logout(request) # 到数据库删除session key
    return HttpResponseRedirect('/index/')