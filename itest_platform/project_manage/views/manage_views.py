from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required   # 控制视图是否允许在未登陆时访问
from project_manage.models import Project,Module


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
def project_add(request):
    return render(request, "project/add.html")




